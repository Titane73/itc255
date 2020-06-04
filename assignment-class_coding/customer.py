from user import User
from sale import Sale
from rewards import Rewards

class Customer():
    def __init__(self, customer_id, reward_id, security_level):
        self.customer_id = customer_id
        self.reward_id = reward_id
        self.security_level = security_level

    def getCustomerId(self):
        return self.customer_id
    
    def getReward(self):
        # method to get point total form rewards table
        # seems like there may need to be more here?
        return self.reward_id
    
    def getSecurity(self):
        return self.security_level

    def getHistory(self):
        # method to get purchase history
        # linked to Sale and SaleDetail

     