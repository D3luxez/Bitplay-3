#program to swap two numbers without using third variables
def swap1(a,b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print("after swaping: a = ",a, "b = ",b)
swap1(1,2)