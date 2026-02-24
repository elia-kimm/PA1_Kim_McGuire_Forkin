# Program: Programming Assignment 1 (Part 1)
# Two-bit binary addition using only logical operations
# Authors: Vanessa McGuire, Sophia Forkin, Elia Kim
# Date Due: March 26, 2026
# INPUTS: A2, A1 (two-bit first binary number)
#         B2, B1 (two-bit second binary number)
# OUTPUTS: Cout, S1, and S2 (three-bit binary result)

"""
This program computes two-bit binary addition strictly using 
only logic gates; AND, OR, and NOT. No arithmetic addition 
is used to compute the sum. 
"""

# adds two, two-bit binary numbers
def sum_two_bit(A2, A1, B2, B1):
    
    # all computed using logic gates which output booleans
    # compute the sum of the first two bits (A1 and B1) 
    S1 = (A1 or B1) and not(A1 and B1)
    # compute carry (if necessary)
    C1 = A1 and B1
  

    # compute the sum of the next two bits (A2 and B2) but
    # do not add the previous carry bit (if it exists) yet
    T = (A2 or B2) and not(A2 and B2)
    # compute carry (if necessary)
    C2 = A2 and B2


    # add first carry (if it exists) into the previous sum, T
    # to finalize the addition in the left column
    S2 = (T or C1) and not(T and C1)
    # compute carry (if necessary)
    C3 = T and C1


    # compute the final carry-out (if necessary)
    Cout = C2 or C3

    # print the final result and convert the
    # booleans into ints
    print(int(Cout), int(S2), int(S1))
    

def main():
    # print to the user the program function and the action
    # that is needed
    print("This is a program to compute two-bit binary addition")
    print("Enter inputs for the four bits (0 or 1)")

    # enter integer (0 or 1) inputs for the bits
    A2 = int(input("A2:"))
    A1 = int(input("A1:"))
    B2 = int(input("B2:"))
    B1 = int(input("B1:"))

    # convert integer inputs into booleans
    A2 = (A2 == 1)
    A1 = (A1 == 1)
    B2 = (B2 == 1)
    B1 = (B1 == 1)

    # compute the sum using binary addition
    sum_two_bit(A2, A1, B2, B1)

main()

