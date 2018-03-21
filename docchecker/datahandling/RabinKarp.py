'''
Created on 25-Feb-2018

@author: palashsarkar
'''

class RabinKarpMatcher(object):
            __txt=""
            __ptt = ""
            __m = 0
            __n = 0
            __p = 0
            __t = 0
            __h = 0
            __d = 256
            __q = 139
       
            def __init__(self,__txt,__ptt):
                self.__txt = __txt
                self.__ptt = __ptt
                self.__m = len(__ptt)
                self.__n = len(__txt)
                self.__h = pow(self.__d,(self.__m-1))%self.__q
                self.hsvalFstFrm ()
            
            def hsvalFstFrm(self):
                for i in range(self.__m):
                    self.__p = (self.__d*self.__p + ord(self.__ptt[i]))%self.__q;
                    self.__t = (self.__d*self.__t + ord(self.__txt[i]))%self.__q;
                    
                    
            def match(self):
                count = 0
                for i in range((self.__n-self.__m)+1):
                    if self.__p == self.__t:
                        if (self.__txt[i:(i+self.__m)]).lower()==(self.__ptt).lower():
                            count += 1
                            #print("Match found at point %d.\n"%(i))
                    if i < (self.__n-self.__m): 
                        self.__t = (self.__d*(self.__t - ord(self.__txt[i])*self.__h) + ord(self.__txt[i+self.__m]))%self.__q;
                        if self.__t < 0:
                            self.__t = (self.__t + self.__q)
                #if count>0:
                    #print("Some hits occured!!\n")
                #else:
                    #print("No hits!!\n")
                return count
                
                    
        
        