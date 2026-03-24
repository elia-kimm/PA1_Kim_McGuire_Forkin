# Program: Programming Assignment 1 (Part 1)
# Two-bit binary addition using only logical operations
# Authors: Vanessa McGuire, Sophia Forkin, Elia Kim
# Date Started: Febraury 23, 2026
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

    return Cout, S2, S1


# Part 2

# full adder
# We want to add two single bits (A and B) as well as a carry using logical gates. This 
# returns the sum of the bits and the carry out portion. 
# The purpose of the sum_bits is to be stored in the results list
# Carry out is still a boolean, so shan't be an int
def add_bits(a, b, carry):
    # Logic : (a XOR b) XOR carrry
    temp = (a or b) and not (a and b)
    sum_bits = (temp or carry) and not (temp and carry)
    
    # carry logic : (a AND b) OR (carry AND temp)
    carry_out = (a and b) or (carry and temp)
    
    return int(sum_bits), carry_out

# Convert to 32 bits
# We want to convert a positive integer into a 32 bit binary array. 
# Each index represents a bit
def binary(numb):
    
    is_negative = numb < 0
    n = abs(numb)
    
    # Start the 32 bit array with 0s
    arr = [0] * 32
    
    # Start filling in from the right bit
    pos = 31
    # Loop until the array is finished
    while n > 0 and pos >= 0:
        # Store the remainder 
        arr[pos] = n % 2
        # Divide by 2 to shift the number right
        n = n // 2
        # Move left
        pos -= 1
        
    if is_negative:
        # Conver the positive array to negative using our logic tools
        inverted = invert(arr)
        arr = add_numbs(inverted, binary(1))[0]
        
    return arr

# Addition
def add_numbs(A, B):
    # Start the array with 0s
    result = [0] * 32
    
    #The carry in is 0
    carry0 = False
    
    # We manually compute each bit starting from 31 to 0
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
    result[5], carry27 = add_bits(A[5], B[5], carry26)
    result[4], carry28 = add_bits(A[4], B[4], carry27)
    result[3], carry29 = add_bits(A[3], B[3], carry28)
    result[2], carry30 = add_bits(A[2], B[2], carry29)
    result[1], carry31 = add_bits(A[1], B[1], carry30)
    result[0], carry32 = add_bits(A[0], B[0], carry31)
    
    return result, carry32
    
"""def add_numbs(A, B) :
    # array of 0s w/ 32 slots so if addition only affects the right most
    #bits, the other bits stay 0.
    result = [0] * 32
    curr_carry = False
    # Used a loop to "chain" 32 adders together
    for i in range(31, -1, -1) :
        # pass bitand carry from prev iteration
        # sum_bits and carry_out
        bit_sum, curr_carry = add_bits(A[i] == 1, B[i] == 1, curr_carry)
        result[i] = bit_sum
    # curr_carry is now the carry out of the 32nd bit (Overflow)
    return result, curr_carry"""

# Invert all the bits in array B
def invert(B):
    return[
        int(not B[0]), int(not B[1]), int(not B[2]), int(not B[3]), int(not B[4]), int(not B[5]),
        int(not B[6]), int(not B[7]), int(not B[8]), int(not B[9]), int(not B[10]), int(not B[11]),
        int(not B[12]), int(not B[13]), int(not B[14]), int(not B[15]), int(not B[16]), int(not B[17]),
        int(not B[18]), int(not B[19]), int(not B[20]), int(not B[21]), int(not B[22]), int(not B[23]),
        int(not B[24]), int(not B[25]), int(not B[26]), int(not B[27]), int(not B[28]), int(not B[29]),
        int(not B[30]), int(not B[31]) 
    ]

"""def add1(B):
        1 = [0]*31 + [1]
        result, carry = add_numbs (B, one)
        return result"""
              
#Invert B, add 1, and add A plus negative B
# our code is robust enough to handle smaller numbers first.
def subtract(A, B):
    # invert b, add 1 to get the Two's complement, then A + (-B)
    B_inv = invert(B)
    one_binary = binary(1)
    
    # must get rid of the carry .
    B_twos = add_numbs(B_inv, one_binary)[0]  #add1(B_inv)
    
    #result, carry = add_numbs(A, B_twos)
    result = add_numbs(A, B_twos)[0]
    
    return result, B_twos

# This is to check the 32nd bit.
def to_decimal(B):
    # Pre-calculated bit weights for a 32-bit signed integer
    # Index 0 is the sign bit with negative weight (look at lines 108, 115)
    weights = [
        2147483648, 1073741824, 536870912, 268435456, 134217728, 67108864, 
        33554432, 16777216, 8388608, 4194304, 2097152, 1048576, 524288, 
        262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 
        256, 128, 64, 32, 16, 8, 4, 2, 1
    ]
    
    value = 0
    power = 1
    
    # Add weights for bits 1 through 31
    for i in range(1, 32):
        if B[i] == 1:
            value += weights[i]
            
    # Handle the Sign Bit (Index 0) using Two's Complement logic [cite: 112, 115]
    if B[0] == 1:
        value -= weights[0]
        
    return value


