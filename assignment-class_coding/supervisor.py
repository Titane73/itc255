from user import User
from sale import Sale
from checker import Checker

class Supervisor():
    def __init__(self, supervisor_id, supervisor_grade, security_level):
        self.supervisor_id = supervisor_id
        self.supervisor_grade = supervisor_grade
        self.security_level = security_level

    def getSupervisorId(self):
        return self.supervisor_id
    
    def getGrade(self):
        return self.supervisor_grade
    
    def getSecurity():
        return self.security_level

    # returns the supervisor grade as string
    def __str__(self):
        return self.supervisor_grade

    
    def addChecker(self):
        # method for admin option for supervisor
        # linked to User and Checker classes
    

