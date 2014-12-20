'''
Created on 15 Nov 2014

@author: MuresanVladut
'''

from Assignments import Assignment
from LabAssignment import LabAssignment
from Repository import StudentRepo,AssignmentRepo
from Students import Student
from AssignmentsValidator import AssignmentValidator
from StudentsValidator import StudentValidator
from Controller import Controller



class Console:
    def __init__(self,ctrl):
        self.ctrl=ctrl
        
    def showMenu(self):
        print('''1. Students
2. Assignments.
3. Data Base.''')
    def run(self):
        menu={1:self.uiStudents,2:self.uiAssignments,3:self.uiDatabase}
        while True:
            self.showMenu()
            try:
                opt=int(input("Choose option: "))
                menu[opt]()
            except ValueError:
                print("Invalid option")
            except KeyError:
                print("Unimplemented option")
    def uiStudents(self):
        print('''1. Add a student.
2. Remove a student.
3. Find a student.
4  Print a student.
5. Main menu.''')
        menu={1:self.addStudent,2:self.removeStudent,3:self.findStudent,4:self.printStudent,5:self.run}
        while True:
            try:
                opt=int(input("Choose option: "))
                menu[opt]()
            except ValueError:
                print("Invalid option.")
            except KeyError:
                print("Unimplemented option.")

    def addStudent(self):
        while True:
            try:
                idd=int(input("Please enter the id: "))
                break
            except ValueError:
                print("Invalid id.")
                
        
        name=str(input("Please enter the name: ")) 
        while True:
            try:
                group=int(input("Please enter the group: "))
                break
            except ValueError:
                print("Invalid group.")
                
        s=Student(idd,name,group)
        sVal.validate(s)
        sRepo.add(s)
        self.uiStudents()
    def printStudent(self):
        print(sRepo.getAll())
        self.uiStudents()
    def removeStudent(self):
            try:
                idd=int(input("Please enter the id you want to remove: "))
                sRepo.remove(idd)
            except ValueError:
                print("Invalid id.")
        
            self.uiStudents()
    def findStudent(self):
        try:
            idd=int(input("Please enter the id you want to find: "))
            print(sRepo.find(idd))
        except ValueError:
            print("Invalid input")
            
        self.uiStudents()


    def uiAssignments(self):
        print('''1. Add an assignment.
2. Remove an assignment.
3. Find an assignment.
4  Print an assignment.
5. Main menu.''')
        menu={1:self.addAssignment,2:self.removeAssignment,3:self.findAssignment,4:self.printAssignment,5:self.run}
        while True:
            try:
                opt=int(input("Choose option: "))
                menu[opt]()
            except ValueError:
                print("Invalid option.")
            except KeyError:
                print("Unimplemented option.")    


    def addAssignment(self):
        print(sRepo.getAll())
        i=int(input("Choose the student for the assignment: "))
        while True:
            try:
                '''ry:
                    idd=int(input("Please enter the id (press any non numerical key to go back): "))
                except ValueError:
                    self.run()'''
                
                try:
                    idd=list(sRepo.getId())[i-1]
                except IndexError:
                    print("Id out of range.")
                    self.addAssignment()
                description=input("Please enter the description: ")
                while True:
                    try:
                        year2=int(input("Please enter the deadline's year: "))
                    except ValueError:
                        print("Invalid input.")
                    if year2 not in range(2014,2016):
                            print("The year must be 2014 or 2014.")
                    else:
                        year=year2
                        break
                    
                while True:
                    try:
                        month2=int(input("Please enter the deadline's month: "))
                    except ValueError:
                        print("Invalid input")
                    if month2 not in range(1,13):
                        print("The month must be between 1 and 12.")
                    else:
                        month=month2
                        break
                    
                while True:
                    try:
                        day2=int(input("Please enter the deadline's day: "))
                    except ValueError:
                        print("Invalid input")
                    if day2 not in range(1,32):
                        print("The day must be between 1 and 31.")
                    else:
                        day=day2
                        break
                
                deadline=str(day)+"."+str(month)+"."+str(year)
                try:
                    grade=int(input("Please enter the grade: "))
                except ValueError:
                    self.uiAssignments()
                a=Assignment(idd,description,deadline,grade)
                aVal.validate(a)
                aRepo.add(a)
                self.uiAssignments()
            except ValueError:
                break
    def removeAssignment(self):
        try:
            idd=int(input("Please enter the id you want to remove: "))
        except ValueError:
            print("Invalid input")
        aRepo.remove(idd)
        self.uiAssignments()
    def findAssignment(self):
        try:
            idd=int(input("Please enter the id you want to find: "))
            print(aRepo.find(idd))
        except ValueError:
            print("Invalid input")
            
        self.uiAssignments()
    def printAssignment(self):
        print(aRepo.getAll())
        self.run()


    def uiDatabase(self):
        print('''1. Print the database.
2. Statistics.
3. Main menu.''')
        menu={1:self.printFinal,2:self.statisticsss,3:self.run}
        while True:
            try:
                opt=int(input("Choose option: "))
                menu[opt]()
            except ValueError:
                print("Invalid option")
            except KeyError:
                print("Unimplemented option")    


    def statisticsss(self):
            try:
                a=int(input("Enter the desired grade: "))
            except ValueError:
                print("Invalid option")
            b=input("Enter the desired assignment: ")
            
            
            ctrl.statistic(a,b)
            for i in range(len(self.sRepo.data.keys())):
                print("The student "+str(((self.sRepo.getAll())[i].getName()))+" with the id: "+str(((self.sRepo.getAll()[i].getId())))+" has passed the statistic that the grade is smaller than: "+str(a)+" and the homework to be: "+str(b))
            self.uiDatabase()
    def printFinal(self):
        for value in sRepo.data.keys():
            lab=LabAssignment(sRepo.data[value],aRepo.data[value])
            print(lab)
    
        





aVal=AssignmentValidator()
sVal=StudentValidator()
sRepo=StudentRepo()
aRepo=AssignmentRepo()


ctrl=Controller(aRepo,sRepo)
console=Console(Controller)
console.run()



