import sys
import json

mnomicCodeTable={}
symbolTable={}
def readMnoCodeTable():
    rawStr=""
    with open("config.json","r") as fp:
        l=fp.readline()
        while(l!=""):
            rawStr += l
            l=fp.readline()
    
    global mnomicCodeTable
    mnomicCodeTable=dict(json.loads(s=rawStr))

def main():
    data=[]
    readMnoCodeTable()
    with open(sys.argv[1],"r") as fp:
        l=fp.readline()
        while(l!=""):
            data.append(str(l).split())
            l=fp.readline()
    global mnomicCodeTableclear
    for i in data:
        if i[0] not in list(mnomicCodeTable.keys()) and i[0][0]!='+':
            symbolTable.update({str(i[0]):0})
            i=i[1:]
        print("i[0]:",i[0])

    print(symbolTable)
if __name__ == "__main__":
    main()