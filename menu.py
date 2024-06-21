#nuke.knobDefault('Read.colorspace', 'Utility - Raw')

import W_hotbox, W_hotboxManager



def toggleBW():
    selectedNode = None
    try:
        selectedNode = nuke.selectedNode()
    except:    
        nuke.message("select a RotoPaint node!")
        return
    if selectedNode.Class() == 'RotoPaint':
        if not selectedNode.knob('toolbar_paint_color').value(1):
            selectedNode.knob('toolbar_paint_color').setValue(1)
        else:
            selectedNode.knob('toolbar_paint_color').setValue(0)
    else:
        nuke.message("select a RotoPaint node!")
        return

viewer = nuke.menu('Viewer')
viewer.addCommand('RotoPaint/toggle b\/w', 'toggleBW()', 'shift+d')


try:
    import shortcuteditor
    shortcuteditor.nuke_setup()
except Exception:
    import traceback
    traceback.print_exc()

HeyGizmosMenu = nuke.menu('Nodes').addMenu('nukepedia')
HeyGizmosMenu.addCommand('ImagePlaneR', 'nuke.createNode("ImagePlaneR")')

HeyGizmosMenu.addCommand('L_Grain', 'nuke.createNode("L_Grain_v05")')
HeyGizmosMenu.addCommand('RoughenEdges', 'nuke.createNode("RoughenEdges.gizmo")')


