'''
Created on 15 Nov 2014

@author: MuresanVladut
'''

class Controller:
    def __init__(self,aRepo,sRepo):
        self.aRepo=aRepo
        self.sRepo=sRepo
    def statistic(self,grade,homework):
        self.aRepo.data={k:v for k,v in self.aRepo.data.items() if v.getGrade()<=grade and v.getDescription()==homework}
        self.sRepo.data={k:v for k,v in self.sRepo.data.items() if k in self.aRepo.data.keys()}
    