#encoding:utf-8

from Split import Splitter
from Split import simpleSplitter
class percent(object):
    
    def __init__(self):
        self.currentCorrentNum=0
        self.originNum=0
        self.segAllNum=0
        self.segTests = {}
        self.allResult = {}
        self.strText = []
    def recallPercent(self):
        return float(self.currentCorrentNum)/self.originNum
    def correntPercent(self):
        return float(self.currentCorrentNum)/self.segAllNum
    def readFile(self,path):
        with open(path) as f:
            for line in f:
                line = unicode(line,u'utf8')
                result = line.split(u'　');
                originWords = []
                for i,j in enumerate(result):
                    if i!=0:
                        originWords.append(j.strip())
                    #print i,j.strip()
                self.segTests[result[0].strip()] = originWords
                self.strText.append(result[0].strip())
                #print percent.segTests
                #percent.segTests[j.strip()]
    def compareList(self,originList,segList):
        self.segAllNum+=len(segList)
        self.originNum+=len(originList)
        test={}
        for word in originList:
            #print word
            if test.get(word)!=None:
                test[word] += 1 
            else:
                test[word] = 1 
        for word in segList:
            if test.get(word)!=None:
                self.currentCorrentNum+=1
                test[word]-=1
    def seg_text(self,text,ext_dict_words = set(), use_combine = True):
    #dict = [dictword for dictword in Dictionary.Dictionary.Dictionary.dict_words]
    #通过默认调用Splitter的迭代器来分割语句，并把每次获取的值添加到结果列表中
        #Result=[word for word in Splitter.Splitter(text, set())]
        Result=[]
        print text
        for word in Splitter.Splitter(text,ext_dict_words):
            Result.append(word)
            print word
        return Result
    def segAlltext(self):
        for text in self.strText:
            #print text
            Result = self.seg_text(text)
            self.compareList(percent.segTests[text],Result)
            self.allResult[text] = Result
        print self.originNum,self.segAllNum
        print "召回率：" +str(self.recallPercent()*100)+"%"
        print "正确率：" +str(self.correntPercent()*100)+"%"
    def simpleSegText(self,text,ext_dict_words = set(), use_combine = True):
    #dict = [dictword for dictword in Dictionary.Dictionary.Dictionary.dict_words]
    #通过默认调用Splitter的迭代器来分割语句，并把每次获取的值添加到结果列表中
        #Result=[word for word in Splitter.Splitter(text, set())]
        Result=[]
        print text
        for word in simpleSplitter.simpleSplitter(text,ext_dict_words):
            Result.append(word)
            print word
        return Result
    def simpleSegAlltext(self):
        for text in self.strText:
            #print text
            Result = self.simpleSegText(text)
            self.compareList(percent.segTests[text],Result)
            self.allResult[text] = Result
        print self.originNum,self.segAllNum
        print "召回率：" +str(self.recallPercent()*100)+"%"
        print "正确率：" +str(self.correntPercent()*100)+"%"
percent = percent()
percent.readFile("./test/DEMO.TXT")      
percent.segAlltext()
#percent.simpleSegAlltext()