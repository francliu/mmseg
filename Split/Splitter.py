#encoding:utf-8
import re
import BaseSplitter
from core.Router import route
from core import Chunk
class Splitter(BaseSplitter.BaseSplitter):  
      
    #初始化对象，构造函数
    def __init__(self, text, ext_dict_words=[], route=route):
        BaseSplitter.BaseSplitter.__init__(self, text, ext_dict_words)  
        self.route = route  
        self.group_char = re.compile(u'[a-zA-Z]+[*?]*|[0-9]+[*?]*|.+[*?]*', re.UNICODE).findall
      
    #得到下一个切割结果  
    def __iter__(self):  
        while self.pos < self.text_length:  
            if self.is_cjk_char(self.current_char()):  
                for word in self.get_cjk_words():
                    if len(word) > 0:
                        word = unicode(word)
                        (yield word)
            else :  
                word = self.get_latin_words() 
                if len(word) > 0:
                    for word in self.group_char(unicode(word)):
                        (yield word) 
        raise StopIteration
      
    #切割出中文词，并df且做处理，用上述4种方法  
    def get_cjk_words(self):  
        #应用规则过滤
        chunks = self.route(self.create_chunks())
          
        #最后只有一种切割方法  
        chunk = chunks[0] 
        self.pos += chunk.total_word_length()  
        return chunk.words
      
    #三重循环来枚举切割方法，这里也可以运用递归来实现  
    def create_chunks(self):  
        chunks = []  
        originalPos = self.pos  
        words1 = self.get_match_cjk_words()  
          
        for word1 in words1:  
            self.pos += len(word1)  
            if self.pos < self.text_length:  
                words2 = self.get_match_cjk_words()  
                for word2 in words2:  
                    self.pos += len(word2)  
                    if self.pos < self.text_length:  
                        words3 = self.get_match_cjk_words()  
                        for word3 in words3:  
                            chunk = Chunk.Chunk(word1, word2, word3)  
                            chunks.append(chunk)  
                    elif self.pos == self.text_length: 
                        chunks.append(Chunk.Chunk(word1, word2))  
                    self.pos -= len(word2)  
            elif self.pos == self.text_length:
                chunks.append(Chunk.Chunk(word1))  
            self.pos -= len(word1)  
        self.pos = originalPos
        return chunks