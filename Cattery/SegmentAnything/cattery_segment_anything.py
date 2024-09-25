import nuke 
import sys

def on_create():
    this = nuke.thisNode()
    inference = nuke.toNode(f"{this.name()}.Inference1")
    this["gpuName"].setValue(inference["gpuName"].value())
    this["channelsIn"].setValue("rgba.red, rgba.green, rgba.blue")
    inference.forceValidate()
    is_enabled = inference["modelFile"].enabled()
    if (sys.platform.lower() == "darwin") and (not inference["useGPUIfAvailable"].enabled()): this["useGPUIfAvailable"].setValue(False), this["useGPUIfAvailable"].setEnabled(False)
    if not is_enabled:
        for k in this.knobs(): this[k].setEnabled(False)
    
def knob_changed():
    node = nuke.thisNode()
    single_mask_knobs = ['add_to_mask','remove_from_mask', 'view_mode']
    multi_mask_knobs = ['create_crypto_matte']
    ensure_node_connection()
    if node['mode'].value().lower() == 'multi mask':
        for i in single_mask_knobs:
            node[i].setVisible(False)
        node[multi_mask_knobs[0]].setVisible(True)
        node["channelsIn"].setValue("rgba.red, rgba.green, rgba.blue")

    else:
        for i in single_mask_knobs:
            node[i].setVisible(True)
        node[multi_mask_knobs[0]].setVisible(False)
        node["channelsIn"].setValue("rgba.red, rgba.green, rgba.blue, motion.red, motion.green")

def unique_name(node):
    ''' Create unique name for point knobs '''

    name = [ i for i in node.knobs() if ('subtract' in i or 'add' in i) and not ('points' in i or 'mask' in i)]
    if len(name) > 0:
        name = max([int(i.split('_')[-1]) for i in name])
        return name + 1
    else:
        return 0

def get_expression_nodes():
    return nuke.allNodes('Expression')

def are_expression_there():
    return True if get_expression_nodes() else False

def set_up_merge(expression_nodes):
    ''' Function to ensure that merge node exists and is connected correctly to the nodes '''

    if not nuke.toNode('Merge1'):
        merge = nuke.createNode('Merge2', inpanel=False)
        merge['operation'].setValue('screen')
        for idx, i in enumerate(expression_nodes):
            if idx > 1:
                idx += 1
            merge.setInput(idx, i)
    else:
        merge = nuke.toNode('Merge1')
        for idx, i in enumerate(expression_nodes):
            if idx > 1:
                idx += 1
            merge.setInput(idx, i)
    return merge

def ensure_node_connection():
    ''' Function to make sure that all the important nodes are correctly connected'''

    nuke.toNode('Shuffle1').setInput(0, nuke.toNode('Dot4'))
    nuke.toNode('Output1').setInput(0, nuke.toNode('Switch3'))
    nuke.toNode('Switch1').setInput(0, nuke.toNode('Copy1'))  
    if nuke.thisNode()['mode'].value() == 'Multi Mask':
        nuke.toNode('Switch1').setInput(0, nuke.toNode('Reformat2'))

def remove_point(node, knob_name):
    ''' Function to remove points from knob and delete the associated expression node within the script '''

    # Knobs to delete
    _knob = knob_name.replace('delete_','')
    _size_knob = f'size_{_knob}'
    _delete_knob = knob_name
    
    with node:
        
        # Delete expression node and associated knobs
        _expresion_nodes = get_expression_nodes()
        _are_expression_there = are_expression_there()
        [nuke.delete(i) for i in _expresion_nodes if _knob in i['expr0'].value() or _knob in i['expr1'].value()]
        node.removeKnob(node[_knob])
        node.removeKnob(node[_size_knob])
        node.removeKnob(node[_delete_knob])

        # Rearrange the inputs of the merge node / delete if needed
        _expresion_nodes = get_expression_nodes()
        _are_expression_there = are_expression_there()
        if len(_expresion_nodes) > 1:
            set_up_merge(_expresion_nodes)
        elif len(_expresion_nodes) == 1 and nuke.toNode('Merge1') != None:
            merge = nuke.toNode('Merge1')
            if merge:
                nuke.delete(merge)
                nuke.toNode('Shuffle1').setInput(1, _expresion_nodes[0])
        else:
            nuke.toNode('Shuffle1').setInput(1,nuke.toNode('Crop1'))

        # Ensure nodes are correctly connected
        ensure_node_connection()
         

