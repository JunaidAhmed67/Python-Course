str = "string 1 \n second str"
a = "junaid  junaid tehhnwhmd gyewj ygejgw eud"
b= " Ahmed"
print(a[1]+b[1])
print(a[:3]) #0 se start
print(a[1:]) #end of string tak

print(a.endswith("eud"))
print(a.capitalize())
print(a.replace("junaid","osj"))
print(a.find("teh"))
print(a.count("j"))
name = input("Enter your name : ")
print(name.count("$"))
age = int(input("Please enter your age: "))
if (age>88 and age<99):
    print("You can apply for driving license.")
elif(age>=18):
    print("Alo can apply.")
else:
    print("You can not apply for driving lisence.")

number1 = int(input("Enter number1 : "))
number2 = int(input("Enter number2 : "))
number3 = int(input("Enter number3 : "))

if (number2>number1 and number2>number3):
    print("number 2 is greatest: ", number2)
elif (number3>number1 and number3>number2 ):
    print("number 3 is greatest: ", number3)
else:
    print("number 1 is greatest: ", number1)

if(number1%7==0):
    print("number is dividible by 7")
else:
    print("number is not dividible by 7")