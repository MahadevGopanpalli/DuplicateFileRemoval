import sys
import os
import hashlib

def hashfile(path,blocksize=1024):
    afile=open(path,'rb')
    hasher=hashlib.md5()
    buf=afile.read(blocksize)
    while len(buf)>0:
        hasher.update(buf)
        buf=afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()


def main():
    flag=os.path.isabs(sys.argv[1])
    if flag==False:
        path=os.path.abspath(sys.argv[1])
    
    exits=os.path.isdir(path)
    
    if exits:
        print(path)

    data={}

    for F,SF,f in os.walk(path):
        for fil in f:
            path=os.path.join(F,fil)
            chk=hashfile(path)
            if chk in data:
                data[chk].append(path)
            else:
                data[chk]=[path]

    newdata = []
    print(data)
    newdata = list(filter(lambda x: len(x)>1,data.values()))
    print(newdata)
    count = 0
    line = "-"*40
    fobj = open("Log.txt",'w')
        
    fobj.write(line+"\n")
    fobj.write("Marvellous names of duplicate files\n") 
    fobj.write(line+"\n")
    for outer in newdata:
        icnt = 0
        for inner in outer:
            icnt+=1
            if icnt >= 2:
                count+=1
                #print("filename",inner)
                fobj.write(inner+"\n")
                inner=os.path.abspath(inner)
                os.remove(inner)
    print("Total Duplicate files ",count);
    fobj.close()


if __name__ == "__main__":
    main()