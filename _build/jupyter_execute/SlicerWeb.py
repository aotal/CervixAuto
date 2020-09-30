<h1><center>Click here to open 3D Slicer in a new window</center></h1></a>

# Run this cell (Shift+Enter) to show application here
import JupyterNotebooksLib as slicernb
slicernb.AppWindow(contents='full')

# Run this cell to load a file from a URL.
# You can load your own data by changing inputs of downloadFromURL.
# Any questions? Write us on the Slicer forum: https://discourse.slicer.org
slicer.mrmlScene.Clear()

volume = slicernb.downloadFromURL(
    uris="https://github.com/Slicer/SlicerTestingData/releases/download/MD5/39b01631b7b38232a220007230624c8e",
    fileNames="MRHead.nrrd",
    nodeNames="Volume")[0]

slicernb.showVolumeRendering(volume)

