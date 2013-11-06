#test class

def generateFile(code):
    fo = open("testFile.txt","w")
    
    for i in range(1,10):
        fo.write(str(i)+"\n")
    fo.close