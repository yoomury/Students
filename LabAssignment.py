'''
Created on 18 Nov 2014

@author: MuresanVladut
'''


class LabAssignment:
    def __init__(self,Student,Assignment):
        self.Student=Student
        self.Assignment=Assignment
    def __str__(self):
        return "The student "+self.Student.getName() + " with the id: "+ str(self.Student.getId()) + " which is in the group: "+str(self.Student.getGroup())+ " has the assignment "+self.Assignment.getDescription()+" with the deadline on: "+str(self.Assignment.getDeadline())+" and the grade: "+str(self.Assignment.getGrade())+"."            


