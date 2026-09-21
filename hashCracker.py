import hashlib #Hash library
import argparse as arg #Command-line parsing library adds arguments on the cmd when executing the program
import time 

parser = arg.ArgumentParser(
                    prog='Hash Cracker',
                    description='Hash Cracker using .txt files')
parser.add_argument('hash', help='Paste down the target hash')
parser.add_argument('-w', '--wordlist', default='rockyou.00.txt', help='Choose the file you want to use as a wordlist | rockyou.00.txt by default')
parser.add_argument('-a', '--algorithm', default='md5', help='Choose the hashing algorithm you want to use | md5 by default')
args = parser.parse_args()

def crack_hash(file, targetHash ,hashAlgorithm):
    wordCount = 0 #Number of words tested
    targetHash = targetHash.lower() #Make sure the targetHash is always lower case

    try:
        hashlib.new(hashAlgorithm)
    except ValueError: #Verify if the hashing algorithm introduced is valid
        print(f'\nHashing Algorithm "{hashAlgorithm}" does not exist, please utilize a valid hashing algorithm\n')
        return    
    
    try:
        with open(file, errors='ignore') as f:
            for line in f:
                word = line.strip() #Return a copy of the string with leading and trailing whitespace removed.  
                hashedWord = hashlib.new(hashAlgorithm, word.encode()).hexdigest() #Return a new hashing object using the named algorithm
                wordCount += 1
                if hashedWord == targetHash: # Verify if the word hash equals the targetHash  
                    print(f'\nMatch found: {word}\n')
                    break
            else:
                print(f'\nNo Matches ({wordCount} words tested)\n')
    except IOError:
        print(f'\n{file} not found')

start = time.time()
crack_hash(args.wordlist, args.hash, args.algorithm)
print('**********************\nFinished')
print(f'Execution time: {time.time() - start:.2f} seconds\n**********************')


