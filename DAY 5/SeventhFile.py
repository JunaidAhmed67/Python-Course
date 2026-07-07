# File I/O

f = open("demo.txt","r") 
data = f.read(5) #only read 5 characters from start abcde 
line1 = f.readline() #only read single line from a file  
line1 = f.readlines()[1] # read multiple lines by default 1 from a file  
data = f.read()
print(line1)
f.close


f= open("demo.txt","w") # for rewriting the existing file , if file does not exist can also create that file

f= open("demo.txt","a") # for adding data in existing dta in  the existing file , if file does not exist can also create that file

f.write("\nyessssssssssssssssssss")
f.close()


f = open("demo.txt", "r+") # read + write (read old data in file write new but written at the end)
data = f.read() 

f.write("ddd")
f.close()

f = open("demo.txt", "w+") #empty the file before write or read
data = f.read() 
print(data)
f.write("sss")
data = f.read() 
print(data)
f.close()


f = open("demo.txt", "a+") #empty the file before write or read
data = f.read() 
print(data)
f.write("222222")
data = f.read() 
print(data)
f.close()

with open("demo.txt","r") as f:
    data = f.read()
    print(data)

with open("demo.txt","w") as f:
    f.write("new data")

import os 
os.remove("sample.txt")  #to remove a file 

with open("practice.txt","w") as f:
    f.write("Hi everyone\nWe are Learning\nfile I/O\nusing java\ni like programming in java.")

with open("practice.txt","r+") as f:
    data = f.read()
    newData = data.replace("Java","python")

with open("practice.txt","w") as f:
    f.write(newData)


with open("practice.txt","r") as f:
    data = f.read()
    if (data.find("Learning")>=0):
        print("yes it exist.")
    else:
        print("It does not exist!")

found = False
lineNo= None
with open("practice.txt","r") as f:
    data = f.readlines()

for l in range(len(data)):
    if (data[l].find("Learning")>=0):
      found = True
      lineNo = l+1
      break

if(found):
   print("yes it exists at line no : ",lineNo)
else:
    print("It does not exist!")
   
def findLineNo(): 
   found = True
   word = "Learning"
   with open("practice.txt","r") as f:
      data = f.readline()
      linenum =1
      while found:
         if(word in data):
            print(linenum)
            return
         linenum = linenum +1
   return -1

print(findLineNo())
count =0
with open("practice.txt","r") as f:
    data = f.read()
    nums = data.rsplit(",")
    for num in nums:
        if(int(num)%2==0):
            print(num)
            count+=1
print("Even : ",count)



with open("practice.txt","r") as f:
    data = f.read()
count = 0
num =""
for i in range(len(data)):
    if (data[i] == ","):
        print(num)
        num =""
    else:
        num+=data[i]





