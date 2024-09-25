nuke.pluginAddPath("./NukeSurvivalToolkit")
nuke.pluginAddPath("./Gizmos")

import autosave

# nuke.ViewerProcess.register("GRN_515_LUT", nuke.Node, ("GRN_515", ""))
# nuke.ViewerProcess.register("TVSS_lut", nuke.Node, ("TVSS_lut", ""))

#nuke.ViewerProcess.register("_______", nuke.Node, ("_______", ""))

# Project Settings > Default format
nuke.knobDefault("Root.format", "UHD_4K")

# Project Settings > Default frame rate
nuke.knobDefault("Root.fps", "23.976")

#nuke.pluginAddPath("./Aitor_Echeveste")

nuke.pluginAddPath('pixelfudger3')
# >>>PrismStart
import sys
import nuke

#def filenameFix(filename):
#    if sys.platform in ("Windows", "Microsoft"):
#        return filename.replace( "/run/media/carlos/WorkLinux/Dropbox/", "D:/Dropbox/" )
#   return filename.replace( "D:/Dropbox/", "/run/media/carlos/WorkLinux/Dropbox/")

import nuke
nuke.pluginAddPath('./Cattery/vitmatte')
nuke.pluginAddPath('./Cattery/DepthAnythingV2')