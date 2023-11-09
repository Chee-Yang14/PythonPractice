#using dict
students = {"Hermione": "Gryffindor", 
            "Harry": "Gryffindor",
            "ron": "Gryffindor",
            "Draco": "Slytherin"}

for student in students:
    print(student, students[student], sep=", House: ")
    
    
print("\n")


#using dic with more keys
moreStudents = [
    {"name": "Hermione", "house": "Gryffindor", "patronus":"otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus":"stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus":"Jack Russell Terrier"},
    {"name": "Draco", "house": "Gryffindor", "patronus":None}
]

for student in moreStudents:
    print(student["name"], student["house"],student["patronus"])