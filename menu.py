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

HeyGizmosMenu.addCommand('PointCloudKeyer', 'nuke.createNode("PointCloudKeyer")')

HeyGizmosMenu.addCommand('L_Grain', 'nuke.createNode("L_Grain_v05")')
HeyGizmosMenu.addCommand('RoughenEdges', 'nuke.createNode("RoughenEdges.gizmo")')


'''

m = menubar.addMenu("&Viewer")
n = m.addMenu("Connect to A Side")
n.addCommand("Using Input &1", "nuke.connectViewer(0, nuke.selectedNode())", "ctrl+1")
n.addCommand("Using Input &2", "nuke.connectViewer(1, nuke.selectedNode())", "ctrl+2")
n.addCommand("Using Input &3", "nuke.connectViewer(2, nuke.selectedNode())", "ctrl+3")'''




menubar=nuke.menu("Nodes")

m=menubar.addMenu("gizmos", "gizmos.png")

m.addCommand("Mask", "mer = nuke.createNode(\"Merge2\");mer[\'bbox\'].setValue(\'A\');mer[\'operation\'].setValue(\'mask\')")

m.addCommand("Stencil", "mer = nuke.createNode(\"Merge2\");mer[\'bbox\'].setValue(\'B\');mer[\'operation\'].setValue(\'stencil\')")


import nuke
toolbar = nuke.menu("Nodes")
toolbar.addCommand('Cattery/Segmentation/ViTMatte', 'nuke.createNode("vitmatte")', icon="vitmatte.png")
toolbar.addCommand('Cattery/Depth Estimation/DepthAnythingV2', 'nuke.createNode("DepthAnythingV2")', icon="DepthAnythingV2.png")



