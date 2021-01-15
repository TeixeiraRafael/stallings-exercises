#This program also solves problem 2.25

#!/usr/bin/env python3
import sys 
import math

results = int(sys.argv[1])
#networksecurityandcriptographytheoryandpractice
message = "ofxupsl tfdvsjuz boe dsjquphsbqiz uifpsz boe qsbdujdf"
alphabet = 'abcdefghijklmnopqrstuvwxyz'

alphabetFrequency = {
    'e' : 12.0, 't' : 9.10, 'a' : 8.12, 'o' : 7.68, 'i' : 7.31, 'n' : 6.95, 
    's' : 6.28, 'r' : 6.02, 'h' : 5.92, 'd' : 4.32, 'l' : 3.98, 'u' : 2.88,
    'c' : 2.71, 'm' : 2.61, 'f' : 2.30, 'y' : 2.11, 'w' : 2.09, 'g' : 2.03, 
    'p' : 1.82, 'b' : 1.49, 'v' : 1.11, 'k' : 0.69, 'x' : 0.17, 'q' : 0.11,
    'j' : 0.10, 'z' : 0.07 
}

letterCount = {c: 0 for c in alphabet} 
letterFrequency = dict()

for c in message:
    if(c == ' '):
        continue
    letterCount[c] += 1;

for c in message:
    if(c == ' '):
        continue
    letterFrequency[c] = (letterCount[c] / len(message)) * 100

sortedFrequency = dict(sorted(letterFrequency.items(), key=lambda item: item[1], reverse=True))

threshold = 0.9
for i in range(results):
    decrypted = message    
    substitutions = []
    
    sortedFrequencyList = [(k, v) for k,v in sortedFrequency.items()]
    alphabetFrequencyList = [(k, v) for k,v in alphabetFrequency.items()]
    
    for i in range(len(sortedFrequencyList)):
        old = sortedFrequencyList[i][0]
        new = alphabetFrequencyList[i][0]
        decrypted = decrypted.replace(old, new)

        
    threshold += 0.1
    print(decrypted)
    print()