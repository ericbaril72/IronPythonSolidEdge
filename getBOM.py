import Basic as SE

def initPartInfo():
    partInfo = {}
    partInfo["Rev"]="-"
    partInfo["Name"]="-"
    partInfo["Desc"]="-"
    return partInfo
    
def showBOM(Document, level=0,partlist=""):
    # recursive function ... calls itself if current part is sub-assembly
    objParts = Document.Parts

    print "Name:",Document.Name
    print "Has ",objParts.Count," parts..."
    bomList={}

    for i in range (1, objParts.Count+1):
        print level,objParts[i].Name
        element         =     objParts[i].Name.split(":")[0]
        elementQty      = int(objParts[i].Name.split(":")[1])


        if element in bomList.keys():
            bomListQty = bomList[element]["Qty"]
            bomListQty += 1
        else:
            bomListQty = 1

        if objParts[i].Subassembly:
            #print "is a sub-asm:"
            try:
                partInfo = objParts[i].PartDocument.Properties["ProjectInformation"]["Project Name"].Value
            except:
                print "Got error GettingASSFileProperties"
                partInfo = initPartInfo()
            elementBom          = showBOM( objParts[i].PartDocument, level+1)
            bomList[element]    = {"Bom":elementBom, "partInfo": partInfo, "Path": objParts[i].PartDocument.Path,"Qty":bomListQty}
        else:
            try:
                partInfo = getPartFileProperties(objParts[i].PartDocument)

                bomList[element] = {"partInfo":partInfo,"Path": objParts[i].PartDocument.Path,"Qty":bomListQty}

            except:
                print "Got error getting Part file properties",i
                print "-------"
                bomList[element] = {"partInfo":initPartInfo(),"Path": "Unknown","Qty":bomListQty}

    #print "This ASM: ",Document.Name
    #for item in bomList:
    #    print "\t",item,bomList[item]["Qty"]
    return bomList


if __name__ =="__main__":
  SE.checkForSE()
  objApp = SE.objApp
  objDoc=objApp.ActiveDocument
  
  BOM = showBOM(objDoc)
  # BOM is Dictionary
