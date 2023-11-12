from exceptions import WithdrawalAmountTooLargeException


class Account:
    customer_num = 0

    """
    During account creation increment customer number

    """

    def __new__(cls, *args, **kwargs):
        cls.customer_num += 1
        return super().__new__(cls)

    """
    An account is initialised with the id
    of the customer opening the account and
    the account number that will be assigned

    :type id: int
    :param id: Faux primary key for account
    :type account_num: int
    :param account_num: The account number
    """

    def __init__(self, id, account_num, balance) -> None:
        self.id = id
        self.account_num = account_num
        self._balance = balance

    @property
    def balance(self):
        """
        Get the current balance
        """
        return self._balance

    @balance.setter
    def balance(self, value):
        raise ValueError("Please make a deposit and then check your account.")

    """
    You can make a withdrawal from an account

    :type amount: float
    :param amount: The amount being withdrawn
    """

    def withdraw(self, amount):
        pass

    """
    Only allow a deposit if the amount is more than R0.0  

    :type amount: float
    :param amount: The amount that is being withdrawn
    """

    def deposit(self, amount) -> None:
        if amount <= 0.0:
            raise ValueError("Please deposit a valid amount.")
        self._balance += amount


class SavingsAccount(Account):

    """
    Create a new empty object and prevent creating
    a savings account if a deposit of R1000 is not made

    :type id: int
    :param id: Faux primary key for account
    :type account_num: int
    :param account_num: The account number
    :type balance: float
    :param balance: The opening balance
    """

    def __init__(self, id, account_num, balance) -> None:
        if int(balance) < 1000:
            SavingsAccount.customer_num -= 1
            raise ValueError(
                "You must deposit at least R1000 to open a savings account."
            )
        super().__init__(id, account_num, balance)

    """
    Make a withdrawal and reject a withdrawal 
    if the remaining balance is going to be less than R1000

    :type amount: float
    :param amount: The amount that is being withdrawn
    """

    def withdraw(self, amount) -> None:
        if int(self.balance - amount) < 1000:
            raise WithdrawalAmountTooLargeException(
                "The withdrawal amount puts the balance under R1000."
            )
        self.balance -= amount


class CurrentAccount(Account):

    """
    Create a new empty object and prevent creating
    a savings account if a deposit of R1000 is not made

    :type id: int
    :param id: Faux primary key for account
    :type account_num: int
    :param account_num: The account number
    :type balance: float
    :param balance: The opening balance
    """

    def __init__(self, id, account_num, balance=0, overdraft=100000) -> None:
        if overdraft > 100000:
            CurrentAccount.customer_num -= 1
            raise ValueError(
                "The overdraft should not be more than R100000 in a current account."
            )
        super().__init__(id, account_num, balance)
        self._overdraft = overdraft

    @property
    def overdraft(self):
        """
        Get overdraft
        """
        return self._overdraft

    @overdraft.setter
    def overdraft(self, value):
        raise ValueError("You can't change the overdraft")

    """
    Make a withdrawal and reject a withdrawal 
    if the sum of the remaining balance and overdraft  
    is less than the amount being withdrawn

    :type amount: float
    :param amount: The amount that is being withdrawn
    """

    def withdraw(self, amount) -> None:
        if amount > (self._balance + self._overdraft):
            raise WithdrawalAmountTooLargeException(
                "The withdrawal amount cannot be larger than the sum of the balance and overdraft"
            )
        self._balance -= amount
