from linked_list import *

class HashTable(object):
    """A class that models a basic hash table structure, that stores Records within
    Linked Lists. A HashTable has a scalable property, which modifies how its
    insert method works. A HashTable has a property to record the number of records
    it contains as well."""
    def __init__(self, size, scalable):
        """HashTable(size, scalable)
        Construct a HashTable with the given size and scalable properties."""
        self.__size = size
        self.__scalable = scalable
        self.__num_records = 0
        self.__buckets = []
        for i in range(self.__size):
            self.__buckets.append(LinkedList())
        
    def hashing(self, key):
        """H.hashing(key) --> int
        Returns a value created from the key of the Record."""
        #return hash(key) % self.__size
        if type(key) == str:
            hashVal = 0
            for i, c in enumerate(key):
                hashVal += int(ord(c)) * 31 ** (len(key) -1 - i)
            return hashVal % self.__size
        return key % self.__size
    
    def insert(self, record):
        """H.insert(record) --> None
        Inserts a Record into the HashTable. If the HashTable is scalable, it will
        also double the size of its buckets to decrease its load factor if needed."""
        temp = self.hashing(record.get_key())
        self.__buckets[temp].insert(record)
        self.__num_records += 1        
        if self.__scalable:
            if self.load_factor() > 0.75:
                temp_list = []
                self.__size *= 2
                for i in range(self.__size):
                    temp_list.append(LinkedList())                 
                for i in self.__buckets:
                    while not i.is_empty():
                        first = i.get_first()
                        j = first.get_data()
                        temp = self.hashing(j.get_key())
                        temp_list[temp].insert(j)
                        i.delete(j)        
                self.__buckets = temp_list
               
    def delete(self, record):
        """H.delete(record) --> None
        Deletes the Record given from the HashTable."""
        temp = self.hashing(record.get_key())
        if self.__buckets[temp].contains(record):
            self.__buckets[temp].delete(record)
            self.__num_records -= 1
             
    def get_num_records(self):
        """H.get_num_records() --> int
        Returns the amount of records that the HashTable contains."""
        return self.__num_records
    
    def load_factor(self):
        """H.load_factor() --> float
        Returns the HashTable's load factor which is its number of records        
        divided by the number of buckets it has."""
        return self.__num_records / self.__size
    
    def num_empty(self):
        """H.num_empty() --> int
        Returns the number of empty buckets within the HashTable."""
        count = 0
        for i in self.__buckets:
            if i.size() == 0:
                count += 1
        return count
    
    def largest_bucket(self):
        """H.largest_bucket() --> int
        Returns the size of the largest bucket."""
        size = 0
        for i in self.__buckets:
            if i.size() > size:
                size = i.size()
        return size
    
    def retrieve(self, record):
        """H.retrieve(record) --> Record or None
        Returns a reference to the Record given or None if it is not in the HashTable."""
        temp = self.hashing(record.get_key())
        return self.__buckets[temp].retrieve(record)
    
    def condensed_str(self):
        """H.condensed_str() --> str
        Returns a condensed format version of the HashTable."""
        s = "Size={} Records={} LF={}".format(self.__size, self.__num_records, self.load_factor())
        for i in self.__buckets:
            temp = ":"
            hashtag = i.size()
            for j in range(hashtag):
                temp += "#"
            s += "\n" + temp
        return s
    
    def __str__(self):
        """H.__str__() --> str        
        Returns the string version of the HashTable."""
        s = ""
        for i in self.__buckets:
            temp =""
            while len(temp) + len(str(self.__buckets.index(i))) < 5:
                temp += "_"     
            s += "[{}{}]{}\n".format(temp, self.__buckets.index(i), str(i))
        return s