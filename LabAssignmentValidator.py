'''
Created on 18 Nov 2014

@author: MuresanVladut
'''

class LabAssignmentValidator: 
    def validate(self,c):
        errors = ""
        try:
            int(c.idd)
        except ValueError:
            errors +=" Id must be an integer  \n"
        try:
            int(c.group)
        except ValueError:
            errors+=" Group must be an integer \n"
        try:
            int(c.grade)
        except ValueError:
            errors+=" Grade must be an integer \n"
        if (c.idd==0):
            errors += "Id must not be 0 \n"
        if (c.name==""):
            errors += "Name must not be empty \n"
        if (c.group==0):
            errors += "Group must not be 0 \n"
        if (c.description==""):
            errors += "Description must no be empty \n"
        if (c.deadline==""):
            errors += "Deadline must not be empty \n"
        if (c.grade==0):
            errors += " Grade must no be 0 \n"
        if (len(errors)>0):
            raise ValueError(errors)