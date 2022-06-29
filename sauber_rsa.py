import sys

def main_function():
    # Choosing random Prime numbers
    p = 19
    q = 29

    # Multiplication of the prime numbers
    n = p*q
    # Creating The totient of n
    t = (p-1) * (q-1)  # 120

    # Calculating E(Public Key part) and D(Private Key Part)
    e = find_e(t, n)
    d = find_d(e, t)

    # Storing Public and private key
    public_key = (e, n)
    private_key = (d, n)

    print(f"Your public key is: {public_key}")
    print(f"Your private key is: {private_key}")

    while(1):
        try: 
            # Encoding
            text = input("Encode: ")
            cypher_string = encode(text, public_key)
            print(f"Your encrypted message: {cypher_string}")
            print(f"Your decrypted message: {decode(cypher_string, private_key)}")
        except KeyboardInterrupt:
            print("\n\n---------------------------------------------------------------------------------")
            print("\n                           KeyboardInterrupt successful..")
            print("\n---------------------------------------------------------------------------------")
            sys.exit()

# Function for finding all Factors of a given number
# Returns an array with all Factors
def factors(number):
    factors = []

    for i in range(2, number):

        if ((number % i) == 0):

            factors.append(i)

    return factors

# Function to check wether two numbers are coprime to each other or not
# Returns True or False given to Situation


def if_coprime(to_chek, n_or_t):
    to_check_factors = factors(to_chek)
    n_or_t_factors = factors(n_or_t)
    if set(to_check_factors).isdisjoint(set(n_or_t_factors)):
        # No common Factors -> Coprime
        return True
    else:
        # Not Coprime
        return False

# Function to calculate possible candidates for public key part E
# Returns first Candidate of list


def find_e(t, n):
    candidates = []
    f_t = factors(t)
    f_n = factors(n)
    for i in range(2, t):
        #if_coprime(i, n) and
        if if_coprime(i, t) and t % i != 0 and n % i != 0:
            candidates.append(i)

    return candidates[0]

# Function to Calculate private key part D
# Returns first candidate D


def find_d(e, t):
    candidates = []
    for i in range(100000):
        product = e*i
        mod = product % t

        if mod == 1:
            if e == i:
                continue
            candidates.append(i)
    return candidates[0]


# Function to convert string into ascii numbers and using the RSA formula. C = ( M ^ E ) % N
# Returns encoded characters via the ascii list range 0->1,114,111!!!
# Meaning q && p shouldnt be big or it wont work
# Solution to given problem -> Storing numbers in ascii value without converting them to char back
def encode(text, public_key):
    cypher_string = ""
    new_ascii_value = []
    for i in text:
        new_ascii_value.append(pow(ord(i), public_key[0]) % public_key[1])
        cypher_string += (str(chr(pow(ord(i), public_key[0]) % public_key[1])))
    print(f"Your Encrypted Message in number form: {new_ascii_value}")
    return cypher_string


# Function to decode given string back to original string. Formula M = ( C ^ D ) % N
def decode(text, private_key):
    decoded_string = ""
    for i in text:
        decoded_string += (str(chr(pow(ord(i),
                           private_key[0]) % private_key[1])))
    return decoded_string


if __name__ == '__main__':
    
    main_function()
    
