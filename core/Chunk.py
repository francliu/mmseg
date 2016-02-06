#encoding:utf-8
class Chunk(object):

    def __init__(self, *words):
        self.words = []
        for word in words:
            if len(word) == 0:
                continue
            self.words.append(word)
    
    #计算chunk的总长度
    def total_word_length(self):
        length = 0
        for word in self.words:
            length += len(word)
        return length
    
    #计算平均长度
    def average_word_length(self):
        return float(self.total_word_length()) / float(len(self.words))

    #统计有效词数
    def effective_word_number(self):
        _sum = 0
        for word in self.words:
            if len(word) > 1 and word.freq >=0:
                _sum += 1
        return _sum

    #统计词频
    def word_frequency(self):
        _sum = 0
        for word in self.words:
            _sum += word.freq
        return _sum
    
    #计算标准差
    def standard_deviation(self):
        average = self.average_word_length()
        _sum = 0.0
        for word in self.words:
            tmp = (len(word) - average)
            _sum += float(tmp) * float(tmp)
        return _sum