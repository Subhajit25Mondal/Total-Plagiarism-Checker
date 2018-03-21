import requests
import re
import string
import math
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from .FileOps import filterStringList
from .Compare import compareLists


def getWordListFromText(txt):
    txt = txt.translate(string.punctuation)
    txt = re.sub(r'[^\w]', ' ', txt)
    word_lst = word_tokenize(txt)
    #seperators = ['(',')',';',':','[',']',',','{','}','-','=','\n','.',' ','\u2013','\u2014']# My Long Logic....
    #nouse_words = stopwords.words('english')
    nouse_words = ['none'] #We can customize our own low priority words
    word_lst=filterStringList(word_lst,nouse_words) #Add seperators list if required.
    return word_lst


def fromWeb(text):
    wl=getWordListFromText(text)
    lstofres=[]
    r = requests.get("http://webhose.io/filterWebContent?token=c29ad3bb-9cb4-4006-b141-37fc69a63940&format=json&ts=1518421795038&sort=crawled&q={0}".format(text[0:10]))
    if r.status_code != 200:
        print("Fail")
    else:
        data = r.json()
        print(data)
    try:
        if (data['totalResults']==0):
            temp = {}
            temp['url'] = 'Empty No Results!!'
            temp['text'] = 'Empty No Results!!'
            temp['voc_sim'] = 'Empty No Results!!'
            lstofres.append(temp)
        else:
         for i in range(len(data['posts'])):
            temp={}
            temp['url'] = data['posts'][i]['thread']['site_section']
            temp['text'] = (data['posts'][i]['text'])[0:math.floor(0.05*len(data['posts'][i]['text']))]+'.....'
            temp['voc_sim'] = compareLists(wl,getWordListFromText(temp['text']))
            lstofres.append(temp)
    except:
          temp={}
          temp['url']='Could not fetch links_urls.'
          temp['text']='Could not fetch text.'
          temp['voc_sim']='Could not calculate similarity of words!!'
          lstofres.append(temp)

    return(lstofres)

def fromWebAgain(text):
    wl=getWordListFromText(text)
    lstofres=[]
    r = requests.get("http://webhose.io/filterWebContent?token=c29ad3bb-9cb4-4006-b141-37fc69a63940&format=json&ts=1518421795038&sort=crawled&q={0}".format(text))
    if r.status_code != 200:
        print("Fail")
    else:
        data = r.json()
        print(data)
    try:
        if (data['totalResults']==0):
            temp = {}
            temp['url'] = 'Empty No Results!!'
            temp['text'] = 'Empty No Results!!'
            temp['voc_sim'] = 'Empty No Results!!'
            lstofres.append(temp)
        else:
         for i in range(len(data['posts'])):
            temp={}
            temp['url'] = data['posts'][i]['thread']['site_section']
            temp['text'] = (data['posts'][i]['text'])[0:math.floor(0.05*len(data['posts'][i]['text']))]+'.....'
            temp['voc_sim'] = compareLists(wl,getWordListFromText(temp['text']))
            lstofres.append(temp)
    except:
          temp={}
          temp['url']='Could not fetch links_urls.'
          temp['text']='Could not fetch text.'
          temp['voc_sim']='Could not calculate similarity of words!!'
          lstofres.append(temp)

    return(lstofres)
