#encoding:utf-8
#单个词实体映射
class Word(object):

    def __init__(self,text = '',freq = 0,length = -1):
        self.text = text#词
        self.freq = freq#词频
        if text != 'X':
            self.length = len(text) if length<0 else length#有效词长
        else:
            self.length = 0
    #为了便于调试信息时打印使用
    def __str__(self):
        return self.text
    
    def __repr__(self):
        return self.text
    #为了便于获取单词的长度
    def __len__(self):
        return self.length