from AccountClass import Account


# Create account object
account = Account(
    "John",
    "Smith",
    "5551234567",
    "john@gmail.com"
)


# Test __repr__
print("\n--- Account Creation ---")
print(account)


# Test update_balance
print("\n--- Balance Update ---")

account.update_balance(500)

print(account)


# Test update_account
print("\n--- Account Update ---")

account.update_account(
    first_name="Johnny",
    phone_num="1112223333",
    email="johnny@gmail.com"
)

print(account)