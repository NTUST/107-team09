from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from magicsite.models import *


string1='''
掠奪,100,「為什麼得到掌聲的總是你？」
連結,11,「為什麼大家都這樣對我？」
交換,53,「如果我也是這樣就好了。」
倒轉,749,「一切都是我的錯......」
'''

girl=[]
girl = string1.split("\n")
girl.pop()
girl.pop(0)

for j,i in enumerate(girl):
    image_name = "MagicGirl_"+str(j+1)+".png"
    print(image_name)
    data= i.split(",")
    name = data[0]
    age = data[1]
    desc = data[2]
	content = open(image_name, 'rb').read()
	picture = InMemoryUploadedFile(file=BytesIO(content), field_name="file", name="image_name", content_type="image/<png>", size=len(content), charset=None)
	Mahou_Shoujo.objects.create(name=name, age=age, desc =desc, picture=picture)
	

string2='''
吸塵器,可以透過魔杖吸取身邊人們的一項才能，但同時要交換一項等值的才能、記憶或是金錢。
吹泡泡,對他人吹泡泡，可以讓周圍的人以自己想要的方式對待自己，但對一個人只能改寫一次無法再度改寫。
拍立得,拍一張照片，可以跟拍到的人交換身份，但交換過的人便無法再度交換，也無法回到自己本來的身體。
MP3,按下倒轉鍵可以回到過去，但無法跳轉回現在或是未來。
'''

wand = []
wand = string2.split("\n")
wand.pop()
wand.pop(0)

for j,i in enumerate(wand):
    image_name = "wand_"+str(j+1)+".png"
    print(image_name)
    data= i.split(",")
    name = data[0]
    desc = data[1]
    content = open(image_name, 'rb').read()
    picture = InMemoryUploadedFile(file=BytesIO(content), field_name="file", name="image_name", content_type="image/<png>", size=len(content), charset=None)
    Mahou_Shoujo.objects.create(name=name, age=age, desc =desc, picture=picture)
    