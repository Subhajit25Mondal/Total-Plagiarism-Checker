'''
Created on 27-Feb-2018

@author: palashsarkar
'''

import PyPDF2
#import textract
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import re


file_obj=None

def opnFile(file_marker):
    global file_obj
    file_obj=open(file_marker,'rb', 100)
    return file_obj

def closeNDelFileObject():
    global file_obj
    file_obj.close()
    del file_obj

def getPdfReaderObj(file_marker):
    pdf_rd_obj = PyPDF2.PdfFileReader(opnFile(file_marker))
    return pdf_rd_obj

def getTextFromFile(loc):
    file_marker=loc #input("Enter file name: ")
    cntr=0
    txt=u''
    pdr=getPdfReaderObj(file_marker)
    while cntr < pdr.numPages:
        pgOb = pdr.getPage(cntr)
        cntr +=1
        txt += pgOb.extractText()
    #if txt=="":
        #txt = textract.process(fileurl, method='tesseract', language='eng')
        # ------Textract Lib can be used to extract text from handwritten pdf files ------#
    closeNDelFileObject()
    return txt.strip()
        
def getWordList(loc):
    txt = getTextFromFile(loc)
    txt = txt.translate(string.punctuation)
    txt = re.sub(r'[^\w]', ' ', txt)
    word_lst = word_tokenize(txt)
    #seperators = ['(',')',';',':','[',']',',','{','}','-','=','\n','.',' ','\u2013','\u2014']# My Long Logic....
    nouse_words = stopwords.words('english')
    #nouse_words = ['are','Abstract'] #We can customize our own low priority words 
    word_lst=filterStringList(word_lst,nouse_words) #Add seperators list if required.
    return word_lst
    
def filterStringList(wrd_lst,excl_lst):
    for i in range(len(wrd_lst)):
        if(i>=len(wrd_lst)):
            break
        for j in excl_lst:
            if((wrd_lst[i]).lower()==j.lower()):
                    del(wrd_lst[i])
                    break
            else:
                continue
    return wrd_lst

def getFinalFilterdText(word_lst):
    final_text = list(set(word_lst))
    final_text = ', '.join(final_text[:-1])
    final_text = final_text.replace(',', '')
    final_text = final_text.replace('Ô', '')
    final_text = final_text.replace('Õ', '')
    return(final_text)
