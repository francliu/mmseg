#encoding:utf-8
import re
import BaseSplitter
class simpleSplitter(BaseSplitter.BaseSplitter):  
      
    #初始化对象，构造函数
    def __init__(self, text, ext_dict_words=[]):
        BaseSplitter.BaseSplitter.__init__(self, text, ext_dict_words)  
        self.group_char = re.compile(u'[a-zA-Z]+[*?]*|[0-9]+[*?]*|.+[*?]*', re.UNICODE).findall
      
    #得到下一个切割结果  
    def __iter__(self):  
        while self.pos < self.text_length:  
            if self.is_cjk_char(self.current_char()):  
                word  = self.get_cjk_words()
                if len(word) > 0:
                    word = unicode(word)
                    #print word
                    (yield word)
            else :  
                word = self.get_latin_words() 
                if len(word) > 0:
                    for word in self.group_char(unicode(word)):
                        (yield word) 
        raise StopIteration
      
    #切割出中文词  
    def get_cjk_words(self):  
        words = self.get_match_cjk_words()
        maxPos=0
        maxValue=0
        for pos,word in enumerate(words):
            if len(word)>maxValue:
                maxValue = len(word);
                maxPos = pos 
        word = words[maxPos]
        self.pos += len(word)
        return word