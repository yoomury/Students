'''
Created on 15 Nov 2014

@author: MuresanVladut
'''



class Student:
    def __init__(self,idd,name,group):
        self.idd=idd
        self.name=name
        self.group=group
    def getId(self):
        return self.idd
    def getName(self):
        return self.name
    def getGroup(self):
        return self.group
    def setId(self,idd):
        self.idd=idd
    def setName(self,name):
        if not isinstance(name,str):
            raise TypeError
        self.name=name
    def setGroup(self,group):
        self.group=group
    def __str__(self):
        '''return "The student "+self.name+" with the id "+str(self.idd)+" is in the group "+str(self.group)'''
        return "The student "+self.getName()+" with the id "+str(self.getId())+" is in the group "+str(self.getGroup())
    def __repr__(self):
        return str(self.idd)+":"+str(self.name)+":"+str(self.group)


