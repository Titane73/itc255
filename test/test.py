import unittest
from user import User
from security import Security


class UserTest(unittest.TestCase):
    def setUp(self):
        self.user = User(999, 2, 'P@ssw0rd1', 'Ti', '999 Test', 2061112233, 'email@test.com', '01-01-1980')

    def test_UserString(self):
        self.assertEqual(str(self.user), 'P@ssw0rd1 Ti 999 Test')
    
    def test_getUserId(self):
        self.assertEqual(self.user.getUserId(), '999')
    
    def test_getUserType(self):
        self.assertEqual(self.user.test_getUserType(), 2)

class SecurityTest(unittest.TestCase):
    def setUp(self):
        self.secure = Security(2, True)
    
    def test_validateLogin(self):
        self.assertEqual(self.validateLogin(), 2)
    
    def test_checkRestriction(self):
        self.assertEqual(self, checkRestriction = True)
        

        
    
    

    