def create_new_points(node, _is_negative = False):
    '''Create new points within the gizmo and add the relevant knobs to the group node'''

    # Create name convention for the knobs
    suffix = 'subtract' if _is_negative else 'add'
    name = f'{suffix}_{str(unique_name(node))}'

    # Create point knob
    point_knob = nuke.XY_Knob(name,name.replace('_',' ').capitalize())
    point_knob.setTooltip('XY coordinate of the point passed to the model.')
    point_knob.setDefaultValue((node.width()/2, node.height()/2))
    node.addKnob(point_knob)

    # Create point size knob and ensure it's not on a new line
    pixel_size_name = f'size_{name}'
    size_knob = nuke.Int_Knob(pixel_size_name, 'Point size')
    size_knob.setDefaultValue((5,))
    size_knob.clearFlag(nuke.STARTLINE)
    size_knob.setTooltip('Set the size of the point that is passed to the model.')
    node.addKnob(size_knob)

    # Create the delete point button and ensure it's not on a new line
    py_knob = nuke.PyScript_Knob(f'delete_{name}', 'Delete point')
    py_knob.setValue(f"this_node = nuke.thisNode()\nthis_knob = 'delete_{name}'\ncattery_segment_anything.remove_point(nuke.thisNode(), this_knob)")
    py_knob.setTooltip('Delete this point.')
    py_knob.clearFlag(nuke.STARTLINE)
    node.addKnob(py_knob)

    with node:
        # Set up the expression nodes
        _expresion_nodes = get_expression_nodes()
        _are_expression_there = are_expression_there()
        expr = nuke.createNode('Expression', inpanel = False)
        _expresion_nodes.insert(-1,expr)
        expr['expr0'].setValue(f"x >=floor({node.name()}.{name}.x) - ({node.name()}.{pixel_size_name}/2) && x <=floor({node.name()}.{name}.x) + ({node.name()}.{pixel_size_name}/2) && y >=floor( {node.name()}.{name}.y) - ({node.name()}.{pixel_size_name}/2) && y <=floor( {node.name()}.{name}.y) + ({node.name()}.{pixel_size_name}/2)? 1 :0")
        expr['expr1'].setValue('0')
        expr['expr2'].setValue('0')

        if _is_negative:
            expr['expr0'].setValue('0')
            expr['expr1'].setValue(f"x >=floor({node.name()}.{name}.x) - ({node.name()}.{pixel_size_name}/2) && x <=floor({node.name()}.{name}.x) + ({node.name()}.{pixel_size_name}/2) && y >=floor( {node.name()}.{name}.y) - ({node.name()}.{pixel_size_name}/2) && y <=floor( {node.name()}.{name}.y) + ({node.name()}.{pixel_size_name}/2)? 1 :0")
        
        # Connect expression node to input and set up merge nodes if needed 
        expr.setInput(0, nuke.toNode('Input1'))
        if _are_expression_there:
            merge = set_up_merge(_expresion_nodes)
            nuke.toNode('Shuffle1').setInput(1,merge)
        else:
            nuke.toNode('Shuffle1').setInput(1, expr)

        # Ensure nodes are correctly connected
        ensure_node_connection()

def create_cryptomatte():
    '''Create a group of encryptomatte stacks so that we can use the cryptomatte node'''

    # Ensure we aren't inside the SegmentAnything gizmo
    this_node = nuke.thisNode()
    channels = nuke.toNode('Input1').channels()
    this_node.end()

    # Ensure we run the code only if the node is connected to something
    if len(channels) == 0:
        nuke.alert('The input is missing rgb, please connect the node to a Read node')
    else:
        # Set up the new group
        group = nuke.createNode('Group')
        group.setName('SegmentAnythingEncryptomatte1')
        group['tile_color'].setValue(16711935)
        with group:
            nuke.createNode('Input')
        group.setInput(0, this_node)

        with group:
            dd = nuke.createNode('Dot')

            # Create/Execute and delete curve tool to fetch maximum number of classes found by the model
            ct = nuke.createNode('CurveTool', inpanel = False)
            ct['ROI'].setValue((0,0,dd.width(), dd.height()))
            ct['operation'].setValue('Max Luma Pixel')
            ct['channels'].setValue('alpha')
            ct.setInput(0, dd)
            nuke.execute(ct,dd.firstFrame(), dd.firstFrame())
            classes = int(ct['maxlumapixvalue'].value()[0])
            nuke.delete(ct)

            # Loop over the classes and setup the encryptomatte node
            for i in range(classes):
                expr = nuke.createNode('Expression', inpanel= False)
                expr['channel3'].setValue('alpha')
                expr['expr3'].setValue(f'a == {i} ? 1 :0')
                expr.setInput(0, dd)
                encr = nuke.createNode('Encryptomatte', inpanel = False)
                encr.setInput(0,expr)
                if i > 0:
                    encr.setInput(0, prev_encr)
                encr.setInput(1,expr)

                # Need to set this manually as otherwise it doesn't work 
                encr['matteNameType'].setValue('manual')
                encr['matteName'].setValue(expr.name())
                encr['cryptoLayer'].setValue('CryptoLayer')
                prev_encr = encr
            nuke.createNode('Output', inpanel = False)

        # Ensure we aren't inside the gizmo again
        this_node.end()
        cryptomatte = nuke.createNode('Cryptomatte')