def check_overflow(A, B, Res):
    # Overflow if signs of A and B are same, but Result sign is different
    # Res[0] is the sign bit (1 for neg, 0 for pos)
    a_sign = A[0]
    b_sign = B[0]
    res_sign = Res[0]
    
    # (A_sign == B_sign) AND (A_sign != Result_sign)
    overflow = (a_sign == b_sign) and (a_sign != res_sign)
    
    return overflow

def main():
    # Part 1
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
    Cout, S2, S1 = sum_two_bit(A2, A1, B2, B1)
    
    # convert Part 1 inputs into base 10
    val_a = (int(A2) * 2) + int(A1)
    val_b = (int(B2) * 2) + int(B1)
    # multiply by the weight of the bits (Cout=4, S2=2, S1=1)
    val_sum = (int(Cout) * 4) + (int(S2) * 2) + int(S1)

    # print Part 1 result
    # print the final result and convert the
    # booleans into ints
    print(f"Binary: {int(Cout)}{int(S2)}{int(S1)}")
    print(f"Base 10: {val_a} + {val_b} = {val_sum}")

    # Part 2
    print("\n--- PART 2: 32-BIT SYSTEM ---")
    val1 = int(input("Enter first base-10 number: "))
    val2 = int(input("Enter second base-10 number: "))
    op = input("Add or Subtract? (+/-): ")

    A_bin = binary(val1)
    B_bin = binary(val2)

    if op == '+':
        res, carry_out = add_numbs(A_bin, B_bin)
        overflow = check_overflow(A_bin, B_bin, res)
        if overflow:
            print("ERROR: Overflow!")
        else:
            print(f"Binary: {''.join(map(str, res))}")
            print(f"Base 10: {to_decimal(res)}")
    else:
        # User ensures A > B as per prompt instructions
        res, B_twos = subtract(A_bin, B_bin)
        overflow = check_overflow(A_bin, B_twos, res)
        if overflow:
            print("ERROR: Overflow!")
        else:
            print(f"Binary: {''.join(map(str, res))}")
            print(f"Base 10: {to_decimal(res)}")

main()

"""def run_tests():
    # Test cases: (Value 1, Value 2, Operation)
    test_cases = [
        (500, 500, "+"),                # 1000
        (64, 32, "+"),                  # 96
        (2000000000, 1000000000, "+"),  # overflow 
        (2147483647, 1, "+"),           # overflow
        (-1000, -2000, "+"),            # -3000
        
        (800000, 100000, "-"),          # 700,000
        (100000, 800000, "-"),          # -700,000
        (0, 500, "-"),                  # -500
        (-1000, -500, "-"),             # -500
        (-500, -1000, "-"),             # 500
        (2000000000, -2000000000, "-"), # Overflow
        (-2000000000, 2000000000, "-")  # Overflow
    ]

    print(f"{'Operation':<20} | {'Binary Result':<34} | {'Base 10':<15} | {'Status'}")
    print("-" * 85)

    for v1, v2, op in test_cases:
        A_bin = binary(v1)
        B_bin = binary(v2)
        
        if op == "+":
            res = add_numbs(A_bin, B_bin)[0]
            is_overflow = check_overflow(A_bin, B_bin, res)
        else:
            res, B_twos = subtract(A_bin, B_bin)
            # For subtraction (A - B), we check overflow as if adding A + (-B)
            # So we compare A and the Two's Complement of B
            is_overflow = check_overflow(A_bin, B_twos, res)

        # Formatting for the table
        bin_str = "".join(map(str, res))
        val_10 = to_decimal(res)
        status = "OVERFLOW" if is_overflow else "OK"
        
        print(f"{v1} {op} {v2:<10} | {bin_str} | {val_10:<15} | {status}")

if __name__ == "__main__":
    # Run Part 1 manually once
    print("--- PART 1 TEST (1 + 1) ---")
    sum_two_bit(False, True, False, True) 
    
    print("\n--- PART 2 AUTOMATED TESTS ---")
    run_tests()"""

"""def run_part1_tests():
    # Required Part 1 test cases from the assignment
    # Format: (A2, A1, B2, B1)
    test_cases = [
        (0,0,0,0),    # 00 + 00 = 000
        (0,1,0,0),    # 01 + 00 = 001
        (0,1,0,1),    # 01 + 01 = 010 
        (1,0,0,1),    # 10 + 01 = 011
        (1,0,1,0),    # 10 + 10 = 100
    ]

    print(f"{'Input A':<8} | {'Input B':<8} | {'Binary Result':<14} | {'Base 10'}")
    print("-" * 55)

    for A2, A1, B2, B1 in test_cases:
        # Convert integers into booleans 
        A2_bool = (A2 == 1)
        A1_bool = (A1 == 1)
        B2_bool = (B2 == 1)
        B1_bool = (B1 == 1)

        # Compute Part 1 sum
        Cout, S2, S1 = sum_two_bit(A2, A1, B2, B1)

        # Convert Part 1 inputs and result into base 10
        val_a = (int(A2) * 2) + int(A1)
        val_b = (int(B2) * 2) + int(B1)
        val_sum = (int(Cout) * 4) + (int(S2) * 2) + int(S1)

        # Format binary strings
        input_a = f"{A2}{A1}"
        input_b = f"{B2}{B1}"
        binary_result = f"{int(Cout)}{int(S2)}{int(S1)}"

        print(f"{input_a:<8} | {input_b:<8} | {binary_result:<14} | {val_a} + {val_b} = {val_sum}")

