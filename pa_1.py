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

# Part 2

# full adder
def add_bits(a,b,carry):
    temp = (a or b) and not (a and b)
    sum_bits = (temp or carry) and not (temp and carry)
    carryy = (a and b) or (carry and temp)
    return sum_bits, carryy

# Convert to 32 bits
def binary(numb):
    arr = [0]*32
    pos = 31
    while numb > 0 and pos >= 0:
        arr[pos] = numb % 2
        numb = numb //2
        pos -= 1
    return arr

# Addition
def add_numbs(A,B):
    result = [0]*32
    carry0 = False
    result[31], carry1 = add_bits(A[31], B[31], carry0)
    result[30], carry2 = add_bits(A[30], B[30], carry1)
    result[29], carry3 = add_bits(A[29], B[29], carry2)
    result[28], carry4 = add_bits(A[28], B[28], carry3)
    result[27], carry5 = add_bits(A[27], B[27], carry4)
    result[26], carry6 = add_bits(A[26], B[26], carry5)
    result[25], carry7 = add_bits(A[25], B[25], carry6)
    result[24], carry8 = add_bits(A[24], B[24], carry7)
    result[23], carry9 = add_bits(A[23], B[23], carry8)
    result[22], carry10 = add_bits(A[22], B[22], carry9)
    result[21], carry11 = add_bits(A[21], B[21], carry10)
    result[20], carry12 = add_bits(A[20], B[20], carry11)
    result[19], carry13 = add_bits(A[19], B[19], carry12)
    result[18], carry14 = add_bits(A[18], B[18], carry13)
    result[17], carry15 = add_bits(A[17], B[17], carry14)
    result[16], carry16 = add_bits(A[16], B[16], carry15)
    result[15], carry17 = add_bits(A[15], B[15], carry16)
    result[14], carry18 = add_bits(A[14], B[14], carry17)
    result[13], carry19 = add_bits(A[13], B[13], carry18)
    result[12], carry20 = add_bits(A[12], B[12], carry19)
    result[11], carry21 = add_bits(A[11], B[11], carry20)
    result[10], carry22 = add_bits(A[10], B[10], carry21)
    result[9], carry23 = add_bits(A[9], B[9], carry22)
    result[8], carry24 = add_bits(A[8], B[8], carry23)
    result[7], carry25 = add_bits(A[7], B[7], carry24)
    result[6], carry26 = add_bits(A[6], B[6], carry25)
    result[5], carry27 = add_bits(A[5],B[5], carry26)
    result[4], carry28 = add_bits(A[4], B[4], carry27)
    result[3], carry29 = add_bits(A[3], B[3], carry28)
    result[2], carry30 = add_bits(A[2], B[2], carry29)
    result[1], carry31 = add_bits(A[1], B[1], carry30)
    result[0], carry32 = add_bits(A[0], B[0], carry31)
    return result, carry32

def invert(B):
    return[
        int(not B[0]), int(not B[1]), int(not B[2]]0, int(not B[3]), int(not B[4]), int(not B[5]),
        int(not B[6]), int(not B[7]), int(not B[8], int(not B[9], int(not B[10], int(not B[11]),
        int(not B[12]), int(not B[13]), int(not B[14]), int(not B[15]), int(not B[16]), int(not B[17]),
        int(not B[18]), int(not B[19]), int(not B[20]), int(not B[21]), int(not B[22]), int(not B[23]),
        int(not B[24]), int(not B[25]), int(not B[26]), int(not B[27]), int(not B[28]), int(not B[29]),
        int(not B[30]), int(not B[31]) ]

def add1(B):
        1 = [0]*31 + [1]
        result, carry = add_numbs (B, one)
        return result

def subtract(A, B):
              B_inv = invert(B)
              B_twos = add1(B_inv)
              result, carry = add_numbs(A, B_twos)
            return result

def to_decimal(B):
            value = 0
            power = 1

                    for i in range(31, -1 , -1):
                        if B[i] == 1:
                            value += power
                        power *=2
                    return value
