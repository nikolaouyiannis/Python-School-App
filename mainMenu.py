from datetime import date
from sys import exit

from moduleCourses import addCourses, dummyCourses
from moduleTrainersOrStudents import addTrainers, addStudents, dummyTrainers, dummyStudents, Students
from moduleAssignments import addAssignments, dummyAssignments
from moduleExtras import collection, forPerCourse, assignmentMarksInfo

def menu():
    print("\n", "menu".upper().center(100,'-'), "\n")
    print("[1] Enter information for each language course.")
    print("[2] Enter information for trainers.")
    print("[3] Enter information for students.")
    print("[4] Enter information for assignments.")
    print("[5] Enter information for students' personal assignments.")
    print("[6] View a collection of all language courses.")
    print("[7] View a collection of all trainers.")
    print("[8] View a collection of all students.")
    print("[9] View a collection of all assignments.")
    print("[10] View all students per course.")
    print("[11] View all trainers per course.")
    print("[12] View all assignments per course.")
    print("[13] View all assignments per student per course.")
    print("[14] View a list of students that belong to more than one courses.")
    print("[15] Use dummy data.")
    print("[0] Exit.")



print("\n"," welcome to our school! ".upper().center(100,'*'))
menu()


option_6_available = False
option_7_available = False
option_8_available = False
option_9_available = False
option_10_available = False
option_11_available = False
option_12_available = False
option_13_available = False
option_14_available = False
option_15_available = False
#prevent the user from using options 6 to 15 without entering information first



