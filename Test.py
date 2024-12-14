import unittest
def multiply(a, b):
    return a * b

def reverse_list(input_list):
    reversed_list = input_list[::-1]
    return reversed_list


def calculate_discount(price, discount_percentage):
    if discount_percentage < 0 :
        raise ValueError ("Discount cant be negative value")
    if discount_percentage > 100 :
        raise ValueError ("Discount cant be greater than 100%")
    if price == 0 or discount_percentage ==0 :
        raise ValueError ("Discount and price cant equal 0")
    return (1-discount_percentage/100)*price

def test_multiply():
    assert multiply(5,5) == 25
    assert multiply(5,0) == 0
    assert multiply(-5,-5) == 25

def test_reverse_list():
    assert reverse_list([1,2,3,4]) == [4,3,2,1]
    assert reverse_list([]) == []
    assert reverse_list([50]) == [50]

def test_discount(): 
    assert calculate_discount(100,10) == 90
    with unittest.TestCase().assertRaises(ValueError):
        calculate_discount(100,-10)
        calculate_discount(0,10)
        calculate_discount(100,110)

class MathOperations():
    def is_prime(n):
        if n <=1 :
            return False
        for i in range(2,int(n**0.5)+1):
            if n % i ==0:
                return False
        return True

    def factorial(n):
        if n<0 :
            raise ValueError("Cant get factorial of neagtive number")
        if n==0 or n==1 :
            return 1
        else :
            return n*MathOperations.factorial(n-1)

def test_prime():
    assert MathOperations.is_prime(7) == True
    assert MathOperations.is_prime(7) == False
    assert MathOperations.is_prime(-29) == False
def test_factorial():
    assert MathOperations.factorial(3) == 6
    assert MathOperations.factorial(10) == 1
    with unittest.TestCase().assertRaises(ValueError):
        MathOperations.factorial(-1)
    print("All tests passed")

def test_all():
    test_multiply()
    test_reverse_list()
    test_discount()
    test_prime()    
    test_factorial()

test_all()