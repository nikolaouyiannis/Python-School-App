from abc import ABC, abstractmethod
from datetime import date

class Person(ABC):
    """This class serves as parent to Trainers class and Students class"""
    @abstractmethod
    def __init__(self, fname, lname, memberID, language):
        self.fname = fname
        self.lname = lname
        self.memberID = memberID
        if language == None:
            self.language = self.addLanguage()
            #in this case, instance variable 'language' is a set
        else:
            self.language = language
        #the purpose of this if statement is to handle differently dummy objects, where language is set by default

    def addLanguage(self):
        """This method is called when an object is initiated by the user, in order to give a value to instance variable 'language'.
        It returns a set containing languages the user teaches/learns."""
        availableLanguages = ('C#', 'Java', 'Javascript', 'Python')
        self.language = set()
        #set in order to avoid double entrys

        while True:
            given_language = input(f"\nEnter language {availableLanguages} for this person or press 'q' to stop entering: ")
            if given_language in availableLanguages and given_language != 'q':
                self.language.add(given_language)
                continue
            elif given_language == 'q' and len(self.language) == 0:
                print("\n", " Enter a language before quiting. ".center(85,'*'))
                continue                
            elif given_language == 'q':
                break
            else:
                print("\n", " Enter one of the available languages or check for typos. ".center(85,'*'))
                continue                

        return self.language

    def perCourse(self, dictPerCourse):
        """This method takes as an argument this dict {'C#' : [], 'Java' : [], 'Javascript' : [], 'Python' : []} (from moduleExtras),
        in order to add as value the person's full name depending on the language it teaches/learns."""
        self.full_name = f"{self.fname} {self.lname}"

        for lang in self.language:
        #iterating through the set that contains the languages
            if lang == 'C#':
                dictPerCourse['C#'].append(self.full_name)
            elif lang == 'Java':
                dictPerCourse['Java'].append(self.full_name)
            elif lang == 'Javascript':
                dictPerCourse['Javascript'].append(self.full_name)
            else:
                dictPerCourse['Python'].append(self.full_name)

        return dictPerCourse


class Trainers(Person):
    """This class represents a trainer"""
    trainersInfo = []
    dummyTrainersInfo = []
    #these lists will be filled with class objects
    def __init__(self, fname, lname, memberID, language):
        super().__init__(fname, lname, memberID, language)

    def __str__(self):
        return f"{self.memberID}: {self.fname} {self.lname}, {self.language}"
            


class Students(Person):
    """This class represents a student"""
    studentsInfo = []    
    multipleCoursesStd = []
    dummyStudentsInfo = []
    dummyMultipleCoursesStd = []
    #these lists will be filled with class objects
    def __init__(self, fname, lname, memberID, language, fees, birthdate):
        super().__init__(fname, lname, memberID, language)
        self.fees = fees
        self.birthdate = birthdate

    def __str__(self):
        return f"{self.memberID}: {self.fname} {self.lname}, {self.language}, {self.birthdate}, Fees = {self.fees}"


def addTrainers():
    """This method accepts user input info, creates a class object, appends it to a list
    and finally returns a list with all class objects"""
    print("\n", " Trainers information section ".upper().center(100,'-'), "\n")

    while True:
        fname = input("Enter trainer's first name: ")
        lname = input("Enter trainer's last name: ")
        memberID = "TR_" + input("Enter trainer's member ID: ")
        x = Trainers(fname, lname, memberID, None)
        Trainers.trainersInfo.append(x)
        print("\n", ">New trainer: ", x, "\n")
        q = input(" To continue adding trainers press any key. To quit press 'q'. ".center(100, '>'))
        if q == 'q':
            break

    return Trainers.trainersInfo

