#TypeHinting

from typing import List 

## New feature in python 3.5

## tell python to accept a list and return a float
def list_average(sequence: list) -> float:
    return sum(sequence)/len(sequence)

print(list_average([2,3,4,5]))



