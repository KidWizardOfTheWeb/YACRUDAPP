import uuid

class Account:
    # Constructor
    def __init__(self, first_name, last_name, phone_num, email):

        # Validate and store customer information
        self.first_name = self.validate_name(first_name, "First")
        self.last_name = self.validate_name(last_name, "Last")

        # Generated UUID on init, cannot modify.
        # Should be private, as this is used as a key for BankClass.
        self._id = str(uuid.uuid4())

        # Validate and store contact information
        self.phone_num = self.validate_phone(phone_num)
        self.email = self.validate_email(email)

        # Always initialize balance as zero
        self.balance = 0


    # Validation Methods

    def validate_name(self, name, name_type):

        while not isinstance(name, str) or len(name) < 3:
            name = input(
                f"{name_type} name not valid, please enter a 3+ letter name: "
            )

        return name


    def validate_phone(self, phone_num):

        while len(str(phone_num)) != 10 or not str(phone_num).isdigit():
            phone_num = input(
                "Phone number not valid, please enter a 10 digit number: "
            )

        return str(phone_num)


    def validate_email(self, email):
        while "@" not in email and "." not in email:
            email = input(
                "Email not valid, please enter a valid email: "
            )

        return email


    # Account Methods

    def update_balance(self, new_balance):
        self.balance = new_balance

    def update_account(
        self,
        first_name=None,
        last_name=None,
        phone_num=None,
        email=None
    ):

        if first_name is not None:
            self.first_name = self.validate_name(
                first_name,
                "First"
            )

        if last_name is not None:
            self.last_name = self.validate_name(
                last_name,
                "Last"
            )

        if phone_num is not None:
            self.phone_num = self.validate_phone(phone_num)

        if email is not None:
            self.email = self.validate_email(email)



    #Call this to get a string representation of the account
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



# FOR TESTING
DUMMY_ACCOUNT = Account("XXX", "YYY", "1234567890", "ABC@gmail.com")