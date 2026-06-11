#Input for the number of students
NumberOfStudents = int(input("Enter the number of students: "))

#Declare array to store names and marks of students
names = []
marks = []

#Get the names and marks of each student using a loop
for i in range(NumberOfStudents):
    name = input(f"\n🎓 Enter the name of the student: ")
    names.append(name)
    
    mark = int(input(f"💡 Enter the mark for {name}: "))
    marks.append(mark)
    
#Get the total marks of all students, calculate the average and display it
TotalMarks = 0
AverageMark = 0.0

for i in range(NumberOfStudents):
    TotalMarks = TotalMarks + marks[i]
    
AverageMark = TotalMarks / NumberOfStudents

print(f"\n📋 RESULTS")
print(f"\n 🔀 Average Mark: {AverageMark}")

#Calculate the highest mark of all the students using a for loop and an if statement, and display it
HighestMark = marks[0]
HighestName = names[0]

for i in range(NumberOfStudents):
    
    if marks[i] > HighestMark:
        HighestMark = marks[i]
        HighestName = names [i]
        
print(f"\n ⬆️ Highsest Mark: {HighestName} - {HighestMark}")

#Calculate the lowest mark of all the students using a for loop and an if statement, and display it
LowestMark = marks[0]
LowestName = names[0]

for i in range(NumberOfStudents):
    
    if marks[i] < LowestMark:
        LowestMark = marks[i]
        LowestName = names[i]
        
print(f"\n ⬇️ Lowest Mark: {LowestName} - {LowestMark}")

#Calculate the students who passed and display a list of their names and marks
print(f"\n ✅ List of students who PASSED: \n")

for i in range(NumberOfStudents):
    
    if marks[i] >= 50:
        print(f"\t {names[i]} \t {marks[i]}")

#Calculate the students who passed and display a list of their names and marks
print(f"\n ❌ List of students who FAILED: \n")

for i in range(NumberOfStudents):
    
    if marks[i] < 50:
        print(f"\t {names[i]} \t {marks[i]}")
        