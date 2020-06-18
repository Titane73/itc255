from user import User
from sale import Sale

class Checker():
    def __init__(self, checker_id, checker_grade, security_level):
        self.checker_id = checker_id
        self.checker_grade = checker_grade
        self.security_level = security_level

    def getCheckerId(self):
        return self.checker_id
    
    def getGrade(self):
        return self.checker_grade
    
    def getSecurity():
        return self.security_level
    
    def salesAdmin(self):
        # method for admin option for checker
        # linked to Sale class
        return self.salesAdmin
    
    # returns the checker grade as string
    def __str__(self):
        return self.checker_grade

