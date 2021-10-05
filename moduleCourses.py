class Courses:
    """This class represents a language course"""
    coursesInfo = []
    dummyCoursesInfo = []
    #these lists will be filled with class objects
    def __init__(self, c_title, c_language, c_description, c_type):
        self.c_title = c_title
        self.c_language = c_language
        self.c_description = c_description
        self.c_type = c_type

    def __str__(self):
        return f"{self.c_title}: {self.c_language}, {self.c_description}, {self.c_type}"
    

def addCourses():
    """This method asks for user input info, creates a class object, appends it to a list
    and finally returns a list with all class objects"""
    print("\n", " Courses information section ".upper().center(100,'-'), "\n")
    availableLanguages = ('C#', 'Java', 'Javascript', 'Python')

    while True:
        c_language = input(f"Select a language {availableLanguages} to add language course information or press 'q' to quit: ")
        if c_language in availableLanguages:
            print(f"\nFor {c_language} enter the following: Course Title, Course Description, Course Type.")
            c_title = input("Course Title: ")
            c_description = input("Course Descrpition: ")
            c_type = input("Course Type: ")
            x = Courses(c_title, c_language, c_description, c_type)
            Courses.coursesInfo.append(x)
            print("\n", ">New course: ", x, "\n")
        elif c_language == 'q':
            break
        else:
            print("\n", " Enter one of the available languages or check for typos. ".center(85,'*'), "\n")

    return Courses.coursesInfo

def dummyCourses():
    """This method creates dummy courses, simultaneously appends them to a list  and finally returns it"""
    Courses.dummyCoursesInfo.append(Courses('CB13FTCS', 'C#', '12 weeks', 'Full Time'))
    Courses.dummyCoursesInfo.append(Courses('CB13PTCS', 'C#', '24 weeks', 'Part Time'))
    Courses.dummyCoursesInfo.append(Courses('CB13FTJA', 'Java', '12 weeks', 'Full Time'))
    Courses.dummyCoursesInfo.append(Courses('CB13PTJA', 'Java', '24 weeks', 'Part Time'))
    Courses.dummyCoursesInfo.append(Courses('CB13FTJS', 'Javascript', '12 weeks', 'Full Time'))
    Courses.dummyCoursesInfo.append(Courses('CB13PTJS', 'Javascript', '24 weeks', 'Part Time'))
    Courses.dummyCoursesInfo.append(Courses('CB13FTPY', 'Python', '12 weeks', 'Full Time'))
    Courses.dummyCoursesInfo.append(Courses('CB13PTPY', 'Python', '24 weeks', 'Part Time'))

    return Courses.dummyCoursesInfo
