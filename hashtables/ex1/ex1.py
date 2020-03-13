#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)

def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(length)
    
    for i in range(length):
        # loop over the weight items
        # set get weights to value at weight limit minus current weight
        get_weights =  hash_table_retrieve(ht, limit - weights[i])
        # get current item in the hash table
        if get_weights is not None: 
            # if the item is not none then set the answer to the current index and get weights
            answer = (i, get_weights)
            return answer
        else: 
            hash_table_insert(ht, weights[i], i)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

