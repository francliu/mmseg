#encoding:utf-8
#词典
import os
import digital
import Word
class Dictionary(object):

    #静态变量存放单词以及单词词频
    dict_words = {}
    quantifier_words = set()
    def __init__(self,root_path):
        #载入字库
        print root_path
        if not Dictionary.dict_words:
            for path in os.listdir(root_path): 
                if path.endswith('.dic'):
                    self.load(os.sep.join([root_path,path]))
                elif path.endswith("unit"):#单位
                    self.load(os.sep.join([root_path,path]), 'unit')
    #载入词典
    @staticmethod
    def load(path,ftype="dic"):
        """
        载入字典
        """
        with open(path) as f:
            for line in f:
                words = line.split(' ')
                if ftype == 'dic':
                    if len(words)==4:
                        word = unicode(words[0].strip(), 'utf-8')
                        Dictionary.dict_words[word] = Word.Word(word, int(words[3]))
                    elif len(words)<4 and len(words)>=2:
                        word = unicode(words[0].strip(), 'utf-8')
                        Dictionary.dict_words[word] = Word.Word(word, int(words[1]))
                    elif len(words)==1:
                        word = unicode(words[0].strip(),'utf-8')
                        Dictionary.dict_words[word] = Word.Word(word,0)
                elif ftype == 'unit':
                    Dictionary.quantifier_words.add(unicode(words[0].strip(),"utf-8"))
    #为了便于获取词典的长度
    def __len__(self):
        return len(self.dict_words)
    #为了获取字典中对应元素的相关信息
    def __getitem__(self,word):
        if Dictionary.dict_words.has_key(word):
            return Dictionary.dict_words[word]
        elif digital.is_chinese_number(word):#数字识别
            return Word(word,0)
        elif len(word) == 1:#生僻字词频为0
            return Word.Word(word,0)
        else:
            return None