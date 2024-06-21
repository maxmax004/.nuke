# Kaeden James

# V 1.1: Added option to stabilise as well as matchmove!

# Use this script and any highlighted Tracker4 nodes, will sprout a SplineWarp node with Pins using the tracks and reference frame from the Tracker node. Personally, I've coupled this script with Wouter Gilsing's fabulous W_hotbox, for ease of use. I've found it great for doing skin patches, or any patches really where a general CornerPin track doesn't quite cut it. Think of it as an ultra CornerPin track with up to 99 corners! It's expression-linked so changes to any existing tracks, or to the reference frame, will follow through.

# To use this script with W_hotbox, simply save the python script in a location nuke has access to, (for me: .nuke/pythons). When creating a new W_hotbox function, call trackerToPins() externally with:
# import KJ_Tracker_to_Pins
# KJ_Tracker_to_Pins.trackerToPins()

import nuke
import os
import nuke.splinewarp as sw

def trackerToPins():
    p = nuke.Panel('Tracker to Pins')
    p.addButton('Back')
    p.addButton('Matchmove')
    p.addButton('Stabilise')
    result = p.show()
    if(result == 2):
        trackerToPinsOp(True)
    elif(result == 1):
        trackerToPinsOp(False)
    else:
        return

def trackerToPinsOp(reverse):

    def getTrackNames(tracker4Node):
        k=tracker4Node['tracks']
        s=tracker4Node['tracks'].toScript().split(' \n} \n{ \n ')
        s.pop(0)
        ss=str(s)[2:].split('\\n')
        if ss: 
            ss.pop(-1)
        if ss: 
            ss.pop(-1)
        outList=[]
        for i in ss:
            outList.append(i.split('"')[1])
        return outList   

    def getNumberOfTracks(tracker4Node): 
        result = len(getTrackNames(tracker4Node))
        return result

    originalSelection = nuke.selectedNodes()
    for each in nuke.allNodes():
        each.knob("selected").setValue(False)

    for node in originalSelection:
        if node.Class() == "Tracker4":
            nodeTracker = node
            trackerTracks = nodeTracker['tracks']
            trackerColumns = 31
            trackerColumnName = 1
            trackerColumnX = 2
            trackerColumnY = 3

            selectAll = nodeTracker.knob("select_all")
            selectAll.execute()

            nodeSplineWarp = nuke.createNode("SplineWarp3", inpanel = False)
            nodeSplineWarp['xpos'].setValue(nodeTracker['xpos'].value()+100)
            nodeSplineWarp['ypos'].setValue(nodeTracker['ypos'].value())
        
            scriptIn = """AddMode 0 0 0 0 {{v x3f99999a}
  {f 0}
  {n
   {layer Root
    {f 2097152}
    {t x44f00000 x44870000}
    {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
    {layer Layer99
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin198 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3b6c95c0 x38a7c5ac}
     {0 0}}}
       {tx x435a0000 x3b6c95c0}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin197 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3b6c95c0 x38a7c5ac}
     {0 0}}}
       {tx x435a0000 x3b6c95c0}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer98
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin196 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3b675793 x39a2877f}
     {0 0}}}
       {tx x435a0000 x3b675793 x39a2877f}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin195 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3b675793 x39a2877f}
     {0 0}}}
       {tx x435a0000 x3b675793 x39a2877f}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer97
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin194 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3b5844d0 x39ad03da}
     {0 0}}}
       {tx x435a0000 x3b5844d0 x39ad03da}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin193 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3b5844d0 x39ad03da}
     {0 0}}}
       {tx x435a0000 x3b5844d0 x39ad03da}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer96
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin192 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3b564d7f x3a156c0d}
     {0 0}}}
       {tx x435a0000 x3b564d7f x3a156c0d}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin191 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3b564d7f x3a156c0d}
     {0 0}}}
       {tx x435a0000 x3b564d7f x3a156c0d}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer95
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin190 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3b47e282 x3a54562e}
     {0 0}}}
       {tx x435a0000 x3b47e282 x3a54562e}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin189 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3b47e282 x3a54562e}
     {0 0}}}
       {tx x435a0000 x3b47e282 x3a54562e}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer94
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin188 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3b319a41 x3a8461fa}
     {0 0}}}
       {tx x435a0000 x3b319a41 x3a8461fa}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin187 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3b319a41 x3a8461fa}
     {0 0}}}
       {tx x435a0000 x3b319a41 x3a8461fa}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer93
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin186 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3b1e98dd x3aa137f4}
     {0 0}}}
       {tx x435a0000 x3b1e98dd x3aa137f4}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin185 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3b1e98dd x3aa137f4}
     {0 0}}}
       {tx x435a0000 x3b1e98dd x3aa137f4}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer92
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin184 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3b0e368f x3a870111}
     {0 0}}}
       {tx x435a0000 x3b0e368f x3a870111}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin183 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3b0e368f x3a870111}
     {0 0}}}
       {tx x435a0000 x3b0e368f x3a870111}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer91
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin182 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3aefdc9c x3ac5eb31}
     {0 0}}}
       {tx x435a0000 x3aefdc9c x3ac5eb31}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin181 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3aefdc9c x3ac5eb31}
     {0 0}}}
       {tx x435a0000 x3aefdc9c x3ac5eb31}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer90
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin180 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x38a7c5ac x3ae1719f}
     {0 0}}}
       {tx x435a0000 0 x3ae1719f}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin179 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x38a7c5ac x3ae1719f}
     {0 0}}}
       {tx x435a0000 0 x3ae1719f}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer89
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin178 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3a59945b x3aea9e6f}
     {0 0}}}
       {tx x435a0000 x3a59945b x3aea9e6f}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin177 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3a59945b x3aea9e6f}
     {0 0}}}
       {tx x435a0000 x3a59945b x3aea9e6f}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer88
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin176 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3a0aefb3 x3aed3d86}
     {0 0}}}
       {tx x435a0000 x3a0aefb3 x3aed3d86}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin175 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3a0aefb3 x3aed3d86}
     {0 0}}}
       {tx x435a0000 x3a0aefb3 x3aed3d86}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer87
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin174 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3a8d8ec9 x3ae1719f}
     {0 0}}}
       {tx x435a0000 x3a8d8ec9 x3ae1719f}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin173 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3a8d8ec9 x3ae1719f}
     {0 0}}}
       {tx x435a0000 x3a8d8ec9 x3ae1719f}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer86
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin172 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3b41fc8f x39324207}
     {0 0}}}
       {tx x435a0000 x3b41fc8f x39324207}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin171 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3b41fc8f x39324207}
     {0 0}}}
       {tx x435a0000 x3b41fc8f x39324207}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer85
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin170 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3b3eb5b3 x3a180b24}
     {0 0}}}
       {tx x435a0000 x3b3eb5b3 x3a180b24}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin169 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3b3eb5b3 x3a180b24}
     {0 0}}}
       {tx x435a0000 x3b3eb5b3 x3a180b24}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer84
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin168 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3b525edd x38e6afcd}
     {0 0}}}
       {tx x435a0000 x3b525edd x38e6afcd}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin167 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3b525edd x38e6afcd}
     {0 0}}}
       {tx x435a0000 x3b525edd x38e6afcd}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer83
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin166 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3b3630a9 x3912ccf7}
     {0 0}}}
       {tx x435a0000 x3b3630a9 x3912ccf7}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin165 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3b3630a9 x3912ccf7}
     {0 0}}}
       {tx x435a0000 x3b3630a9 x3912ccf7}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer82
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin164 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3b1fe868 x3a2a64c3}
     {0 0}}}
       {tx x435a0000 x3b1fe868 x3a2a64c3}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin163 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3b1fe868 x3a2a64c3}
     {0 0}}}
       {tx x435a0000 x3b1fe868 x3a2a64c3}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer81
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin162 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3b488a48 x39c73abd}
     {0 0}}}
       {tx x435a0000 x3b488a48 x39c73abd}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin161 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3b488a48 x39c73abd}
     {0 0}}}
       {tx x435a0000 x3b488a48 x39c73abd}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer80
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin160 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3b319a41 x3a3f5d79}
     {0 0}}}
       {tx x435a0000 x3b319a41 x3a3f5d79}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin159 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3b319a41 x3a3f5d79}
     {0 0}}}
       {tx x435a0000 x3b319a41 x3a3f5d79}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer79
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin158 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3b1e98dd x3a870111}
     {0 0}}}
       {tx x435a0000 x3b1e98dd x3a870111}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin157 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3b1e98dd x3a870111}
     {0 0}}}
       {tx x435a0000 x3b1e98dd x3a870111}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer78
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin156 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3b07a8d6 x3aae5365}
     {0 0}}}
       {tx x435a0000 x3b07a8d6 x3aae5365}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin155 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3b07a8d6 x3aae5365}
     {0 0}}}
       {tx x435a0000 x3b07a8d6 x3aae5365}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer77
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin154 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3add82fd x3aa3d70a}
     {0 0}}}
       {tx x435a0000 x3add82fd x3aa3d70a}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin153 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3add82fd x3aa3d70a}
     {0 0}}}
       {tx x435a0000 x3add82fd x3aa3d70a}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer76
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin152 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3ab24207 x3ae02214}
     {0 0}}}
       {tx x435a0000 x3ab24207 x3ae02214}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin151 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3ab24207 x3ae02214}
     {0 0}}}
       {tx x435a0000 x3ab24207 x3ae02214}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer75
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin150 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3992ccf7 x3ae6afcd}
     {0 0}}}
       {tx x435a0000 x3992ccf7 x3ae6afcd}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin149 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3992ccf7 x3ae6afcd}
     {0 0}}}
       {tx x435a0000 x3992ccf7 x3ae6afcd}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer74
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin148 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3a12ccf7 x3ac9d9d3}
     {0 0}}}
       {tx x435a0000 x3a12ccf7 x3ac9d9d3}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin147 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3a12ccf7 x3ac9d9d3}
     {0 0}}}
       {tx x435a0000 x3a12ccf7 x3ac9d9d3}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer73
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin146 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x39473abd x3ac49ba6}
     {0 0}}}
       {tx x435a0000 x39473abd x3ac49ba6}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin145 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x39473abd x3ac49ba6}
     {0 0}}}
       {tx x435a0000 x39473abd x3ac49ba6}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer72
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin144 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3a96bb99 x3ab8cfc0}
     {0 0}}}
       {tx x435a0000 x3a96bb99 x3ab8cfc0}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin143 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3a96bb99 x3ab8cfc0}
     {0 0}}}
       {tx x435a0000 x3a96bb99 x3ab8cfc0}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer71
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin142 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3a6410b6 x3ad5a5b9}
     {0 0}}}
       {tx x435a0000 x3a6410b6 x3ad5a5b9}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin141 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3a6410b6 x3ad5a5b9}
     {0 0}}}
       {tx x435a0000 x3a6410b6 x3ad5a5b9}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer70
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin140 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3ac49ba6 x3ac1fc8f}
     {0 0}}}
       {tx x435a0000 x3ac49ba6 x3ac1fc8f}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin139 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3ac49ba6 x3ac1fc8f}
     {0 0}}}
       {tx x435a0000 x3ac49ba6 x3ac1fc8f}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer69
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin138 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3b2efb2b x39d6f545}
     {0 0}}}
       {tx x435a0000 x3b2efb2b x39d6f545}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin137 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3b2efb2b x39d6f545}
     {0 0}}}
       {tx x435a0000 x3b2efb2b x39d6f545}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer68
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin136 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3afe4799 x3a870111}
     {0 0}}}
       {tx x435a0000 x3afe4799 x3a870111}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin135 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3afe4799 x3a870111}
     {0 0}}}
       {tx x435a0000 x3afe4799 x3a870111}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer67
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin134 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3afa58f7 x3a49d9d3}
     {0 0}}}
       {tx x435a0000 x3afa58f7 x3a49d9d3}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin133 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3afa58f7 x3a49d9d3}
     {0 0}}}
       {tx x435a0000 x3afa58f7 x3a49d9d3}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer66
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin132 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3b0ede55 x3a449ba6}
     {0 0}}}
       {tx x435a0000 x3b0ede55 x3a449ba6}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin131 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3b0ede55 x3a449ba6}
     {0 0}}}
       {tx x435a0000 x3b0ede55 x3a449ba6}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer65
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin130 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3aabb44e x3a96bb99}
     {0 0}}}
       {tx x435a0000 x3aabb44e x3a96bb99}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin129 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3aabb44e x3a96bb99}
     {0 0}}}
       {tx x435a0000 x3aabb44e x3a96bb99}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer64
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin128 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3a5ed289 x3aa91538}
     {0 0}}}
       {tx x435a0000 x3a5ed289 x3aa91538}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin127 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3a5ed289 x3aa91538}
     {0 0}}}
       {tx x435a0000 x3a5ed289 x3aa91538}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer63
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin126 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3a1d4952 x3aa91538}
     {0 0}}}
       {tx x435a0000 x3a1d4952 x3aa91538}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin125 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3a1d4952 x3aa91538}
     {0 0}}}
       {tx x435a0000 x3a1d4952 x3aa91538}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer62
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin124 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3ac34c1b x3a8461fa}
     {0 0}}}
       {tx x435a0000 x3ac34c1b x3a8461fa}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin123 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3ac34c1b x3a8461fa}
     {0 0}}}
       {tx x435a0000 x3ac34c1b x3a8461fa}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer61
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin122 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3a51b717 x3a956c0d}
     {0 0}}}
       {tx x435a0000 x3a51b717 x3a956c0d}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin121 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3a51b717 x3a956c0d}
     {0 0}}}
       {tx x435a0000 x3a51b717 x3a956c0d}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer60
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin120 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3adae3e7 x3a4c78ea}
     {0 0}}}
       {tx x435a0000 x3adae3e7 x3a4c78ea}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin119 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3adae3e7 x3a4c78ea}
     {0 0}}}
       {tx x435a0000 x3adae3e7 x3a4c78ea}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer59
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin118 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3a59945b x3a3cbe62}
     {0 0}}}
       {tx x435a0000 x3a59945b x3a3cbe62}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin117 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3a59945b x3a3cbe62}
     {0 0}}}
       {tx x435a0000 x3a59945b x3a3cbe62}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer58
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin116 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x39e6afcd x3a83126f}
     {0 0}}}
       {tx x435a0000 x39e6afcd x3a83126f}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin115 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x39e6afcd x3a83126f}
     {0 0}}}
       {tx x435a0000 x39e6afcd x3a83126f}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer57
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin114 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x39d6f545 x3aa67621}
     {0 0}}}
       {tx x435a0000 x39d6f545 x3aa67621}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin113 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x39d6f545 x3aa67621}
     {0 0}}}
       {tx x435a0000 x39d6f545 x3aa67621}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer56
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin112 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x38fba882 x3aad03da}
     {0 0}}}
       {tx x435a0000 x38fba882 x3aad03da}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin111 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x38fba882 x3aad03da}
     {0 0}}}
       {tx x435a0000 x38fba882 x3aad03da}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer55
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin110 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3a8461fa x3a902de0}
     {0 0}}}
       {tx x435a0000 x3a8461fa x3a902de0}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin109 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3a8461fa x3a902de0}
     {0 0}}}
       {tx x435a0000 x3a8461fa x3a902de0}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer54
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin108 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3a9aaa3b x3a7ba882}
     {0 0}}}
       {tx x435a0000 x3a9aaa3b x3a7ba882}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin107 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3a9aaa3b x3a7ba882}
     {0 0}}}
       {tx x435a0000 x3a9aaa3b x3a7ba882}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer53
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin106 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3ac0ad04 x3a49d9d3}
     {0 0}}}
       {tx x435a0000 x3ac0ad04 x3a49d9d3}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin105 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3ac0ad04 x3a49d9d3}
     {0 0}}}
       {tx x435a0000 x3ac0ad04 x3a49d9d3}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer52
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin104 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3b252696 x393cbe62}
     {0 0}}}
       {tx x435a0000 x3b252696 x393cbe62}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin103 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3b252696 x393cbe62}
     {0 0}}}
       {tx x435a0000 x3b252696 x393cbe62}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer51
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin102 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3b17635e x39f66a55}
     {0 0}}}
       {tx x435a0000 x3b17635e x39f66a55}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin101 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3b17635e x39f66a55}
     {0 0}}}
       {tx x435a0000 x3b17635e x39f66a55}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer50
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin100 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3ae2c12b x3a22877f}
     {0 0}}}
       {tx x435a0000 x3ae2c12b x3a22877f}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin99 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3ae2c12b x3a22877f}
     {0 0}}}
       {tx x435a0000 x3ae2c12b x3a22877f}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer49
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin98 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3afcf80e x3a0aefb3}
     {0 0}}}
       {tx x435a0000 x3afcf80e x3a0aefb3}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin97 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3afcf80e x3a0aefb3}
     {0 0}}}
       {tx x435a0000 x3afcf80e x3a0aefb3}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer48
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin96 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3b180b24 x39324207}
     {0 0}}}
       {tx x435a0000 x3b180b24 x39324207}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin95 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3b180b24 x39324207}
     {0 0}}}
       {tx x435a0000 x3b180b24 x39324207}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer47
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin94 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3b070111 x39ad03da}
     {0 0}}}
       {tx x435a0000 x3b070111 x39ad03da}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin93 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3b070111 x39ad03da}
     {0 0}}}
       {tx x435a0000 x3b070111 x39ad03da}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer46
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin92 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3b06594b x38bcbe62}
     {0 0}}}
       {tx x435a0000 x3b06594b}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin91 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3b06594b x38bcbe62}
     {0 0}}}
       {tx x435a0000 x3b06594b}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer45
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin90 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3af27bb3 x39712c28}
     {0 0}}}
       {tx x435a0000 x3af27bb3 x39712c28}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin89 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3af27bb3 x39712c28}
     {0 0}}}
       {tx x435a0000 x3af27bb3 x39712c28}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer44
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin88 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3ae410b6 x38d1b717}
     {0 0}}}
       {tx x435a0000 x3ae410b6}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin87 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3ae410b6 x38d1b717}
     {0 0}}}
       {tx x435a0000 x3ae410b6}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer43
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin86 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3ae1719f x39d1b717}
     {0 0}}}
       {tx x435a0000 x3ae1719f x39d1b717}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin85 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3ae1719f x39d1b717}
     {0 0}}}
       {tx x435a0000 x3ae1719f x39d1b717}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer42
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin84 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3acf1801 x3966afcd}
     {0 0}}}
       {tx x435a0000 x3acf1801 x3966afcd}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin83 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3acf1801 x3966afcd}
     {0 0}}}
       {tx x435a0000 x3acf1801 x3966afcd}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer41
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin82 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3ac1fc8f x3a1d4952}
     {0 0}}}
       {tx x435a0000 x3ac1fc8f x3a1d4952}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin81 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3ac1fc8f x3a1d4952}
     {0 0}}}
       {tx x435a0000 x3ac1fc8f x3a1d4952}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer40
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin80 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3abf5d79 x39e6afcd}
     {0 0}}}
       {tx x435a0000 x3abf5d79 x39e6afcd}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin79 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3abf5d79 x39e6afcd}
     {0 0}}}
       {tx x435a0000 x3abf5d79 x39e6afcd}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer39
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin78 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3abb6ed6 x38a7c5ac}
     {0 0}}}
       {tx x435a0000 x3abb6ed6}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin77 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3abb6ed6 x38a7c5ac}
     {0 0}}}
       {tx x435a0000 x3abb6ed6}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer38
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin76 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3ab78034 x3992ccf7}
     {0 0}}}
       {tx x435a0000 x3ab78034 x3992ccf7}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin75 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3ab78034 x3992ccf7}
     {0 0}}}
       {tx x435a0000 x3ab78034 x3992ccf7}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer37
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin74 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3a4f1801 x3a807358}
     {0 0}}}
       {tx x435a0000 x3a4f1801 x3a807358}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin73 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3a4f1801 x3a807358}
     {0 0}}}
       {tx x435a0000 x3a4f1801 x3a807358}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer36
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin72 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3851b717 x3a92ccf7}
     {0 0}}}
       {tx x435a0000 0 x3a92ccf7}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin71 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3851b717 x3a92ccf7}
     {0 0}}}
       {tx x435a0000 0 x3a92ccf7}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer35
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin70 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3988509c x3a83126f}
     {0 0}}}
       {tx x435a0000 x3988509c x3a83126f}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin69 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3988509c x3a83126f}
     {0 0}}}
       {tx x435a0000 x3988509c x3a83126f}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer34
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin68 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3a89a027 x39ebedfa}
     {0 0}}}
       {tx x435a0000 x3a89a027 x39ebedfa}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin67 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3a89a027 x39ebedfa}
     {0 0}}}
       {tx x435a0000 x3a89a027 x39ebedfa}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer33
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin66 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3aa3d70a x39f66a55}
     {0 0}}}
       {tx x435a0000 x3aa3d70a x39f66a55}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin65 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3aa3d70a x39f66a55}
     {0 0}}}
       {tx x435a0000 x3aa3d70a x39f66a55}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer32
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin64 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3aa52696 x3a49d9d3}
     {0 0}}}
       {tx x435a0000 x3aa52696 x3a49d9d3}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin63 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3aa52696 x3a49d9d3}
     {0 0}}}
       {tx x435a0000 x3aa52696 x3a49d9d3}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer31
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin62 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3a180b24 x3a8d8ec9}
     {0 0}}}
       {tx x435a0000 x3a180b24 x3a8d8ec9}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin61 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3a180b24 x3a8d8ec9}
     {0 0}}}
       {tx x435a0000 x3a180b24 x3a8d8ec9}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer30
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin60 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3983126f x3a9d4952}
     {0 0}}}
       {tx x435a0000 x3983126f x3a9d4952}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin59 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3983126f x3a9d4952}
     {0 0}}}
       {tx x435a0000 x3983126f x3a9d4952}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer29
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin58 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3a79096c x3a66afcd}
     {0 0}}}
       {tx x435a0000 x3a79096c x3a66afcd}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin57 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3a79096c x3a66afcd}
     {0 0}}}
       {tx x435a0000 x3a79096c x3a66afcd}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer28
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin56 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3992ccf7 x3a1aaa3b}
     {0 0}}}
       {tx x435a0000 x3992ccf7 x3a1aaa3b}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin55 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3992ccf7 x3a1aaa3b}
     {0 0}}}
       {tx x435a0000 x3992ccf7 x3a1aaa3b}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer27
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin54 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3a449ba6 x39dc3372}
     {0 0}}}
       {tx x435a0000 x3a449ba6 x39dc3372}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin53 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3a449ba6 x39dc3372}
     {0 0}}}
       {tx x435a0000 x3a449ba6 x39dc3372}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer26
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin52 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3aa7c5ac x38a7c5ac}
     {0 0}}}
       {tx x435a0000 x3aa7c5ac}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin51 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3aa7c5ac x38a7c5ac}
     {0 0}}}
       {tx x435a0000 x3aa7c5ac}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer25
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin50 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3a9d4952 x398d8ec9}
     {0 0}}}
       {tx x435a0000 x3a9d4952 x398d8ec9}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin49 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3a9d4952 x398d8ec9}
     {0 0}}}
       {tx x435a0000 x3a9d4952 x398d8ec9}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer24
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin48 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3a85b185 x3a22877f}
     {0 0}}}
       {tx x435a0000 x3a85b185 x3a22877f}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin47 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3a85b185 x3a22877f}
     {0 0}}}
       {tx x435a0000 x3a85b185 x3a22877f}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer23
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin46 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3a870111 x38d1b717}
     {0 0}}}
       {tx x435a0000 x3a870111}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin45 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3a870111 x38d1b717}
     {0 0}}}
       {tx x435a0000 x3a870111}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer22
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin44 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3a712c28 x39b24207}
     {0 0}}}
       {tx x435a0000 x3a712c28 x39b24207}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin43 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3a712c28 x39b24207}
     {0 0}}}
       {tx x435a0000 x3a712c28 x39b24207}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer21
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin42 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3a27c5ac x3a54562e}
     {0 0}}}
       {tx x435a0000 x3a27c5ac x3a54562e}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin41 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3a27c5ac x3a54562e}
     {0 0}}}
       {tx x435a0000 x3a27c5ac x3a54562e}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer20
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin40 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3a3cbe62 x3a1fe868}
     {0 0}}}
       {tx x435a0000 x3a3cbe62 x3a1fe868}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin39 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3a3cbe62 x3a1fe868}
     {0 0}}}
       {tx x435a0000 x3a3cbe62 x3a1fe868}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer19
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin38 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3a0d8ec9 x39dc3372}
     {0 0}}}
       {tx x435a0000 x3a0d8ec9 x39dc3372}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin37 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3a0d8ec9 x39dc3372}
     {0 0}}}
       {tx x435a0000 x3a0d8ec9 x39dc3372}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer18
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin36 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x39bcbe62 x3a6410b6}
     {0 0}}}
       {tx x435a0000 x39bcbe62 x3a6410b6}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin35 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x39bcbe62 x3a6410b6}
     {0 0}}}
       {tx x435a0000 x39bcbe62 x3a6410b6}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer17
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin34 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x39dc3372 x3a27c5ac}
     {0 0}}}
       {tx x435a0000 x39dc3372 x3a27c5ac}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin33 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x39dc3372 x3a27c5ac}
     {0 0}}}
       {tx x435a0000 x39dc3372 x3a27c5ac}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer16
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin32 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x38bcbe62 x3a2d03da}
     {0 0}}}
       {tx x435a0000 0 x3a2d03da}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin31 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x38bcbe62 x3a2d03da}
     {0 0}}}
       {tx x435a0000 0 x3a2d03da}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer15
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin30 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x38d1b717 x3a6410b6}
     {0 0}}}
       {tx x435a0000 0 x3a6410b6}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin29 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x38d1b717 x3a6410b6}
     {0 0}}}
       {tx x435a0000 0 x3a6410b6}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer14
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin28 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3a4f1801 x3912ccf7}
     {0 0}}}
       {tx x435a0000 x3a4f1801 x3912ccf7}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin27 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3a4f1801 x3912ccf7}
     {0 0}}}
       {tx x435a0000 x3a4f1801 x3912ccf7}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer13
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin26 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3a102de0 x3988509c}
     {0 0}}}
       {tx x435a0000 x3a102de0 x3988509c}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin25 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3a102de0 x3988509c}
     {0 0}}}
       {tx x435a0000 x3a102de0 x3988509c}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer12
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin24 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3912ccf7 x39fba882}
     {0 0}}}
       {tx x435a0000 x3912ccf7 x39fba882}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin23 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3912ccf7 x39fba882}
     {0 0}}}
       {tx x435a0000 x3912ccf7 x39fba882}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer11
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin22 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x39980b24 x39c73abd}
     {0 0}}}
       {tx x435a0000 x39980b24 x39c73abd}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin21 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x39980b24 x39c73abd}
     {0 0}}}
       {tx x435a0000 x39980b24 x39c73abd}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer10
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer119
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin20 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3a08509c x38a7c5ac}
     {0 0}}}
       {tx x435a0000 x3a08509c}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer118
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin19 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3a08509c x38a7c5ac}
     {0 0}}}
       {tx x435a0000 x3a08509c}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer9
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer117
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin18 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x39cc78ea x39712c28}
     {0 0}}}
       {tx x435a0000 x39cc78ea x39712c28}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer116
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin17 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x39cc78ea x39712c28}
     {0 0}}}
       {tx x435a0000 x39cc78ea x39712c28}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer8
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer115
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin16 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x387ba882 x39b78034}
     {0 0}}}
       {tx x435a0000 0 x39b78034}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer114
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin15 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x387ba882 x39b78034}
     {0 0}}}
       {tx x435a0000 0 x39b78034}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer7
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer113
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin14 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x39c1fc8f x3892ccf7}
     {0 0}}}
       {tx x435a0000 x39c1fc8f}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer112
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin13 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x39c1fc8f x3892ccf7}
     {0 0}}}
       {tx x435a0000 x39c1fc8f}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer6
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer111
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin12 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3951b717 x398d8ec9}
     {0 0}}}
       {tx x435a0000 x3951b717 x398d8ec9}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer110
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin11 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3951b717 x398d8ec9}
     {0 0}}}
       {tx x435a0000 x3951b717 x398d8ec9}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer5
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer109
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin10 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x39712c28 x38e6afcd}
     {0 0}}}
       {tx x435a0000 x39712c28 x38e6afcd}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer108
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin9 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x39712c28 x38e6afcd}
     {0 0}}}
       {tx x435a0000 x39712c28 x38e6afcd}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer4
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer107
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin8 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x393cbe62 x37a7c5ac}
     {0 0}}}
       {tx x435a0000 x393cbe62}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer106
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin7 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x393cbe62 x37a7c5ac}
     {0 0}}}
       {tx x435a0000 x393cbe62}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer3
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer105
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin6 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x38a7c5ac x3912ccf7}
     {0 0}}}
       {tx x435a0000 0 x3912ccf7}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer104
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin5 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x38a7c5ac x3912ccf7}
     {0 0}}}
       {tx x435a0000 0 x3912ccf7}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer2
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer103
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin4 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x387ba882 x37a7c5ac}
     {0 0}}}
       {tx x435a0000 0}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer102
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin3 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x387ba882 x37a7c5ac}
     {0 0}}}
       {tx x435a0000 0}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}
    {layer Layer1
     {f 2097664}
     {t x44f00000 x44870000}
     {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
     {layer Layer101
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin2 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3ae410b6 x3a8461fa}
     {0 0}}}
       {tx x435a0000 x3ae410b6 x3a8461fa}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}
     {layer Layer100
      {f 2097664}
      {t x44f00000 x44870000}
      {a pt1x 0 pt1y 0 pt2x 0 pt2y 0 pt3x 0 pt3y 0 pt4x 0 pt4y 0 ptex00 0 ptex01 0 ptex02 0 ptex03 0 ptex10 0 ptex11 0 ptex12 0 ptex13 0 ptex20 0 ptex21 0 ptex22 0 ptex23 0 ptex30 0 ptex31 0 ptex32 0 ptex33 0 ptof1x 0 ptof1y 0 ptof2x 0 ptof2y 0 ptof3x 0 ptof3y 0 ptof4x 0 ptof4y 0 pterr 0 ptrefset 0 ptmot x40800000 ptref 0}
      {cubiccurve Pin1 262656 bezier
       {cc
        {f 8224}
        {px x435a0000
     {0 0}
     {x3ae410b6 x3a8461fa}
     {0 0}}}
       {tx x435a0000 x3ae410b6 x3a8461fa}
       {a ro 0 go 0 bo 0 ao 0 mbo 0 mb 1 mbs x3f000000 mbsot 0 mbso 0 fo 1 fx 0 fy 0 ff 1 ft 0 osw x41200000 osf 0 str 1 ltn x435a0000 ltm x435a0000 pt 0 ab 1}}}}}}
  {edge Layer99.Layer119.Pin198 Layer99.Layer118.Pin197
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer98.Layer119.Pin196 Layer98.Layer118.Pin195
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer97.Layer119.Pin194 Layer97.Layer118.Pin193
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer96.Layer119.Pin192 Layer96.Layer118.Pin191
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer95.Layer119.Pin190 Layer95.Layer118.Pin189
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer94.Layer119.Pin188 Layer94.Layer118.Pin187
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer93.Layer119.Pin186 Layer93.Layer118.Pin185
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer92.Layer119.Pin184 Layer92.Layer118.Pin183
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer91.Layer119.Pin182 Layer91.Layer118.Pin181
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer90.Layer119.Pin180 Layer90.Layer118.Pin179
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer89.Layer119.Pin178 Layer89.Layer118.Pin177
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer88.Layer119.Pin176 Layer88.Layer118.Pin175
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer87.Layer119.Pin174 Layer87.Layer118.Pin173
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer86.Layer119.Pin172 Layer86.Layer118.Pin171
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer85.Layer119.Pin170 Layer85.Layer118.Pin169
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer84.Layer119.Pin168 Layer84.Layer118.Pin167
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer83.Layer119.Pin166 Layer83.Layer118.Pin165
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer82.Layer119.Pin164 Layer82.Layer118.Pin163
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer81.Layer119.Pin162 Layer81.Layer118.Pin161
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer80.Layer119.Pin160 Layer80.Layer118.Pin159
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer79.Layer119.Pin158 Layer79.Layer118.Pin157
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer78.Layer119.Pin156 Layer78.Layer118.Pin155
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer77.Layer119.Pin154 Layer77.Layer118.Pin153
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer76.Layer119.Pin152 Layer76.Layer118.Pin151
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer75.Layer119.Pin150 Layer75.Layer118.Pin149
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer74.Layer119.Pin148 Layer74.Layer118.Pin147
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer73.Layer119.Pin146 Layer73.Layer118.Pin145
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer72.Layer119.Pin144 Layer72.Layer118.Pin143
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer71.Layer119.Pin142 Layer71.Layer118.Pin141
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer70.Layer119.Pin140 Layer70.Layer118.Pin139
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer69.Layer119.Pin138 Layer69.Layer118.Pin137
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer68.Layer119.Pin136 Layer68.Layer118.Pin135
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer67.Layer119.Pin134 Layer67.Layer118.Pin133
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer66.Layer119.Pin132 Layer66.Layer118.Pin131
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer65.Layer119.Pin130 Layer65.Layer118.Pin129
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer64.Layer119.Pin128 Layer64.Layer118.Pin127
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer63.Layer119.Pin126 Layer63.Layer118.Pin125
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer62.Layer119.Pin124 Layer62.Layer118.Pin123
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer61.Layer119.Pin122 Layer61.Layer118.Pin121
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer60.Layer119.Pin120 Layer60.Layer118.Pin119
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer59.Layer119.Pin118 Layer59.Layer118.Pin117
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer58.Layer119.Pin116 Layer58.Layer118.Pin115
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer57.Layer119.Pin114 Layer57.Layer118.Pin113
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer56.Layer119.Pin112 Layer56.Layer118.Pin111
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer55.Layer119.Pin110 Layer55.Layer118.Pin109
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer54.Layer119.Pin108 Layer54.Layer118.Pin107
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer53.Layer119.Pin106 Layer53.Layer118.Pin105
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer52.Layer119.Pin104 Layer52.Layer118.Pin103
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer51.Layer119.Pin102 Layer51.Layer118.Pin101
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer50.Layer119.Pin100 Layer50.Layer118.Pin99
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer49.Layer119.Pin98 Layer49.Layer118.Pin97
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer48.Layer119.Pin96 Layer48.Layer118.Pin95
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer47.Layer119.Pin94 Layer47.Layer118.Pin93
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer46.Layer119.Pin92 Layer46.Layer118.Pin91
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer45.Layer119.Pin90 Layer45.Layer118.Pin89
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer44.Layer119.Pin88 Layer44.Layer118.Pin87
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer43.Layer119.Pin86 Layer43.Layer118.Pin85
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer42.Layer119.Pin84 Layer42.Layer118.Pin83
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer41.Layer119.Pin82 Layer41.Layer118.Pin81
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer40.Layer119.Pin80 Layer40.Layer118.Pin79
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer39.Layer119.Pin78 Layer39.Layer118.Pin77
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer38.Layer119.Pin76 Layer38.Layer118.Pin75
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer37.Layer119.Pin74 Layer37.Layer118.Pin73
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer36.Layer119.Pin72 Layer36.Layer118.Pin71
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer35.Layer119.Pin70 Layer35.Layer118.Pin69
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer34.Layer119.Pin68 Layer34.Layer118.Pin67
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer33.Layer119.Pin66 Layer33.Layer118.Pin65
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer32.Layer119.Pin64 Layer32.Layer118.Pin63
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer31.Layer119.Pin62 Layer31.Layer118.Pin61
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer30.Layer119.Pin60 Layer30.Layer118.Pin59
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer29.Layer119.Pin58 Layer29.Layer118.Pin57
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer28.Layer119.Pin56 Layer28.Layer118.Pin55
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer27.Layer119.Pin54 Layer27.Layer118.Pin53
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer26.Layer119.Pin52 Layer26.Layer118.Pin51
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer25.Layer119.Pin50 Layer25.Layer118.Pin49
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer24.Layer119.Pin48 Layer24.Layer118.Pin47
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer23.Layer119.Pin46 Layer23.Layer118.Pin45
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer22.Layer119.Pin44 Layer22.Layer118.Pin43
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer21.Layer119.Pin42 Layer21.Layer118.Pin41
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer20.Layer119.Pin40 Layer20.Layer118.Pin39
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer19.Layer119.Pin38 Layer19.Layer118.Pin37
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer18.Layer119.Pin36 Layer18.Layer118.Pin35
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer17.Layer119.Pin34 Layer17.Layer118.Pin33
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer16.Layer119.Pin32 Layer16.Layer118.Pin31
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer15.Layer119.Pin30 Layer15.Layer118.Pin29
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer14.Layer119.Pin28 Layer14.Layer118.Pin27
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer13.Layer119.Pin26 Layer13.Layer118.Pin25
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer12.Layer119.Pin24 Layer12.Layer118.Pin23
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer11.Layer118.Pin22 Layer11.Layer119.Pin21
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer10.Layer119.Pin20 Layer10.Layer118.Pin19
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer9.Layer117.Pin18 Layer9.Layer116.Pin17
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer8.Layer115.Pin16 Layer8.Layer114.Pin15
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer7.Layer113.Pin14 Layer7.Layer112.Pin13
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer6.Layer111.Pin12 Layer6.Layer110.Pin11
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer5.Layer109.Pin10 Layer5.Layer108.Pin9
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer4.Layer107.Pin8 Layer4.Layer106.Pin7
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer3.Layer105.Pin6 Layer3.Layer104.Pin5
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer2.Layer103.Pin4 Layer2.Layer102.Pin3
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}
  {edge Layer1.Layer101.Pin2 Layer1.Layer100.Pin1
   {cp 0 0 0 0 0
    {{{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}
     {{{x435a0000 x3f000000}}
     {{x435a0000 x3f000000}}}}   cache
    {{xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}
     {xff7fffff x7f7fffff x7f7fffff}}}
   {a}}}
"""

            nodeSplineWarp['curves'].fromScript(scriptIn)
            splineWarpCurves = nodeSplineWarp['curves']
            splineWarpRoot = splineWarpCurves.rootLayer

            nodeSplineWarp['boundary_bbox'].setValue(False)
            nodeSplineWarp['crop_to_format'].setValue(False)

            numberOfTracks = getNumberOfTracks(nodeTracker)

            root = nuke.toNode("root")
        
            for i in range(0, numberOfTracks):

                refFrame = int(nodeTracker['reference_frame'].getValue())
                fromAnimTransform = splineWarpRoot[i][0].getTransform()
                toAnimTransform = splineWarpRoot[i][1].getTransform()
                splineWarpRoot[i].name = "TrackerPin_"+str(i+1)
                splineWarpRoot[i][0].name = "From"
                splineWarpRoot[i][1].name = "To"
                splineWarpRoot[i][0][0].name = "Pin"
                splineWarpRoot[i][1][0].name = "Pin"

                knobNameFromX = nodeSplineWarp.name() + ".curves." + splineWarpRoot[i].name + ".From.translate.x"
                knobNameFromY = nodeSplineWarp.name() + ".curves." + splineWarpRoot[i].name + ".From.translate.y"
                knobNameToX = nodeSplineWarp.name() + ".curves." + splineWarpRoot[i].name + ".To.translate.x"
                knobNameToY = nodeSplineWarp.name() + ".curves." + splineWarpRoot[i].name + ".To.translate.y"

                refValueX = trackerTracks.getValueAt(refFrame, trackerColumns*i + trackerColumnX)
                refValueY = trackerTracks.getValueAt(refFrame, trackerColumns*i + trackerColumnY)

                refCurveX = nuke.curvelib.AnimCurve.__new__(nuke.curvelib.AnimCurve)
                refCurveY = nuke.curvelib.AnimCurve.__new__(nuke.curvelib.AnimCurve)
                refCurveX.removeAllKeys()
                refCurveY.removeAllKeys()

                refCurveX.useExpression = True
                refCurveX.expressionString = nodeTracker.name() + ".tracks." + str(i+1) + ".track_x" + "(" + nodeTracker.name() + ".reference_frame)"
                refCurveY.useExpression = True
                refCurveY.expressionString = nodeTracker.name() + ".tracks." + str(i+1) + ".track_y" + "(" + nodeTracker.name() + ".reference_frame)"

                warpCurveX = nuke.curvelib.AnimCurve.__new__(nuke.curvelib.AnimCurve)
                warpCurveY = nuke.curvelib.AnimCurve.__new__(nuke.curvelib.AnimCurve)
                warpCurveX.removeAllKeys()
                warpCurveY.removeAllKeys()

                warpCurveX.useExpression = True
                warpCurveX.expressionString = nodeTracker.name() + ".tracks." + str(i+1) + ".track_x"
                warpCurveY.useExpression = True
                warpCurveY.expressionString = nodeTracker.name() + ".tracks." + str(i+1) + ".track_y"

                if (reverse == False):
                    splineWarpRoot[i][0].getTransform().setTranslationAnimCurve(0, refCurveX, 'main')
                    splineWarpRoot[i][0].getTransform().setTranslationAnimCurve(1, refCurveY, 'main')
                    splineWarpRoot[i][1].getTransform().setTranslationAnimCurve(0, warpCurveX, 'main')
                    splineWarpRoot[i][1].getTransform().setTranslationAnimCurve(1, warpCurveY, 'main')
                else:
                    splineWarpRoot[i][0].getTransform().setTranslationAnimCurve(0, warpCurveX, 'main')
                    splineWarpRoot[i][0].getTransform().setTranslationAnimCurve(1, warpCurveY, 'main')
                    splineWarpRoot[i][1].getTransform().setTranslationAnimCurve(0, refCurveX, 'main')
                    splineWarpRoot[i][1].getTransform().setTranslationAnimCurve(1, refCurveY, 'main')
                
                splineWarpCurves.changed()

            toDelete = list()
            for idx, layer in enumerate(splineWarpRoot):
                if "TrackerPin" not in layer.name:
                    toDelete.append(idx)
            toDelete.sort(reverse=True)
            for idx in toDelete:
                splineWarpRoot.remove(idx)
        for n in nuke.selectedNodes():
            n['selected'].setValue(False)

trackerToPins()