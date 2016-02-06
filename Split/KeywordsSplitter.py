#encoding:utf-8
import Splitter
import BaseSplitter

class KeywordsSplitter(Splitter.Splitter):

    def __iter__(self):
        pre_words = set([word for word in Splitter.Splitter.__iter__(self)])
        return pre_words.union(self.keywords())

    def keywords(self):
        text = self.text
        pos, length = 0, len(text)
        pre_words = set()
        while pos < length:
            for i in range(pos + 1, length + 1):
                pre_word = text[pos:i]
                if BaseSplitter.dict_words[pre_word] and len(pre_word) > 1:
                    pre_words.add(pre_word)
            pos += 1
        return pre_words