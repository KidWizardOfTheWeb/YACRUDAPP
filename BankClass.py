import uuid

from AccountClass import Account

# THIS IS OUR MAIN CLASS
class Bank:
    # All accounts, key = UUID, value = account obj
    account_dict = {}

    # Functions to search for all accounts with X property
    # Filters through users that have a balance based on basic conditionals (greater than, less than, etc)
    def make_newaccount(self, first_name, last_name, phone_num, email):
        new_account = Account(first_name, last_name, phone_num, email)
        self.account_dict[new_account.id] = new_account
        return new_account
    def find_balance_that_matches(self, condition, balance):
        pass

    def find_account(self, first_name=None, last_name=None, phone_num=None, email=None):
        # Retrieve all accounts that satisfy the given details
        matching_accounts = []

        for account in self.account_dict.values():

            if first_name is not None and account.first_name != first_name:
                continue

            if last_name is not None and account.last_name != last_name:
                continue

            if phone_num is not None and account.phone_num != phone_num:
                continue

            if email is not None and account.email != email:
                continue

            matching_accounts.append(account)

        return matching_accounts