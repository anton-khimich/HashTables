from hash_table import *
from linked_list import *
from records import *

def default_reader(list, hashtable):
    """default_reader(list, HashTable) --> None
    A function that takes a list and inserts each key(str) as Records into the
    given HashTable."""
    for i in list:
        if hashtable.retrieve(i) == None:
            hashtable.insert(i)

def word_reader(filename, hashtable):
    """word_reader(str, HashTable) --> None
    A function that takes the given filename and inserts each key(word) and their
    count as Word_Records into the given HashTable."""
    string = open(r"{}".format(filename))
    temp = []
    for line in string:
        temp += line.split()
    for i in temp:
        wr = Word_Record(i)
        if hashtable.retrieve(wr) == None:
            hashtable.insert(wr)
        else:
            hashtable.retrieve(wr).add_one()
        
def ip_reader(filename, hashtable):
    """ip_reader(str, HashTable) --> None
    A function that takes the given filename and inserts each key(IP address) and 
    their pages visited as IP_Records into the given HashTable."""
    string = open(r"{}".format(filename))
    for line in string:
        ir = IP_Record(line.split()[0].strip(":"))
        if hashtable.retrieve(ir) == None:
            ir.add_pages(line.split()[1])
            hashtable.insert(ir)
        else:
            hashtable.retrieve(ir).add_pages(line.split()[1])
        
    

#if __name__ == "__main__":
    #ht = HashTable(11000, False)
    #ip_reader("ip_clicks.txt", ht)
    #word_reader("wordy_file.txt", ht)
    #print(ht)