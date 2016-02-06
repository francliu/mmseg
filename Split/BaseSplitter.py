#encoding:utf-8
import os
import string
from Dictionary import Dictionary
from Dictionary import Word
#系统当前根目录文件位置
here = os.path.abspath(os.path.dirname(__file__))
#根据当前目录获取当前目录下的词典数据，构造好词典，os.sep在linux下相当于／。
dict_words = Dictionary.Dictionary(here+os.sep+'data')

class BaseSplitter(object):
    
    def __init__(self, text, ext_dict_words=set()): 
        self.text = text  
        self.pos = 0
        self.text_length = len(self.text)  
        self.ext_dict_words = ext_dict_words
    
    def current_char(self):  
        return self.text[self.pos]  

    #UTF-8有点类似于Haffman编码，它将Unicode编码为：
    #0x00-0x7F的字符，用单个字节来表示；
    #0x80-0x7FF的字符用两个字节表示；
    #0x800-0xFFFF的字符用3字节表示；
    #汉字的unicode范围是：0x4E00~0x9FA5
    #其实这个范围还包括了中，日，韩的字符
    #判断是否为汉字
    @staticmethod
    def is_cjk_char(charater):  
        c = ord(charater)
        return 0x4E00 <= c <= 0x9FFF or\
               0x3400 <= c <= 0x4dbf or\
               0xf900 <= c <= 0xfaff or\
               0x3040 <= c <= 0x309f or\
               0xac00 <= c <= 0xd7af
    
    #判断是否是ASCII码
    @staticmethod
    def is_latin_char(ch):  
        if ch in string.whitespace:  
            return False  
        if ch in string.punctuation:  
            return False  
        return ch in string.printable  

    #切割出非中文词  
    def get_latin_words(self):  
        # Skip pre-Word whitespaces and punctuations  
        #跳过中英文标点和空格  
        while self.pos < self.text_length:  
            ch = self.current_char()  
            if self.is_latin_char(ch) or self.is_cjk_char(ch):  
                break  
            self.pos += 1  
        #得到英文单词的起始位置      
        start = self.pos  
          
        #找出英文单词的结束位置  
        while self.pos < self.text_length:  
            ch = self.current_char()  
            if not self.is_latin_char(ch):  
                break  
            self.pos += 1  
        end = self.pos  
          
        #Skip chinese Word whitespaces and punctuations  
        #跳过中英文标点和空格  
        while self.pos < self.text_length:  
            ch = self.current_char()  
            if self.is_latin_char(ch) or self.is_cjk_char(ch):  
                break  
            self.pos += 1  
              
        #返回英文单词  
        return Word.Word(self.text[start:end])

    #运用正向最大匹配算法结合字典来切割中文文本    
    def get_match_cjk_words(self):  
        originalPos = self.pos  
        words = []  
        index = 0  
        while self.pos < self.text_length:  
            if index >= len(dict_words) :  
                break  
            if not self.is_cjk_char(self.current_char()):
                break  
            self.pos += 1  
            index += 1  
              
            text = self.text[originalPos:self.pos]  
            word = dict_words[text]  
            if word:  
                words.append(word)
            elif text in self.ext_dict_words:
                words.append(Word.Word(text, -1))
                  
        self.pos = originalPos  
        if not words:
            words.append(Word.Word('X', 0, 0))#添加结束词 
        return words