def dummyTrainers():
    """This method creates dummy trainers, simultaneously appends them to a list, and finally returns it"""
    Trainers.dummyTrainersInfo.append(Trainers('Georges', 'St-Pierre', 'TR_001', {'C#', 'Java', 'Javascript', 'Python'}))
    Trainers.dummyTrainersInfo.append(Trainers('Jon', 'Jones', 'TR_002', {'Java', 'Javascript'}))
    Trainers.dummyTrainersInfo.append(Trainers('Khabib', 'Nurmagomedov', 'TR_003', {'Python', }))
    Trainers.dummyTrainersInfo.append(Trainers('Anderson', 'Silva', 'TR_004', {'C#', 'Python'}))
    Trainers.dummyTrainersInfo.append(Trainers('Francis', 'Ngannou', 'TR_005', {'C#', 'Java'}))
    Trainers.dummyTrainersInfo.append(Trainers('Amanda', 'Nunes', 'TR_006', {'Javascript', 'Python'}))
    Trainers.dummyTrainersInfo.append(Trainers('Robert', 'Whittaker', 'TR_007', {'Java', 'Javascript', 'Python'}))
    Trainers.dummyTrainersInfo.append(Trainers('Nick', 'Diaz', 'TR_008', {'C#', }))
    Trainers.dummyTrainersInfo.append(Trainers('Ronda', 'Rousey', 'TR_009', {'C#', 'Javascript'}))
    Trainers.dummyTrainersInfo.append(Trainers('Valentina', 'Shevchenko', 'TR_010', {'Python', }))

    return Trainers.dummyTrainersInfo
    

def addStudents():
    """This method accepts user input info, creates a class object, appends it to a list
    and finally returns a list with all class objects"""
    print("\n","Students information section".upper().center(100, '-'), "\n")

    while True:
        fname = input("Enter student's first name: ")
        lname = input("Enter student's last name: ")
        memberID = "ST_" + input("Enter student's member ID: ")

        while True:
            try:
                fees = float(input("Enter student's fees (numeric): "))
                y = int(input("Enter year of birth: "))
                m = int(input("Enter month of birth: "))
                d = int(input("Enter day of birth: "))
                break
            except ValueError:
                print("\n", " Your input has to be a number. ".center(85,'*'), "\n")

        birthdate = date(y, m, d)
        x = Students(fname, lname, memberID, None, fees, birthdate)
        Students.studentsInfo.append(x)
        print("\n", ">New student: ", x, "\n")
        if len(x.language) > 1:
            #checks if the student learns multiple languages, if true it appends it's name to the corresponding list
            Students.multipleCoursesStd.append(f"{x.fname} {x.lname}")
        q = input("\nTo continue adding students press any key. To quit press 'q' ".center(100, '>'))
        if q == 'q':
            break

    return Students.studentsInfo

def dummyStudents():
    """This method creates dummy students, simultaneously appends them to a list, and finally returns it"""
    Students.dummyStudentsInfo.append(Students('Joe', 'Gatto', 'ST_A01', {'C#', 'Java', 'Javascript', 'Python'}, 300, '2000-1-1'))
    Students.dummyStudentsInfo.append(Students('Sal', 'Vulcano', 'ST_W45', {'Java', 'Javascript'}, 300, '2001-1-1'))
    Students.dummyStudentsInfo.append(Students('Brian', 'Quinn', 'ST_B99', {'Python', }, 300, '2002-1-1'))
    Students.dummyStudentsInfo.append(Students('James', 'Murray', 'ST_S11', {'C#', 'Python'}, 300, '2003-1-1'))
    Students.dummyStudentsInfo.append(Students('Lauren', 'Cohan', 'ST_A10', {'C#', 'Java'},  300, '2004-1-1'))
    Students.dummyStudentsInfo.append(Students('Danai', 'Gurira', 'ST_R20', {'Javascript', 'Python'},  300, '2005-1-1'))
    Students.dummyStudentsInfo.append(Students('Jeffrey Dean', 'Morgan', 'ST_R21', {'Java', 'Javascript', 'Python'},  300, '2006-1-1'))
    Students.dummyStudentsInfo.append(Students('Christian', 'Serratos', 'ST_B13', {'C#', },  300, '2007-1-1'))
    Students.dummyStudentsInfo.append(Students('Andrew', 'Lincoln', 'ST_007', {'C#', 'Javascript'},  300, '2008-1-1'))

    for std in Students.dummyStudentsInfo:
        #iterating through the list that contains dummy students
        if len(std.language) > 1:
            #checks if the student learns multiple languages, if true it appends it's name to the corresponding list
            Students.dummyMultipleCoursesStd.append(f"{std.fname} {std.lname}")
            
    return Students.dummyStudentsInfo

    

