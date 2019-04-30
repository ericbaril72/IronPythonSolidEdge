import clr
try:
    import clr
    clr.AddReference("Interop.SolidEdge")
    clr.AddReference("System.Runtime.InteropServices")
    solidEnvinstalled=True
except:
    print "Solidedge not installed"

objApp = None
objDocs = None
objDoc  = None

if solidEnvinstalled:
    import SolidEdgeDraft as SEDraft
    import SolidEdgeFramework as SEFramework
    import SolidEdgeFrameworkSupport as SEFrameworkSupport
    import SolidEdgeConstants as SEConstants
    import SolidEdgeAssembly as SEAssembly

    import System.Runtime.InteropServices as SRI
    try:
        import SolidEdgeFramework.ISEApplicationEvents_Event as SEEvents
    except:
        print "no evensts handling"

def checkForSE():
    global objApp
    try:
        objApp = SRI.Marshal.GetActiveObject("SolidEdge.Application")
        return "OK"
    except:
        print "Start Solidedge first"
        return "NO"
        exit()

if __name__ == "__main__":
  global objApp
  checkForSE()
  
  if objApp != None:
    objDoc = objApp.ActiveDocument
    print "ActiveDocument Name:", objDoc.Name
    
    
#More to share if I get requests ...

    
