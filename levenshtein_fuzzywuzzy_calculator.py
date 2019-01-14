import Levenshtein
from fuzzywuzzy import fuzz
def fm(s1, s2):
    if(len(s1)<len(s2)):
        s1,s2 = s2,s1
    score = Levenshtein.distance(s1, s2)
    if score == 0.0:
        score = 1.0
    else:
        score = 1 - (score / len(s1))
    return score


def fuzzwuzz(s1, s2):
    return fuzz.partial_ratio(s1, s2)
print('Enter the first string -->',end='\n')
s1 = input().strip().upper()
print('Enter the second string -->',end='\n')
s2 = input().strip().upper()
print('\nlevenshtein - ',fm(s1,s2),'## fuzzywuzzy - ',fuzzwuzz(s1, s2))
