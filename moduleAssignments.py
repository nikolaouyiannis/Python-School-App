from datetime import date

class Assignments:
    """This class represents a course assignment"""
    assignmentsInfo = []
    dummyAssignmentsInfo = []
    #these lists will be filled with class objects
    def __init__(self, assignment_tilte, assignment_lang, assignment_descr, assignment_deadline):
        self.assignment_tilte = assignment_tilte
        self.assignment_lang = assignment_lang
        self.assignment_descr = assignment_descr
        self.assignment_deadline = assignment_deadline

    def __str__(self):
        return f"{self.assignment_tilte}: {self.assignment_lang}, {self.assignment_descr}, {self.assignment_deadline}"

    def perCourse(self, dictPerCourse):
        """This method takes as an argument a dict with language:[empty list] key:value pairs (from moduleExtras),
        in order to add as value the assignment's title depending on the language it belongs to."""

        if self.assignment_lang == 'C#':
            dictPerCourse['C#'].append(f"{self.assignment_tilte}")
        elif self.assignment_lang == 'Java':
            dictPerCourse['Java'].append(f"{self.assignment_tilte}")
        elif self.assignment_lang == 'Javascript':
            dictPerCourse['Javascript'].append(f"{self.assignment_tilte}")
        else:
            dictPerCourse['Python'].append(f"{self.assignment_tilte}")

        return dictPerCourse


def addAssignments():
    """This method accepts user input info, creates a class object, appends it to a list
    and finally returns a list with all class objects"""
    print("\n", "Assignment information section".upper().center(100,'-'), "\n")
    availableLanguages = ('C#', 'Java', 'Javascript', 'Python')

    while True:
        assignment_lang = input(f"Select the language {availableLanguages} that this assignment refers to or press 'q' to quit: ")
        if assignment_lang in availableLanguages:
            print("\nFor the assignment enter the following: Title, Description, Date of Submission.")
            assignment_tilte = input("Title: ")
            assignment_descr = input("Description: ")

            while True:
                try:
                    date_entry = input("Deadline date of assignment submission (YYYY-MM-DD): ")
                    y, m, d = map(int, date_entry.split('-'))
                    assignment_deadline = date(y, m, d)
                    break
                except ValueError:
                    print("Date is not in correct format (YYYY-MM-DD). Try again ".center(85,'*'), "\n")
                    continue

            x = Assignments(assignment_tilte, assignment_lang, assignment_descr, assignment_deadline)
            Assignments.assignmentsInfo.append(x)
            print("\n", ">New assignment: ", x, "\n")
        elif assignment_lang == 'q':
            break
        else:
            print("\n", " Enter one of the available languages or check for typos ".center(85,'*'), "\n")

    return Assignments.assignmentsInfo

def dummyAssignments():
    """This method creates dummy assignments, simultaneously appends them to a list, and finally returns it"""
    Assignments.dummyAssignmentsInfo.append(Assignments('CS_Brief', 'C#', 'Introductory', '2021-03-01'))
    Assignments.dummyAssignmentsInfo.append(Assignments('CS_Final', 'C#', 'Final for Graduation', '2021-09-30'))
    Assignments.dummyAssignmentsInfo.append(Assignments('JA_Brief', 'Java', 'Introductory', '2021-03-01'))
    Assignments.dummyAssignmentsInfo.append(Assignments('JA_Final', 'Java', 'Final for Graduation', '2021-09-30'))
    Assignments.dummyAssignmentsInfo.append(Assignments('JS_Brief', 'Javascript', 'Introductory', '2021-03-01'))
    Assignments.dummyAssignmentsInfo.append(Assignments('JS_Final', 'Javascript', 'Final for Graduation', '2021-09-30'))
    Assignments.dummyAssignmentsInfo.append(Assignments('PY_Brief', 'Python', 'Introductory', '2021-03-01'))
    Assignments.dummyAssignmentsInfo.append(Assignments('PY_Final', 'Python', 'Final for Graduation', '2021-09-30'))

    return Assignments.dummyAssignmentsInfo
  
