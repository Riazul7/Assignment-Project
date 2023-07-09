import json
student_records = dict()
def add_student(name,age,grade):
    student_records[name]=age,grade
add_student("Riazul",26,"Excellent")
add_student("Rohan",18,"A+")
add_student("Masud",6,"A+")
print(student_records)
def remove_student(name):
    del student_records[name]
remove_student("Masud")
print(student_records)
def search_student(name):
    if name in student_records:
        age, grade = student_records[name]
        return name,age,grade
    else:
        print("Name is not in dictionary")
print(search_student("Riazul"))
def update_grade(name,grade1):
    name,age,grade=search_student(name)
    student_records.update({name:(age, grade1)})
update_grade("Riazul","A+")
print(student_records)
x=json.dumps(student_records)
print(x)
with open("student_data.json", "w") as encode:
    encode.write(x)
with open('student_data.json', 'r') as openfile:
    data = json.load(openfile)
print(data)