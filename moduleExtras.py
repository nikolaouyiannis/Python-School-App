from random import randint
from datetime import date


def collection(entity, itemsInfo):
    """This method takes as arguments a string (Language courses/Trainers/Students/Assignments) and
    a list containing objects of the corresponding entity in order to print them."""
    print("\n", entity.upper().center(50,'-'), "\n")
    for item in range(len(itemsInfo)):
        print(f"{item + 1}. {itemsInfo[item]}")
    

def forPerCourse(itemsInfo, option_10_11_12 = True):
    """This method takes as arguments a list that containts class objects and a boolean,
    in order to create a dict where keys are languages and the value is list that contains objects
    related to the language and returns it."""
    dictPerCourse = {'C#' : [], 'Java' : [], 'Javascript' : [], 'Python' : []}
    for item in itemsInfo:
        item.perCourse(dictPerCourse)
        #calls perCourse() method in moduleTrainersOrStudents
    if option_10_11_12:
        #executed only for printing
        for k, v in dictPerCourse.items():
            print("\n", '---', k, '---')
            for v in range(len(dictPerCourse[k])):
                print(f"{v+1}. {dictPerCourse[k][v]}")
    return dictPerCourse

def assignmentMarksInfo(stdsPerCourse, assPerCourse, not_dummy = True):
    """
    This method takes as arguments two dictionaries created by the forPerCourse() method.
    stdsPerCourse values are lists with students' names and for assPerCourse values are lists with assignment's titles.

    stdsPerCourse = {
        'C#' : ['name1', 'name2'],
        'Java' : ['name3', 'name4'],
        'Javascript' : ['name1', 'name5'],
        'Python' : ['name2',]
     }

    assPerCourse = {
        'C#' : ['title1', 'title2'],
        'Java' : ['title4'],
        'Javascript' : ['title5'],
        'Python' : ['title6', 'title7']
        }

    It creates a dict showing all the assignments per student per course.

    assignmentsMarks = {
        'C#' : {
            'student1' : {
                'title1' : [Oral Mark, markCode, Submission],
                'title2' : [Oral Mark, markCode, Submission],
                },
            'student2' : {
                'title1' : [Oral Mark, markCode, Submission],
                'title2' : [Oral Mark, markCode, Submission],
                }
            },
        'Java' : {}
        }
    """
    print("\n", "Students' Assignments information section".upper().center(100,'-'), "\n")
    assignmentsMarks = {'C#' : {}, 'Java' : {}, 'Javascript' : {}, 'Python' : {}}
    for lang in stdsPerCourse.keys():
        for std in stdsPerCourse[lang]:
            assignmentsMarks[lang].update({std:{}})
    for lang in assPerCourse.keys():
        for ass in assPerCourse[lang]:
            for std in assignmentsMarks[lang]:
                assignmentsMarks[lang][std].update({ass:[]})
                if not_dummy:
                    print("\n", f"Assignment: {ass} - Student: {std}".center(30,'-'))
                    while True:
                        try:
                            assignmentsMarks[lang][std][ass].append(float(input("Oral Mark: ")))
                            assignmentsMarks[lang][std][ass].append(float(input("Submitted Code Mark: ")))
                            assignmentsMarks[lang][std][ass].append(input("Submission Date (YYYY-MM-DD): "))
                            break
                        except ValueError:
                            print("\n", " Marks must be in numeric form and date in (YYYY-MM-DD) form ".center(85,'*'), "\n")
                elif not not_dummy:
                    assignmentsMarks[lang][std][ass].append(randint(0,50))
                    assignmentsMarks[lang][std][ass].append(randint(0,50))
                    assignmentsMarks[lang][std][ass].append('2021-MM-DD')                    
    return assignmentsMarks
