'''Implementation of the Map ADT as HashTable'''

class HashTable:
    def __init__(self, size_init: int=16):
        '''Constructor'''

        self._size = size_init
        self._keys = [None] * self._size
        self._values = [None] * self._size

    def __getitem__(self, key: int):
        '''__getitem__'''
        return self.get(key)

    def __setitem__(self, key: int, value):
        '''__setitem__'''
        self.put(key, value)
    
    def __len__(self):
        '''__len__'''
        return sum(x is not None for x in self._keys)
    
    def __contains__(self, key):
        '''__contains__'''
        return key in self._keys

    def __str__(self):
        '''__str__'''
        out_str = ""
   
        for key, value in zip(self._keys, self._values):
            if key != None:
                key_str = str(key)
                value_str = str(value)

                if key_str.isdigit(): key_repr = key_str
                else: key_repr = "'{}'".format(key_str)

                if value_str.isdigit(): value_repr = value_str
                else: value_repr = "'{}'".format(value_str)

                unit = "{}: {}, ".format(key_repr, value_repr)

                out_str += unit

        out_str = "{" + out_str[0:-2] + "}"
        return out_str 

    def _hash(self, key: int, size: int):
        '''Simple hash function'''
        return key % size

    def _rehash(self, old_hash: int, size: int, step: int=1):
        '''Simple or quadratic rehash'''
        return (old_hash + step**2)%size

    def put(self, key: int, value):
        '''Add or update an item'''
        hashvalue = self._hash(key,len(self._keys))

        if self._keys[hashvalue] == None:
            self._keys[hashvalue] = key
            self._values[hashvalue] = value
        else:
            if self._keys[hashvalue] == key:
                self._values[hashvalue] = value  #replace
            else:
                nextkey = self._rehash(hashvalue,len(self._keys))
                rehash_step = 1
                while self._keys[nextkey] != None and self._keys[nextkey] != key and rehash_step and rehash_step < self._size:
                    rehash_step += 1

                    nextkey = self._rehash(hashvalue,len(self._keys), rehash_step)

                if rehash_step >= self._size: raise Exception("Hash Table is full")

                if self._keys[nextkey] == None:
            
                    self._keys[nextkey]=key
                    self._values[nextkey]=value
                else:
                    self._values[nextkey] = value #replace

    def get(self, key: int):
        '''Retrieve an item'''
        startkey = self._hash(key,len(self._keys))

        data = None
        stop = False
        found = False
        position = startkey
        rehash_step = 0
        while self._keys[position] != None and  \
                            not found and not stop:
            if self._keys[position] == key:
                found = True
                data = self._values[position]
            else:
                rehash_step += 1
                position=self._rehash(startkey,len(self._keys), rehash_step)
                if position == startkey:
                    stop = True
        return data

    def keys(self):
        '''Return all keys'''
        return [x for x in self._keys if x]

    def values(self):
        '''Return all values'''
        return [x for x in self._values if x]

    def items(self):
        '''Return all items'''
        out_list = []
        for key,value in zip(self._keys, self._values):
            if key != None:
                unit = key,value
                out_list.append(unit)
        return out_list

def main():

    the_map = HashTable(11)
    the_map2 = HashTable(10)

    map_test_items = {
            54: "aardvark",
            26: "beaver",
            93: "cheetah",
            17: "dolphin",
            77: "elephant",
            31: "flamingo",
            44: "goat",
            55: "hippo",
            20: "iguana"
            }
    
    for item in map_test_items.items():
        the_map.put(item[0], item[1])

    the_map[21] = "jackal"
    assert the_map[21] == "jackal"
    the_map.put(18, "koala")
    the_map.get(18) == "koala"
    # assert str(the_map) == "{77: 'elephant', 44: 'goat', 20: 'iguana', 55: 'hippo', 26: 'beaver', 93: 'cheetah', 17: 'dolphin', 18: 'koala', 21: 'jackal', 31: 'flamingo', 54: 'aardvark'}"
    # print(the_map)
    # print("{77: 'elephant', 44: 'goat', 20: 'iguana', 55: 'hippo', 26: 'beaver', 93: 'cheetah', 17: 'dolphin', 18: 'koala', 21: 'jackal', 31: 'flamingo', 54: 'aardvark'}")

    the_map[54] = "anteater"
    print(the_map[54])

    the_map.put(55, "hyena")
    print(the_map[55])

    print(the_map)
    print("{77: 'elephant', 44: 'goat', 20: 'iguana', 55: 'hyena', 26: 'beaver', 93: 'cheetah', 17: 'dolphin', 31: 'flamingo', 54: 'anteater'}")

if __name__=="__main__":
    main()