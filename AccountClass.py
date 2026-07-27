import uuid

class Account():
    # Constructor
    def __init__(self, first_name, last_name, phone_num, email):
        # Validate name must be 3 char minimum, must be a string
        while len(first_name) < 3 or not isinstance(first_name, str):
            self.first_name = str(input("First name not valid, please enter a 3 letter name:"))
        self.first_name = first_name

        while len(last_name) < 3 or not isinstance(first_name, str):
            self.last_name = str(input("Last name not valid, please enter a 3 letter name:"))
        self.last_name = last_name

        # Generated UUID on init, cannot modify.
        #
        self.id = str(uuid.uuid4())

        # Phone num must be 10 digits, valid phone number
        self.phone_num = phone_num

        # Valid email ends with @ and the platform (@gmail, @hotmail, etc).
        self.email = email

        # Always init as zero.
        self.balance = 0

    def update_balance(self, new_balance):
        self.balance = new_balance

    """
    1. Phone num check (must be 10 digits)
    2. Name
    """

    # Dunder method for printing user data as representation
    def __repr__(self):
        return (
            f"Account("
            f"id='{self._id}', "
            f"name='{self.first_name} {self.last_name}', "
            f"phone='{self.phone_num}', "
            f"email='{self.email}', "
            f"balance=${self.balance:.2f}"
            f")"
        )
    pass