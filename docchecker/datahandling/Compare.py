'''
Created on 01-Mar-2018

@author: palashsarkar
'''
from . import RabinKarp as rab

#||----------Comparing WordLists To Calculate Vocab Similarity--------||#

def compareLists(lsttochk,wrtlst):
    simhit = 0;    
    for i in lsttochk:
        for j in wrtlst:
            if(len(i)==len(j)):
                if ((rab.RabinKarpMatcher(j,i)).match()>0):
                    simhit += 1
                    break
            else:
                continue
    return ((simhit/len(wrtlst))*100)
