#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * (length - 1)
    
    for my_tick in tickets:
        # save tickets to hash table using their source as key and destination as value
        hash_table_insert(hashtable, my_tick.source, my_tick.destination)

    current_location = "NONE"

    for i in range(length-1):
        # retrieve destination value based on current location and set it to i pos in list
        route[i] = hash_table_retrieve(hashtable, current_location)
        # set current location to destination and iterate again
        current_location = route[i]

    return route
