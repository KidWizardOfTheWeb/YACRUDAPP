import BankClass

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
        print(bank_inst.account_dict.values())
    else:
        # Else, try to retrieve the single instance.
        # If not found, return string
        retrieved_account = bank_inst.account_dict.get(account_query, "No account found.")
        print(retrieved_account)
    pass

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
        print(removed_account)


OPTION_LIST = ("1. View account\n"
               "2. Update accounts\n"
               "3. Add accounts\n"
               "4. Remove accounts\n")

# All valid options for our menu, ranges from 1 to end option
VALID_OPTIONS = [str(x) for x in range(1, 4)]

FUNC_LIST = {
    "1": view_account
}

# Treat main as menu selector
if __name__ == "__main__":
    print("Welcome to the bank managing app.\n")

    # Loop until end of time.
    while True:
        print(OPTION_LIST)
        user_opt = str(input("Select an option with a number:"))

        if user_opt in VALID_OPTIONS:
            # Select the matching functions
            FUNC_LIST[user_opt]()
            pass
        pass