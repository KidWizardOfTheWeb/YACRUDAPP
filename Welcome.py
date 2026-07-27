import BankClass

# Bank instance is global
bank_inst = BankClass.Bank()

OPTION_LIST = ("1. View account"
               "2. Update accounts"
               "3. Add accounts"
               "4. Remove accounts")

# All valid options for our menu, ranges from 1 to end option
VALID_OPTIONS = [str(x) for x in range(1, 4)]

# FUNC_LIST = {
#     "1": func
# }


# View accounts from the account_dict
# If param sent is "ALL", print all accounts.
def view_account():

    account_query = input("Type the UUID of the account to display, or type ALL to see all accounts:")

    if account_query != "ALL":
        print(bank_inst.account_dict[account_query])
        pass
    pass

# Treat main as menu selector
if __name__ == "__main__":
    print(OPTION_LIST)
    user_opt = str(input("Select an option with a number:"))

    if user_opt in VALID_OPTIONS:
        # Select the matching functions


        pass
    pass