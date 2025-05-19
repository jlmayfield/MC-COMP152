import pytest
from typing import List


## Examples to help get you started 

def total(alon : List[int]) -> int:
    """
    compute the sum of all the numbers in alon 

    Parameters:
    alon : List[int] - a list of integers

    Return
    int - sum of all elements in alon
    """
    tot = 0 # accumulator variable for total/sum
    for n in alon: #iterate: for each int n in List[int] alon...
        tot += n #accumulate n into total
    return tot # return accumulated value after iteration is complete 

def test_total():
    assert total([]) == 0
    assert total([3]) == 3
    assert total([1,3,5]) == 9

def multby(alon : List[int], mult : int)-> List[int]:
    """
    Compute a list that contains the elements of alon multiplied (or scaled)
    by mult.  

    Parameters:
    alon : List[int] - the list of numbers
    mult : int - the scalar values

    Return: 
    List[int] - values of alon multipled by mult
    """
    scaled = []
    for n in alon:
        scaled.append(n*mult)
    return scaled

def test_multby():
    assert multby([],3) == []
    assert multby([4],4) == [16]
    assert multby([1,3,5],2) == [2,6,10]

def multby_ip(alon : List[int], mult : int) -> None:
    """
    scale all the values in alon in place. The contents of alon are 
    modified by this function.

    Parameters:
    alon : List[int] - the list of numbers
    mult : int - the scalar 

    Return:
    None
    """
    for i in range(0,len(alon)):
        alon[i] = alon[i] * mult
    return 

def test_multbyip():
    l = []
    multby_ip(l,3)
    assert l == []
    l = [4]
    multby_ip(l,2)
    assert l == [8]
    l = [2,4,6]
    multby_ip(l,5)
    assert l == [10,20,30]


## YOUR CODE BELOW HERE






## YOUR CODE ABOVE HERE

if __name__ == '__main__':
    pytest.main(["lab1.py"]) #run all tests in lab1.py