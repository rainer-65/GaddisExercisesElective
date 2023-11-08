# The SavingsAccount class represents a
# savings account.
import random
from enum import Enum


class SavingsAccount:

    # The __init__ method accepts arguments for the
    # account number, interest rate, and balance.

    def __init__(self, account_num, int_rate, bal):
        self.__account_num = account_num
        self.__interest_rate = int_rate
        self.__balance = bal

    # The following methods are mutators for the
    # data attributes.

    def set_account_num(self, account_num):
        self.__account_num = account_num

    def set_interest_rate(self, int_rate):
        self.__interest_rate = int_rate

    def set_balance(self, bal):
        self.__balance = bal

    # The following methods are accessors for the
    # data attributes.

    def get_account_num(self):
        return self.__account_num

    def get_interest_rate(self):
        return self.__interest_rate

    def get_balance(self):
        return self.__balance


# The MF account represents a managed fund.
# It is a subclass of the SavingsAccount class.

class MF(SavingsAccount):

    # The init method accepts arguments for the
    # account number, interest rate, balance, and
    # risk class.

    def __init__(self, account_num, int_rate, bal, risk_class):
        self.__risk_class = risk_class
        # Call the superclass __init__ method.
        SavingsAccount.__init__(self, account_num, int_rate, bal)

    def set_interest_rate(self):
        super().set_interest_rate(random.choice(range(-10, 10)))

    def get_risk_class(self):
        return self.__risk_class

    def set_risk_class(self, value):
        if value == 1:
            self.__risk_class = "LOW"
        elif value == 2:
            self.__risk_class = "MEDIUM"
        elif value == 3:
            self.__risk_class = "HIGH"
        else:
            pass

    def __str__(self):
        return (f'The MF has the account number {self.get_account_num()} '
                f'with the current balance {self.get_balance()} and \n'
                f'the risk class {self.get_risk_class()} and an interest rate of'
                f' {self.get_interest_rate()}')


class Risk(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3


if __name__ == '__main__':
    fund_one = MF("MF-1234", 0, 50000, Risk.HIGH)
    # Randomize interest rate for MF objects
    fund_one.set_interest_rate()
    fund_one.set_balance(10000)
    fund_one.set_risk_class(3)
    print(str(fund_one))
