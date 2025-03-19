f=open("file.txt","rt")
print(f.read())


f=open("file.txt","a")
f.write("added text")
f.close()

f=open("file.txt",'r')
print(f.read())
