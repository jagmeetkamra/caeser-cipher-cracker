import sys
import subprocess
import string

# implement pip as a subprocess, download dependencies:
print("\n\n-------------Downloading Dependencies---------------\n\n")
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'langdetect'])
print("\n\n----------------Downloads finished------------------\n\n")

from langdetect import detect
from langdetect import DetectorFactory
from langdetect import detect_langs

#accept arguement and convert the whole string to lowercase
code=sys.argv[1]
code=code.lower()

#break the entered code into individual alphabets
code_letters=[]
for letter in code:
    code_letters.append(letter)

# English alphabets added to a list
alphabets=list(string.ascii_lowercase)

#function that tries all possible keys(1-25y) and stops when language is detected
def decrypter(k):
    key = k
    codelen=len(code_letters)
    while key < 26:
        print("\nTrying key",key, end=", ")
        decoded=[]
        n = 0
        while n < codelen: # this loop runs for the length of the secret string
            m = 0
            while m < 26: # this loop finds the index of alphabet, shifts it back using key and appends to list to decode 
                if code_letters[n] == alphabets[m]:
                    decoded.append(alphabets[m-key])
                    break
                elif code_letters[n] == " ":
                    decoded.append(" ")
                    break
                m += 1
            n += 1

        global check
        check=''.join(decoded)
        print("decodes to: ", check)
        
        DetectorFactory.seed = 0
        langg = detect(check)
        probb = detect_langs(check)
        print("Language detected: ", langg)
        print("Language probabilities: ", probb)
        
        global keyd
        keyd = key
        key += 1

        #english_vocab = set(w.lower() for w in nltk.corpus.words.words())

        if langg == "en":
            return check
        else:
            continue
    return "not found !"
        
#main code
print("\nLets get encrypting...")
enc = decrypter(1)
print("\n\nPOTENTIAL DECRYPTION: [", enc, "]")
print("Key : ", keyd, "\n")

if keyd > 24:
    print("All possible keys have been tried. Thank You!\n")
else:
    # lang detect can sometimes detect jumbled words as english language, so to try remaing keys ask user for input
    inp = input("Try more keys? Y/N   ")
    while inp == "Y" or inp == "y": #as long as user is satisfied or all keys have been tested, this loop runs to try more keys
            enc = decrypter(keyd+1)
            print("\n\nPOTENTIAL DECRYPTION: [", enc, "]")
            print("Key : ", keyd, "\n")

            if keyd > 24: # if the last key(25) has been tried break the loop 
                print("All possible keys have been tried. If the last result isnt meaningful, please \nconsider the possibility that the input string wasn't a secret message. Feel \nfree to scroll through all results.\nUntil Next time !\n")
                break

            inp = input("Try more keys? Y/N   ") 

            if not inp == "Y" and not inp == "y":
                print("\nUntil next time !\n")
                break
