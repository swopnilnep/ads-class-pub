'''Banking classes implementation'''
#!/usr/bin/env python3

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
    
    @street.setter
    def street(self, street_name):
        self._street = street_name

    # City 
    @property
    def city(self):
      return self._city

    @city.setter
    def city(self, city_name: str):
        self._city = city_name   

    # State
    @property
    def state(self):
      return self._state

    @state.setter
    def state(self, state_name: str):
      self._state = state_name 

    # Zip
    @property
    def zip(self):
      return self._zip
    
    @zip.setter
    def zip(self, zip_code: int):
      self._zip = zip_code

    def __eq__(self, other: object):
        '''Compare 2 addresses'''
        return self.street == other.street \
        and self.city == other.city \
        and self.state == other.state \
        and self.zip == other.zip

    def __str__(self):
        '''__str method'''
        return "{}, {}, {} {}".format(self.street, self.city, self.state, self.zip)


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
    @property
    def address(self):
        return self._address

    @address.setter    
    def move(self, new_address: object):
        '''Change address'''
        self._address = new_address 

    def __str__(self):
        '''__str'''
        return "{} ({}) {}".format(self.name, self.dob, self.address) 

class Account(ABC):
    '''Account class'''
    @abstractmethod
    def __init__(self, owner_init: object, balance_init: float=0):
        '''Constructor'''
        raise NotImplementedError

    # TODO: Implement data members as properties

    def deposit(self, amount: float):
        '''Add money'''
        raise NotImplementedError

    def close(self):
        '''Close account'''
        raise NotImplementedError

    def __str__(self):
        '''__str__'''
        raise NotImplementedError


class CheckingAccount(Account):
    '''CheckingAccount class'''
    def __init__(self, owner_init: object, fee_init: float, balance_init: float=0):
        '''Constructor'''
        raise NotImplementedError

    def process_check(self, amount: float):
        '''Process a check'''
        raise NotImplementedError

    def __str__(self):
        '''__str__'''
        raise NotImplementedError


class SavingsAccount(Account):
    '''CheckingAccount class'''
    def __init__(self, owner_init: object, interest_rate_init: float, balance_init: float=0):
        '''Constructor'''
        raise NotImplementedError

    def yield_interest(self):
        '''Yield annual interest'''
        raise NotImplementedError

    def __str__(self):
        '''__str__'''
        raise NotImplementedError


def main():
    swopnil = Address("700 College Drive", "Decorah", "IA", "52101")

if __name__=="__main__":
    main()