while True:
    try:
        option = int(input("\n>Enter your menu option [0-15]: "))
        if option == 1:
            coursesInfo = addCourses()
            #asks user to input info, returns a list containing Courses' class objects
            option_6_available = True
            menu()

        elif option == 2:
            trainersInfo = addTrainers()
            #asks user to input info, returns a list containing Trainers' class objects
            option_7_available = True
            option_11_available = True
            menu()

        elif option == 3:
            studentsInfo = addStudents()
            #asks user to input info, returns a list containing Students' class objects
            option_8_available = True
            option_10_available = True
            option_14_available = True
            menu()

        elif option == 4:
            assignmentsInfo = addAssignments()
            #asks user to input info, returns a list containing Assignments' class objects
            option_9_available = True
            option_12_available = True
            menu()

        elif option == 5:
            if option_8_available and option_9_available:
                option_10_11_12 = False
                #when True, forPerCourse() prints dict's key:value pairs but [option 5] doesn't print
                stdsPerCourse = forPerCourse(studentsInfo, option_10_11_12)
                #returns a dict with language:[student_1 name, student_2 name, etc. ] pairs
                assPerCourse = forPerCourse(assignmentsInfo, option_10_11_12)
                #returns a dict with language:[assignment_1 title, assignment_2 name, etc. ] pairs
                assignmentMarks = assignmentMarksInfo(stdsPerCourse, assPerCourse)
                #returns a dict language:{nested dict} pairs
                option_13_available = True
            else:
                print("\nIn order to enter information for students' personal assignments, first you have to insert information about the students (option 3) AND the assignments (option 4) or use dummy data (option 15).")

        elif option == 6:
            if option_6_available:
                collection("Language courses", coursesInfo)
                #prints list's user values
                continue
            elif option_15_available:
                collection("Language courses", dummyCoursesInfo)
                #prints list's dummy values
            else:
                print("\nIn order to view courses you have to insert information first (option 1) or use dummy data (option 15).")
            
        elif option == 7:
            #same functionality as [option 6]
            if option_7_available:
                collection("Trainers", trainersInfo)
                continue                
            elif option_15_available:               
                collection("Trainers", dummyTrainersInfo)                
            else:
                print("\nIn order to view trainers you have to insert information first (option 2) or use dumy data (option 15).")

        elif option == 8:
            #same functionality as [option 6]
            if option_8_available:
                collection("Students", studentsInfo)
                continue
            elif option_15_available:                
                collection("Students", dummyStudentsInfo)               
            else:
                print("\nIn order to view students you have to insert information first (option 3) or use dummy data (option 15).")                

        elif option == 9:
            #same functionality as [option 6]
            if option_9_available:
                collection("Assignments", assignmentsInfo)
                continue
            elif option_15_available:                
                collection("Assignments", dummyAssignmentsInfo)                 
            else:
                print("\nIn order to view assignments you have to insert information first (option 4) or use dummy data (option 15).")                 

        elif option == 10:
            if option_10_available:
                forPerCourse(studentsInfo)
                #creates a dict, prints it's key:value pairs, then returns it
                #option_10_11_12 variable not needed because it is True by default
                continue
                #prevents printing and the dummy data in case option_15_available == True
            elif option_15_available:
                forPerCourse(dummyStudentsInfo)
            else:
                print("\nIn order to view students per course you have to insert information about the students (option 3) or use dummy data (option 15).")

        elif option == 11:
            #same functionality as [option 10]
            if option_11_available:
                forPerCourse(trainersInfo)
                continue
            elif option_15_available:
                forPerCourse(dummyTrainersInfo)
            else:
                print("\nIn order to view trainers per course you have to insert information about the trainers (option 2) or use dummy data (option 15).")

        elif option == 12:
            #same functionality as [option 10]
            if option_12_available:
                forPerCourse(assignmentsInfo)
                continue
            elif option_15_available:
                forPerCourse(dummyAssignmentsInfo)
            else:
                print("\nIn order to view assignments per course you have to insert information about the assignments (option 4) or use dummy data (option 15).")
           
        elif option == 13:
            if option_13_available:
                for k,v in assignmentsMarks.items():
                    print("\n", k.center(50,'_'), "\n")
                    for k1,v1 in v.items():
                        print("\n", k1.center(50,'-'), "\n")
                        for i in v1:
                            print(i.center(50,' '))                
                continue
            elif option_15_available:
                #same functionality as [option 5] but for dummy data
                option_10_11_12 = False
                not_dummy = False
                stdsPerCourse = forPerCourse(dummyTrainersInfo, option_10_11_12)
                assPerCourse = forPerCourse(dummyAssignmentsInfo, option_10_11_12)
                dummyAssignmentMarks = assignmentMarksInfo(stdsPerCourse, assPerCourse, not_dummy)
                #last variable is False in order for the function to recognise that we use dummy data                
                for k,v in dummyAssignmentMarks.items():
                    print("\n", k.upper().center(50,'_'), "\n")
                    for k1,v1 in v.items():
                        print("\n", k1.center(50,'-'), "\n")
                        n = 0
                        for i in v1:
                            print(i.center(50,' ')) 
            else:
                print("\nIn order to view all assignments per student per course you have to do (option 5) or use dummy data (option 15).")
                
        elif option == 14:
            if option_14_available:
                print("\n", "The following students belong to more than one courses.".upper().center(50,'-'))
                for student in Students.multipleCoursesStd:
                    print(student)
                continue
            elif option_15_available:             
                print("\n", "The following students belong to more than one courses.".upper().center(50,'-'))
                n = 0
                for student in Students.dummyMultipleCoursesStd:
                    n += 1
                    print(f"{n}. {student}")
            else:
                print("\nIn order to view the students that belong to more than one courses you have to insert information about the students (option 3) or use dummy data (option 15).")

        elif option == 15:
            #same functionality as options 1,2,3,4 but for dummy data            
            dummyCoursesInfo = dummyCourses()
            dummyTrainersInfo = dummyTrainers()
            dummyStudentsInfo = dummyStudents()
            dummyAssignmentsInfo = dummyAssignments()
            option_15_available = True
            print("\n", "Dummy Data is now available for options [6-14]".center(85,'-'))
            print("\n", "***Note: Choosing one of the options [1-4] will cause dummy data to be overwritten for the corresponding option.***")
            #this note reflects to the continue statement implemented in options 10,11,12,13,14
            
        elif option == 0:
            exit("Exiting now.")

        else:
            print("\n", "Not available option, choose between [0-15]".center(85,'*'))
            #for numeric inputs out of the range [0,15]
                
    except ValueError:
        print("\n", "Not available option, choose between [0-15]".center(85,'*'))
        #for non numeric inputs
