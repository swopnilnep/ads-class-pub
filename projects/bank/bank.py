'''Banking classes implementation'''
#!/usr/bin/env python3
# Swopnil N. Shrestha

from abc import ABC, abstractmethod


class Address:
    '''Address class'''
    def __init__(self, street_init: str, city_init: str, state_init: str, zip_init: str):
        '''__init__'''
        self._street = street_init
        self._city = city_init
        self._state = state_init
        self._zip = zip_init

    # Street 
    @property
    def street(self):
        return self._street

    # City 
    @property
    def city(self):
      return self._city

    # State
    @property
    def state(self):
      return self._state

    # Zip
    @property
    def zip(self):
      return self._zip
    
    def __eq__(self, other: object):
        '''Compare 2 addresses'''
        return self.street == other.street \
        and self.city == other.city \
        and self.state == other.state \
        and self.zip == other.zip

    def __str__(self):
        '''__str method'''
        return "{}\n{}, {} {}".format(self.street, self.city, self.state, self.zip)

class Customer:
    '''Customer class'''
    def __init__(self, name_init: str, dob_init: str, address_init: object):
        '''Constructor'''
        self._name = name_init
        self._dob = dob_init
        self._address = address_init

    # Name
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name: str):
        self._name = name

    # Date of Birth
    @property
    def dob(self):
        return self._dob
    
    @dob.setter
    def dob(self, dob: str):
        self._dob = dob

    # Address
    def address(self):
        return self._address
   
    def move(self, new_address: object):
        '''Change address'''
        self._address = new_address 

    address = property(address, move)

    def __str__(self):
        '''__str'''
        return "{} ({})\n{}".format(self.name, self.dob, self.address) 

class Account(ABC):
    '''Account class'''
    @abstractmethod
    def __init__(self, owner_init: object, balance_init: float=0):
        '''Constructor'''
        self._owner = owner_init
        self._balance = balance_init

    @property
    def balance(self):
        return self._balance

    @property
    def owner(self):
        return self._owner

    @balance.setter
    def balance(self, value: float):
        self._balance = value 

    # Add money 
    def deposit(self, amount: float):
        '''Add money'''
        if amount < 0: raise ValueError("Must deposit positive amount")
        elif amount > 0: self._balance += amount 
        

    def close(self):
        '''Close account'''
        self._balance = 0
   

    def __str__(self):
        '''__str__'''
        return "Owner: {}\n".format(self._owner) + "Balance: {}".format(self.balance)

class CheckingAccount(Account):
    '''CheckingAccount class'''
    def __init__(self, owner_init: object, fee_init: float, balance_init: float=0):
        super().__init__(owner_init, balance_init)
        self._fee = fee_init
        
    def process_check(self, amount: float):
        '''Process a check'''
        if self.balance < amount:
            self.balance -= self._fee
        
        else:
            self._balance = self._balance - amount

    def __str__(self):
        '''__str__'''
        return "Checking account\n" + "Owner: {}\n".format(self._owner) + "Balance: {:.2f}".format(self.balance)


class SavingsAccount(Account):
    '''CheckingAccount class'''
    def __init__(self, owner_init: object, interest_rate_init: float, balance_init: float=0):
        '''Constructor'''
        super().__init__(owner_init, balance_init)
        self._interest_rate = interest_rate_init

    def yield_interest(self):
        '''Yield annual interest'''
        self._balance = self._balance + self._balance * (self._interest_rate/100)
        return self._balance

    def __str__(self):
        '''__str__'''
        return "Savings account\n" + "Owner: {}\n".format(self._owner) + "Balance: {:.2f}".format(self.balance)


def main():
    address1 = Address("700 College Dr", "Decorah", "IA", "52101")
    address2 = Address("700 College Drive", "Decorah", "IA", "52101")
    address3 = Address("700 College Drive", "Decorah", "IA", "52101")

    customer1 = Customer("John Doe", "1861-09-01", address1) 
    customer2 = Customer("Swopnil Shrestha", "1980-06-06", address2) 
    checking1 = CheckingAccount(customer1, 100, 200.00)
    saving1 = SavingsAccount(customer1, 0.05, 500.00)

    # Address check
    # print(address1.street)
    # print(address1.city)
    # print(address1.state)
    # print(address1.zip)
    
    # Address string check
    # print(str(address1).strip() == ('700 College Dr\nDecorah, IA 52101'))
    # print(address1)

    # Address eq check
    # print(address1 == address2) # False
    # print(address2 == address3) # True
    # print(address1 != address2) # True
    # print(address1 is not address2) # True 

    # Customer string check 
    # Same error with address 

    # Customer Move
    # customer1.move(address2)
    # print(customer1.address)

    # Test Account
    # print(checking1.owner)
    # print(checking1.owner.address)
    # print(checking1.balance)
    # print(checking1)
    
    # Test account Deposit
    # checking1.balance = 100
    # print(checking1.balance)
    # checking1.deposit(60)
    # print(checking1.balance)
    
    # Test account deopsit error
    # checking1.deposit(-1)
    # print(checking1.balance)

    # Test account close
    # checking1.close()
    # print(checking1.balance)
    # saving1.close()
    # print(saving1.balance)
    
    # checking1.close()
    # checking1.deposit(2000)
    # print(checking1.balance)
    # checking1.process_check(5000)
    # print(checking1.balance)
    # checking1.process_check(-5000)

    # checking1.balance = 100.0
    # string_check = (str(checking1))
    # check = ('Checking account\n' +'Owner: John Doe (1861-09-01)\n' + '700 College Dr\n' + 'Decorah, IA 52101\n' + 'Balance: 100.00')
    # print(string_check == check)

    # Yield Interest
    # saving1.balance = 100
    # print(saving1.balance)
    # saving1.yield_interest()
    # print(saving1.balance)

    # Test Savings Str
    print(saving1)

    '''
    * test address str # Implemented
    * test customer str # Implemented 
    * test customer move # Implemented 
    * test account # Implemented 
    * test account deposit # Implemented
    * test checking process
    * test checking str
    * test savings yield interest
    * test savings str
    '''


if __name__=="__main__":
    main()