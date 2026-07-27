import uuid

class Account():
    # Constructor
    def __init__(self, name, phone_num, email):
        self.name = name
        self._id = str(uuid.uuid4()) # Generated UUID on init, cannot modify (private)
        self.phone_num = phone_num
        self.email = email
        self.balance = 0

    def update_balance(self, new_balance):
        self.balance = new_balance

    
    pass