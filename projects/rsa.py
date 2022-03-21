
import random
import math

class keyGenerator:

    '''
    Euclid's algorithm for determining the greatest common divisor
    Use iteration to make it faster for larger integers
    '''
    @staticmethod
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    '''
    Euclid's extended algorithm for finding the multiplicative inverse of two numbers
    '''
    @staticmethod
    def multiplicative_inverse(e, phi):
        d = 0
        x1 = 0
        x2 = 1
        y1 = 1
        temp_phi = phi
        
        while e > 0:
            temp1 = temp_phi/e
            temp2 = temp_phi - temp1 * e
            temp_phi = e
            e = temp2
            
            x = x2- temp1* x1
            y = d - temp1 * y1
            
            x2 = x1
            x1 = x
            d = y1
            y1 = y
        
        if temp_phi == 1:
            return d + phi
        else: 
            return d

    '''
    Tests to see if a number is prime.
    '''
    @staticmethod
    def is_prime(num):
        if num == 2:
            return True
        if num < 2 or num % 2 == 0:
            return False
        for n in range(3, int(num**0.5)+2, 2):
            if num % n == 0:
                return False
        return True

    @staticmethod
    def generate_keypair(p, q):
        if not (keyGenerator.is_prime(p) and keyGenerator.is_prime(q)):
            raise ValueError('Both numbers must be prime.')
        elif p == q:
            raise ValueError('p and q cannot be equal')
        #n = pq
        n = p * q
        print("n" , n)

        #Phi is the totient of n
        phi = (p-1) * (q-1)
        print("phi" , phi)
        #Choose an integer e such that e and phi(n) are coprime
        
        k = 1 
        factors = []
        while(len(factors) != 3):
            k += phi
            print("k", k)
            factors = [ x for x in range(1 , int(k /2) ) if k % x == 0]
            print("factors", factors)

        e = factors[2]
        print("e",e)
        d = factors[1]
        print("d", d)
       
        #Return public and private keypair
        #Public key is (e, n) and private key is (d, n)
        return (e, n), (d, n)   

    @staticmethod
    def define_keys():
        '''
        Detect if the script is being run directly by the user
        '''
        print ("RSA Encrypter/ Decrypter")
        p = int(input("Enter a prime number (17, 19, 23, etc): "))
        q = int(input("Enter another prime number (Not one you entered above): "))
        print ("Generating your public/private keypairs now . . .")
        public, private = keyGenerator.generate_keypair(p, q)
        print ("Your public key is ", public ," and your private key is ", private)
        return public , private

    @staticmethod
    def create_keys(p1, p2):
        '''
        Detect if the script is being run directly by the user
        '''
        print ("RSA Encrypter/ Decrypter")
        p = int(p1)
        q = int(p2)
        print ("Generating your public/private keypairs now . . .")
        public, private = keyGenerator.generate_keypair(p, q)
        print ("Your public key is ", public ," and your private key is ", private)
        return public , private

    

class RSA:

    def encrypt(pk, plaintext):
        #Unpack the key into it's components
        key, n = pk
        #Convert each letter in the plaintext to numbers based on the character using a^b mod m
        cipher = [( ord(char) ** key) % n for char in plaintext]
        #Return the array of bytes
        return cipher

    def decrypt(pk, ciphertext):
        #Unpack the key into its components
        key, n = pk
        #Generate the plaintext based on the ciphertext and key using a^b mod m
        plain = [chr((char ** key) % n) for char in ciphertext]
        #Return the array of bytes as a string
        return ''.join(plain)
    
    def test_rsa(public , private , message):
        encrypted_msg = RSA.encrypt(public , message)
        print("Your encrypted message is: ")
        print(','.join(map(lambda x: str(x), encrypted_msg)))
        print("Decrypting message with public key ", public ," . . .")
        print("Your message is:")
        print(RSA.decrypt(private, encrypted_msg))

    
public_key , private_key = keyGenerator.define_keys()
# public_key , private_key = keyGenerator.create_keys(233,29)
# public_key , private_key = (24007 , 55687) , (23 , 55687)
print(public_key)
print(private_key)
msg = "my name is mahmoud mohammed taha"
RSA.test_rsa(public_key,private_key,msg)
# encrypted_msg = RSA.encrypt(private_key, msg)
# decrypted_msg = RSA.decrypt(public_key, encrypted_msg)

