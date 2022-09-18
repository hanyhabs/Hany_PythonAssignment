#Build a simple school which allows for :: 
# 3.1 Adding a new student to a class with a Name & (unique) ID 
# 3.2 Showing total number of students in a class 
# 3.3 Removing the name of a student from a class 
# 3.4 Promoting a student to the next grade


student = input('Enter the name')
function= ' '
Student = {
        1:'Han',2:'Adh'
    }
while(function != '0'):
    function = input('Enter the required operation: \n 1 Adding a new student \n 2 Showing total number of students in a class \n 3 Removing the name of a student from a class \n 4 Promoting a student to the next grade \n Press 0 to EXIT')

    

    def add_student(s):
        Student[len(Student)+1] = s
        print('Student added successfully')
        print(Student)

    def total_students(s):
        print(len(Student))

    def remove_student():
        print(Student)
        st = input('Student to be removed')
        for k,v in dict(Student).items():
            if v == st:
                print('U')
                del Student[k]

    def promotion(s):
        sect = int(input('Enter the grade 1,2..'))
        sect = str(sect+1)
        print(s+ 'promoted to' +sect)

    if function == '1':
        add_student(student)
    elif function == '2':
        total_students(student)
    elif function == '3':
        remove_student()
    elif function == '4':
        promotion(student)
    else:
        print('Wrong input')

