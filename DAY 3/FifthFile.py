count = 5
while (count>0):
    print("junaid",count)
    count-=1
    
count =1 
while count<=100:
    print(count)
    count+=1

count = 100
while count>=0:
    print(count)
    count-=1

number = 2
count = 1

while count<=10:
    print(number," X ",count," = ", number*count)
    count+=1

numbers=[1,4,9,16,25,36,49,64,81,100]
count =0
while count<len(numbers):
    print(numbers[count], count)
    count+=1



numbers= (1,4,9,16,25,36,49,64,81,100)
x=int(input("enter the number to search : " ))
is_found = False
count = 0

while is_found == False:
    if (numbers[count]==x):
        print("found your number : ",numbers[count], "at the iteration : ", count)
        is_found=True
    count+=1

if(is_found==False):
    print("the number (",x,") is not found")


i = 0
while i<=10:
    if(i==4):
        print(i)
        break
    else:
        print(":)")
    i+=1

i = 0
while i<=10:
    if(i==4):
        i+=1
        continue
    print(i)
    i+=1

nums =[1,2,3,4,5]
for num in nums:
    print(num)

numbers=[1,4,9,16,25,9,36,49,64,81,100]
x=9
index =0
for n in numbers:
    if(n==x):
        print("found x on index : ",index)
        # break
    index+=1
n=2
for i in range(1,10+1):
    print(n," x ",i," = ",n*i)

for i in range(100,0,-1):
    print(i)

n =5
sum=0
while n>=0:
    sum =sum+n
    n-=1
print(sum)
factorial =1
for i in range(5,0,-1):
    factorial=factorial*i
print(factorial)

