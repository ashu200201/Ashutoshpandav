"""
file handling modes
r:read
w:write
a:append
x:create blank file
"""
"""
#read text file
#f = open("C:\\Users\\admin\\Desktop\\project\\myfile.txt","r")
f = open("myfile.txt","r")
print(f.read())


#write text file
f=open("myfile_write.txt","w")

name=input("Enter anything : ")
f.write(name)
f.close()
"""
#append text file
f=open("myfile_write.txt","a")

name=input("Enter anything : ")
f.write("\n"+name)
f.close()
"""
#empty file 
f=open("blankfile.txt","x")
f.close()
"""