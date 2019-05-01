
try:
    import clr
    clr.AddReference("Interop.SolidEdge")
    clr.AddReference("System.Runtime.InteropServices")
    import System.Runtime.InteropServices as SRI
    
except Exception as e:
    print "Solidedge not installed or DLL not found"
    print e
    
objApp = None
objDoc  = None

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
  checkForSE()
  
  if objApp != None:
    objDoc = objApp.ActiveDocument
    print "ActiveDocument Name:", objDoc.Name
    
    
#More to share if I get requests ...

    
