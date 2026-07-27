import BankClass
import AccountClass

# Bank instance is global
bank_inst = BankClass.Bank()

# View accounts from the account_dict
# If param sent is "ALL", print all accounts.
def view_account():
    # If no accounts, print that there are none.
    if bank_inst.account_dict is None:
        print("No accounts to show!")
        return

    account_query = str(input("Type the UUID of the account to display, or type ALL to see all accounts:"))

    if account_query == "ALL":
        # Print all account values
        print(list(bank_inst.account_dict.values()))
    else:
        # Else, try to retrieve the single instance.
        # If not found, return string
        retrieved_account = bank_inst.account_dict.get(account_query, "No account found.")
        print(retrieved_account)
    pass

def add_account():
    first_name = str(input("Enter first name:"))
    last_name = str(input("Enter last name:"))
    phone_num = str(input("Enter phone number:"))
    email = str(input("Enter email:"))
    account = bank_inst.make_newaccount(first_name, last_name, phone_num, email)
    return account

def remove_account():
    if not bank_inst.account_dict:
        print("No accounts available to remove.")
        return

    account_id = input("Enter the UUID of the account to remove: ").strip()

    removed_account = bank_inst.remove_account(account_id)

    if removed_account is None:
        print("No account was found with that UUID.")
    else:
        print("Account successfully removed:")
        print(removed_account, "\n")

def modify_details():
    # bank_inst.add_dummy_account()
    details_from_class = [detail for detail in dir(AccountClass.Account) if not detail.startswith('_')]
    print("Details that you can update:\n", details_from_class)

    detail_chosen = str(input("Enter detail to update:"))

    while detail_chosen not in details_from_class:
        detail_chosen = int(input("Enter detail to update:"))

    # If valid, choose option
    idx = details_from_class.index(detail_chosen)

    attribute_to_get = details_from_class[idx].split("_")[1]

    # getattr(bank_inst.account_dict['cee2c9a5-313a-4810-9289-32a4d69d1d1a'], 'email')

    if bank_inst.account_dict is None:
        print("No accounts to show!")
        return

    account_query = str(input("Type the UUID of the account to update:"))

    if bank_inst.account_dict.get(account_query, None) is not None:
        getattr(bank_inst.account_dict[account_query], attribute_to_get)

        new_value_for_field = input("Type a new value for the field:")
        setattr(bank_inst.account_dict[account_query], attribute_to_get, new_value_for_field)
        # bank_inst.account_dict[account_query].balance = new_balance
    pass

def modify_balance():
    new_balance = int(input("Enter new balance:"))

    while not isinstance(new_balance, int):
        new_balance = int(input("Enter new balance:"))

    if bank_inst.account_dict is None:
        print("No accounts to show!")
        return

    account_query = str(input("Type the UUID of the account to update:"))
    if bank_inst.account_dict.get(account_query, None) is not None:
        bank_inst.account_dict[account_query].balance = new_balance
    pass

OPTION_LIST = ("1. View account\n"
               "2. Update accounts\n"
               "3. Add accounts\n"
               "4. Remove accounts\n"
               "5. Modify account balance\n")

# All valid options for our menu, ranges from 1 to end option
VALID_OPTIONS = [str(x) for x in range(1, 6)]

FUNC_LIST = {
    "1": view_account,
    "2": modify_details,
    "3": add_account,
    "4": remove_account,
    "5": modify_balance
}

# Treat main as menu selector
if __name__ == "__main__":
    print("Welcome to the bank managing app.\n")

    # Loop until end of time.
    while True:
        print(OPTION_LIST)
        user_opt = str(input("Select an option with a number:\n"))

        if user_opt in VALID_OPTIONS:
            # Select the matching functions
            FUNC_LIST[user_opt]()
            pass
        pass