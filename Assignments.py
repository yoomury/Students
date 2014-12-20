'''
Created on 15 Nov 2014

@author: MuresanVladut
'''


class Assignment:
    def __init__(self,idd,description,deadline,grade):
        self.idd=idd
        self.description=description
        self.deadline=deadline
        self.grade=grade
    def getId(self):
        return self.idd
    def getDescription(self):
        return self.description
    def getDeadline(self):
        return self.deadline
    def getGrade(self):
        return self.grade
    def setId(self,idd):
        self.idd=idd
    def setDescription(self,description):
        self.description=description
    def setDeadline(self,deadline):
    
        self.deadline=deadline
    def setGrade(self,grade):
        self.grade=grade
    def __str__(self):
        return "The assignment "+self.description+" with the id "+str(self.idd)+" and it's deadline "+str(self.deadline)+" has the grade: "+str(self.grade)
    def __repr__(self):
        return str(self.idd)+":"+str(self.description)+":"+str(self.deadline)+":"+str(self.grade)