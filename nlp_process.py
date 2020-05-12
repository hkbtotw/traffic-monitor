from pythainlp import word_tokenize, Tokenizer
from pythainlp.corpus.common import thai_words
from pythainlp.tokenize import dict_trie
import string
from nlp_name import database


class text_nlp(object):
    def __init__(self):
        self.specWord=['#ฝนตก']
        self.removeWord=['JS100','js100radio']
        self.engineSel='newmm'

    def ProcessText(self,text):

        dataBase=database()
        streetDf, addressDf=dataBase.ReadStreetName()

        streetList=dataBase.DataframeToList(streetDf)
        addressList=dataBase.DataframeToList(addressDf)
        districtList=dataBase.districtName_
        wordList=districtList+streetList+addressList

        custom_words_list=set(thai_words())
        custom_words_list.update(wordList)
        custom_words_list.update(self.specWord)

        trie=dict_trie(dict_source=custom_words_list)

        custom_tokenizer=Tokenizer(custom_dict=trie, engine=self.engineSel)
        proc=custom_tokenizer.word_tokenize(text)
        
        cleanList_1 = []
        cleanList=[]
        [cleanList_1.append(i.translate(str.maketrans('','',string.punctuation))) for i in proc]
        [cleanList.append(i.translate(str.maketrans('','','1234567890'))) for i in cleanList_1]

        procText = list(filter(lambda x: x != " " , proc))
        procText = list(filter(lambda x: x != "  " , procText))
        procText = list(filter(lambda x: x != "" , procText))
        #procText = list(filter(lambda x: len(x)>2, procText))
        joinText=' '.join(procText)
        #print(joinText)
        return joinText
    
    def RemoveWord(self, inStr):
        cleanList=inStr.translate(str.maketrans('','',string.punctuation))
        outStr = cleanList.replace('\n','')
        for n in self.removeWord:
            outStr = outStr.replace(n,'') 

        return outStr