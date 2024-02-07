import random
import json

#Randomly select two prime numbers, denoted by p and q (16 bits each)
#check if the number is prime
def is_prime (num):
    
    while True: #check for primality
        
        if num == 0 or num == 1: #known
            return False #not prime
        else:        
            for i in range(2, num): # check against all numbers including itself
                if num % i == 0:
                    return False #not prime
                
            return True #prime
        
#generate number
def primeGenerator ():
    
    number = random.randint(0, 65535) #16bits = 65535 including 0
    gen_num = is_prime(number) #to check generated number
    
    while True:
        
        if gen_num: #if the number is prime keep it
            return number
        else: #if not, generate new number
            number = random.randint(0, 65535)
            gen_num = is_prime(number) #and check it


def compute_n (p, q):
    return p * q


def compute_phi_n (p, q):
    return (p - 1) * (q - 1)


def gcd(big, small):

    new_big = small #the new big number is the previous small number; initialization in temp variable
    new_small = big % small #the new small number is the remainder of the division; initialization in temp variable
        
    while True: #loop until we get to the gcd 
        new_big = small #the new big number is the previous small number in temp variable
        new_small = big % small #the new small number is the remainder of the division in temp variable
        big = new_big #assign the change to the real variable
        small = new_small #assign the change to the real variable
        
        if new_small == 0: #if we reach the end
            return new_big #return the gcd
        

def public_key_generator(phi_N):
    
    pk_e = random.randint(1, phi_N-1) #generate random e value such that e < phi(N)
    
    while True:
        
        if gcd(phi_N, pk_e) == 1: #check if gcd(e, Phi(N)) = 1)
            return pk_e #if yes, keep e
        else: #if not, generate new e
            pk_e  = random.randint(1, phi_N-1)

             
def private_key_generator(pk_e, phi_N): #we already know that gcd(pk)e, phi(N) = 1      
    return pow(pk_e,-1,phi_N) # return multiplicative inverse of e mod phi(N)


def hex_convert_key(n, pk_e): #convert integers to hexadecimals for N and e to generate key
    
    key = (hex(n), hex(pk_e))
    
    return key
 
            
def main():
    p = primeGenerator()
    print(f"p = {p}")
    q = primeGenerator()
    print(f"q = {q}")
    n = compute_n(p, q)
    print(f"N = {n}")
    phi_N = compute_phi_n(p, q)
    print(f"Phi(N) = {phi_N}")
    pk_e = public_key_generator(phi_N)
    print(f"public key e = {pk_e}")
    pk_d = private_key_generator(pk_e, phi_N)
    print(f"private key d = {pk_d}")
    my_public_key = hex_convert_key(n, pk_e)
    print(f"My public-key (N, e) is: {my_public_key}")
    with open("data.txt", "r") as file:
        contents = file.read()
        print(contents)
        
main()