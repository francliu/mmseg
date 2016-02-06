#encoding:utf-8
import re
import chardet
#处理页面标签类
class replaceTagTool:
    replaceDou = re.compile(u'，')
    replaceQue = re.compile(u'？')
    replaceSentence = re.compile(u'。')
    replaceFen = re.compile(u'；')
    replaceTan = re.compile(u'！')
    replaceMao = re.compile(u'：')
    replaceSingleyin= re.compile(u'‘')
    replaceDoubleyin= re.compile(u'“')
    
    def replace(self,x):
        if not isinstance(x,unicode):
            encoding = chardet.detect(x)['encoding']
            x = unicode(x,encoding)
        x = re.sub(self.replaceDou,"\n",x)
        x = re.sub(self.replaceQue,"\n",x)
        x = re.sub(self.replaceSentence,"\n",x)
        x = re.sub(self.replaceFen,"\n",x)
        x = re.sub(self.replaceTan,"\n",x)
        x = re.sub(self.replaceMao,"\n",x)
        x = re.sub(self.replaceSingleyin,"",x)
        x = re.sub(self.replaceDoubleyin,"",x)
        #strip()将前后多余内容删除
        return x.strip()
