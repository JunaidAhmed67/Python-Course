# def sumOfTwo(x=1,y=2):
#     sum=x+y
#     return sum

print(sumOfTwo())
def avg(x,y,z):
    avg=(x+y+z)/3
    return avg

print(avg(2,2,2))
def LengthOfList(list):
    return(len(list))

list1=[2,3,4,5,7]
length=LengthOfList(list1)
print(length)

def printListE(list):
    for e in list:
        print(e, end=" ")

list1=[2,3,4,5,7]
# printListE(list1)

# def factorialOfN(n):
#     fact=1
#     for i in range(1,n+1):
#         fact = fact*i
#     return(fact)

# u =factorialOfN(5)
# print(u)

# def currencyConvo(curr):
#     usd = 180
#     return(curr*usd)

# print(currencyConvo(2))


# def checkNum(num):
#     if(num%2==0):
#         print("Even")
#     else:
#         print("Odd")

# checkNum(1)

# def show(n):
#     if(n==0):
#         return
#     print(n)
#     n-=1
#     show(n)

# show(5)

# def factorial(n,s=1):
#     if (n==0):
#         print(s)
#         return
#     s =s*n
#     factorial(n-1,s)
        

# factorial(5)

# def sumofNum(n):
#     if(n==0):
#         return 0
#     return sumofNum(n-1) + n

# print(sumofNum(2))


def printEle(list,i=0):
    if(i==len(list)):
        return
    print(list[i])
    i+=1
    printEle(list,i)

list1 =["a","b","c"]
printEle(list1)