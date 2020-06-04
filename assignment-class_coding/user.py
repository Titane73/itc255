class User():
    def __init__(self, user_id, user_type, password, name, address, phone, email, dob):
        self.user_id = user_id
        self.user_type = user_type
        self.password = password
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        self.dob = dob

    def getUserId(self):
        return self.user_id
    
    def getUserType(self):
        return self.user_type
    
    def getPassword(self):
        return self.password
    
    def getName(self):
        return self.name
    
    def getAddress(self):
        return self.address
    
    def getPhone(self):
        return self.phone
    
    def getEmail(self):
        return self.email
    
    def getDob(self):
        return self.dob

    # returns the values as string
    def __str__(self):
        return self.password

    def __str__(self):
        return self.name

    def __str__(self):
        return self.address