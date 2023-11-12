from factory import AccountFactorySingleton
from exceptions import AccountNotFoundExcpetion

account_num = int(input("Enter your account number: "))
transaction = int(input("Enter 1 to make a deposit and 2 to make a withdrawal: "))

if transaction == 1:
    amount = float(input("Enter the amount you would like to deposit: "))
else:
    amount = float(input("Enter the amount you would like to withdraw: "))

accounts = AccountFactorySingleton()

for account in accounts.available_accounts:
    if account.account_num == account_num:
        account = account
        break

account_numbers = list(
    map(
        lambda account: account.account_num,
        accounts.available_accounts,
    )
)

if account_num not in account_numbers:
    raise AccountNotFoundExcpetion(
        "Invalid account number. Please enter a valid account number"
    )


if transaction == 1:
    account.deposit(amount)
else:
    account.withdraw(amount)
