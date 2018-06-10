
from magicsite.models import *

string = """讓你感到痛苦的原因是什麼？
覺得要學的東西好多，好沈重
被身邊的人誤解，或是沒有人可以陪伴自己
身邊的人都比自己好，顯得自己好沒用
以前做錯了一些選擇，導致現在沒辦法成為自己想要的樣子
最後一次哭泣的時候，你心裡所想的比較偏向下面哪一句話？
我怎麼連這個都不會
我再也不要相信他了
我就只能是這樣了
我本來不應該是這樣的
如果可以你會想成為什麼樣的人？
有能力獨當一面的人
有歸宿可以回去的人
有方法可以改變自身處境的人
有機會彌補過錯的人	
想跟過去的自己說些什麼？
你應該要認真的充實自己啊
你不應該對身邊的人那麼差勁
你應該要找點只有你能做的事情
你不應該做這樣子的選擇
你最害怕什麼？
研究書籍、論文
面對人群
權力的壓榨
過去痛苦的記憶
什麼時候會讓你覺得自己很沒用？
試圖跟別人解釋一項自己應該要很熟練，但實際上卻不擅長的事情
想跟一個人好好的說上一段話，卻不歡而散
拚命努力，卻怎麼樣也無法贏過身邊的人
被傳了些和過去有關的謠言，你試著解釋卻越描越黑
幸福的活著對你來說是什麼？
在某個領域有所創新並擁有成就
擁有愛自己的人以及所愛的人
和某些自己崇拜的人一樣，成為一個有用的人
有一個無法也不會後悔的人生
相較之下，你比較不會以下面的哪一項事情排解難過的情緒？
投入大量的時間在工作裡頭
和身邊朋友出去大吃一頓或是看場電影
做一些自己平常會做的事情，裝作沒事
私訊以前的朋友談心
你覺得你是什麼樣的人？
努力卻得不到回報的人
寂寞不被理解的人
有才能卻被埋沒的人
被困在過去的人
你覺得誰最應該被改變？
沒用的自己
身邊自己為是的人
那些不靠努力就能享受一切的人
以前的自己"""

question_set = Question_Set.objects.create(title='絕望的魔法少女',desc ='生而為魔法少女，我很抱歉' )
data = string.split("\n")

for i in range(0, len(data),5):
    question_text = data[i]
    question = Question.objects.create(text=question_text,question_set =question_set)
    for j in range(i+1,i+5):
        if(j==i+1):
            Option.objects.create(text=data[j],op_type='a',question=question)
        elif(j==i+2):
            Option.objects.create(text=data[j],op_type='b',question=question)
        elif(j==i+3):
            Option.objects.create(text=data[j],op_type='c',question=question)
        elif(j==i+4):
            Option.objects.create(text=data[j],op_type='d',question=question)
        
