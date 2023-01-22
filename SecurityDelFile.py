import os
dirs=[]
notper=0
notfile=0
oser=0
while True:
    t=input("filePath:")
    if t=='':
        break
    dirs.append(t)
for i in dirs:
    try:
        print("\nFile:{}".format(i))
        size=os.stat(i).st_size
        print(" Size {}".format(size))
        fd=os.open(i,os.O_WRONLY)
        os.write(fd,b'\000'*size)
        os.close(fd)
        os.remove(i)
    except FileNotFoundError:
        print(" The File NOT Found")
        notfile=notfile+1
    except PermissionError:
        print(" The Program Not has this File Write Permission")
        notper=notper+1
    except [WindowsError,OSError,EnvironmentError,IOError] as e:
        print(" WANING:OS I/O ERROR")
        oser=oser+1
    else:
        print(" OK")
print("\nTotal:{}\nSuccess:{}\nFail:{}\n Not Found File:{}\n Not Permission:{}\n OS I/O ERROR:{}\n".format(
    len(dirs),(len(dirs)-notfile-notper-oser),(notfile+notper+oser),
    notfile,notper,oser
))
os.system("pause")