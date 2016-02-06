#encoding:utf-8
import chardet
from Split.Splitter import Splitter
from Split.KeywordsSplitter import KeywordsSplitter
from core.quantifier import combine_quantifier
from Dictionary.digital import chinese_to_number
from core import replaceTagTool

def seg_text(AllTest, ext_dict_words = set(), use_combine = True):
    #dict = [dictword for dictword in Dictionary.Dictionary.Dictionary.dict_words]
    #通过默认调用Splitter的迭代器来分割语句，并把每次获取的值添加到结果列表中
    allResult = []
    for test in AllTest:
        print test
        for word in Splitter(test, ext_dict_words):
            allResult.append(word)
            print word
    if use_combine == True:
        return combine_quantifier(allResult)
    return allResult
def splitText(Text,orignSegResult = []):
    if not isinstance(Text,unicode):
        encoding = chardet.detect(Text)['encoding']
        Text = unicode(Text,encoding)
        #print Text
    AllTest = []
    rep = replaceTagTool.replaceTagTool()
    Text = rep.replace(Text)
    result = Text.split(u"\n")
    for i in result:
        AllTest.append(i)
        print i
    return AllTest
def seg_keywords(text):
    return KeywordsSplitter(text).__iter__()
def print_seg(test):
    seg_words=seg_text(test)
    for t in seg_words:
        print t
    return seg_words
def test_chinese_to_number():
    test_dig = [(u'九',9),
            (u'十一',11),
            (u'一百二十三',123),
            (u'一千二百零三',1203),
            (u'一万一千一百零一',11101),
            (u'十万零三千六百零九',103609),
            (u'一百二十三万四千五百六十七',1234567),
            (u'一千一百二十三万四千五百六十七',11234567),
            (u'一亿一千一百二十三万四千五百六十七',111234567),
            (u'一百零二亿五千零一万零一千零三十八',10250011038),
            (u'一千一百一十一亿一千一百二十三万四千五百六十七',111111234567),
            (u'一兆一千一百一十一亿一千一百二十三万四千五百六十七',1111111234567),
            ]
    for test in test_dig:
        print chinese_to_number(test[0])
        assert chinese_to_number(test[0])==test[1]
if __name__ == '__main__': 
    #test_chinese_to_number()
    #test_seg(u"为首要目标")
    AllText = splitText(u"好色，打开我额库？济南的名乘客：单词‘！ｆｖ。") 
    seg_text(AllText)
    seg_list = seg_keywords(u'中国人民站起来了pinyin')
    print '\n'.join(seg_list)