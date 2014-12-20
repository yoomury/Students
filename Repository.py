'''
Created on 15 Nov 2014

@author: MuresanVladut
'''




from StudentsValidator import StudentValidator
from AssignmentsValidator import AssignmentValidator
from LabAssignmentValidator import LabAssignmentValidator
from Students import Student
from Assignments import Assignment
from LabAssignment import LabAssignment


class Repository:
    def __init__(self):
        self.data={}
    def getAll(self):
        return list(self.data.values())
    def getId(self):
        return list(self.data.keys())
    def remove(self,idd):
        try:
            self.data.pop(idd)
        except KeyError:
            raise KeyError('Invalid id')
    def update(self,obj):
        try:
            self.data[obj.idd]=obj
        except KeyError:
            raise KeyError
        
    def find(self,idd):
        try:
            return self.data[idd]
        except KeyError:
            raise KeyError
 
    
class StudentRepo(Repository):
    def __init__(self):
        self.validator=StudentValidator()
        Repository.__init__(self)
    def add(self,obj):
        if (obj.idd in self.data.values()):
            raise KeyError
        self.validator.validate(obj)
        self.data[obj.idd]=obj
    def getName(self):
        for value in self.data.values():
            yield    value.getName()
class AssignmentRepo(Repository):
    def __init__(self):
        self.validator=AssignmentValidator()
        Repository.__init__(self)
    def add(self,obj):
        if (obj.idd in self.data.values()):
            raise KeyError
        self.validator.validate(obj)
        self.data[obj.idd]=obj
    '''def filter(self,description):
        for value in self.data.values():
            if description!=value.getDescription():
                self.data.pop(value.getId())
        return self.data'''
    def getDescription(self):
        for value in self.data.values():
            return value.getDescription()
    def getGrade(self):
        for value in self.data.values():
            return value.getGrade()
        
        
        
        
class LabAssignmentRepo(Repository):
    def __init__(self):
        self.validator=LabAssignmentValidator()
        Repository.__init__(self)
    def add(self,obj):
        if (obj.idd in self.data.values()):
            raise KeyError
        self.validator.validate(obj)
        self.data[obj.idd]=obj
        

