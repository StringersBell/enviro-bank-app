from accounts import SavingsAccount, CurrentAccount


class AccountFactorySingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    """
    Pre-populate with some hardcoded accounts
    
    """

    def __init__(self) -> None:
        self._available_accounts = [
            SavingsAccount(id=101, account_num=1, balance=2000),
            SavingsAccount(id=102, account_num=2, balance=5000),
            CurrentAccount(id=103, account_num=3, balance=1000, overdraft=10000),
            CurrentAccount(id=104, account_num=4, balance=-5000, overdraft=20000),
        ]

    @property
    def available_accounts(self):
        """
        Get list of hardcoded accounts
        """
        return self._available_accounts
