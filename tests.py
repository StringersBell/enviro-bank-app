from accounts import SavingsAccount, CurrentAccount
from factory import AccountFactorySingleton


my_accounts = AccountFactorySingleton()

print(my_accounts.available_accounts)

# savings_1 = SavingsAccount(id=101, account_num=1, balance=2000)

# print(savings_1.balance)
# print(savings_1.customer_num)

# savings_2 = SavingsAccount(id=102, account_num=2, balance=5000)
# print(savings_2.balance)
# print(savings_2.customer_num)

# current_1 = CurrentAccount(id=103, account_num=3, balance=1000, overdraft=10000)
# print(current_1.balance)
# print(current_1.customer_num)
# # current_1.balance = 4550


# current_2 = CurrentAccount(id=102, account_num=2, balance=-5000, overdraft=20000)
# print(current_2.balance)
# print(current_2.customer_num)
# current_2.withdraw(15000)
# print(current_2.balance)
# # current_2.balance = 4553
