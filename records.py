class Record(object):
    """A simple class that is used to store a value in a HashTable."""
    def __init__(self, key):
        """Record(key)
        Construct a Record which contains the given key.""" 
        self.__key = key
    
    def get_key(self):
        """R.get_key() --> str
        Returns its key property."""
        return self.__key
    
    def __eq__(self, second):
        """R = second --> bool
        Returns if the Record has the same key as second."""
        if second != None:
            return self.get_key() == second.get_key()
            
    def __str__(self):
        """R.__str__() --> str
        Returns the string version of Record."""
        return str(self.__key)
    
class Word_Record(Record):
    """A customized Record class where the key value is a word. Also has a count
    property which is the number of times that word has been found."""
    def __init__(self, key):
        """Word_Record(key)
        Contruct a Word_Record which contains the given word."""
        self.__count = 1
        Record.__init__(self, key)
        
    def add_one(self):
        """W.add_one --> None
        Adds one to the Word_Record's count property."""
        self.__count += 1
        
    def __str__(self):
        """W.__str__() --> str
        Returns the string version of Word_Record."""
        return "{}:{}".format(Record.__str__(self), self.__count)
        
class IP_Record(Record):
    """A customized Record class where the key value is an IP address. Also has
    a list of web pages the IP has visited."""
    def __init__(self, ip):
        """IP_Record(ip)
        Construct an IP_Record which contains the given IP address."""
        self.__pages = []
        Record.__init__(self, ip)
        
    def add_pages(self, page):
        """I.add_pages(page) --> None
        Adds the given page to the IP_Record's list of visited pages."""
        self.__pages.append(page)
        
    def __str__(self):
        """I.__str__() --> str
        Returns the string version of IP_Record."""
        return "{}:{}".format(Record.__str__(self), self.__pages).replace("'", "")