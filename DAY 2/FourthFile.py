data ={
    "name" : "junaid",
    "age" : 20,
    "course" : "python",
    "marks" : [23,89,34.3,53.6,78.78],
    "is_student" : True
}
data["name"]="ahmed"
data["collage"]="AIUB"
print(data)


student = {
    "name":"junaid",
    "age": 22,
    "score":{
        "phy":45,
        "chem":67,
        "maths":100
    }
}

print(student["score"]["phy"])
print(student["score"].keys())
print(len(student))
print(student.values())

pairs =list(student.items())
print(pairs[2])
# print(student.get("name2")) no error
# print(student["name2"]) 

print(student)
new_dic ={
    "city":"karachi",
    "country":"pakistan",
    "postCode":23627,
}

student.update(new_dic)
student.update({"createdAt":"newDate"})
student.update({"name":"aHMED"})
print(student)

sets = {1,2,3,4,4,"junaid","ahmed","junaid"} #store single value 
emptyset =set()#empty set

print(sets)#
print(type(emptyset))
emptyset.add("a")
emptyset.add("b")
emptyset.add("c")
emptyset.remove("a")
emptyset.clear()
print(emptyset)

set1 = {1,2,3}
set2 = {3,2,9}
print(set1.union(set2))
print(set1.intersection(set2))

wordMeanings ={
    "table":["a piece of furniture","list of facts & figures"],
    "cat":"a small animal"
}
print(wordMeanings)

subjectList={"python","java","C++","python","javaScript","java","python","java","C++","C"
              }
length =len(subjectList)
print(length)

subMarks ={}
mathMarks = float(input("enter marks of math: " ))
phyMarks = float(input("enter marks of phy: " ))
subMarks.update({"chem":float(input("enter marks of chem: " )),"maths":mathMarks,"phy":phyMarks})
subMarks["maths":float(input("enter marks of chem: "))]
subMarks["phy":float(input("enter marks of chem: "))]
print(subMarks)

values={9,9.0}
print(values)