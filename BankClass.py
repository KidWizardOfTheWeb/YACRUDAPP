import uuid

# THIS IS OUR MAIN CLASS
class Bank:
    # All accounts, key = UUID, value = account obj
    account_dict = {}

    # Functions to search for all accounts with X property
    # Filters through users that have a balance based on basic conditionals (greater than, less than, etc)
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
    
    def remove_account(self, account_id):
        """
        Remove an account using its UUID.
        """
        return self.account_dict.pop(account_id, None)