#x=2;
#print(x)
#x=x+2
#print(x)
#x=5
#if x<10:
 #   print("smaller")
#if x > 20:
#    print("bigerr")
#print("finis")
#print('C:\some\name')   # \n yeni satıra geçiş yapacaktır
#print(r'C:\some\name')  # metin öncesi r kullanıldığında \n gördüğünde bir alt satıra geçmeyecektir
#print (30 * 'like -->' +  'egypt') 
#omer ="Egypt"
#Abde="cici"
#print(omer+" : "+Abde)
#text=("istanbulda kar yagiyor ")
#print (text)
#a=5
#a=str(a)
#print(type(a))
#b=int(3.5)
#print(type(b))
#no= float('12!!345.0')
#print(type(no))
#word_python="AaaEgypt"
#print(word_python[0])
#print(word_python[1])
#print(word_python[2])
#print(word_python[-3])
#print(word_python[-2])
#Art="fsmvu"
#print("Ar"+Art[2:]+" ====>  "+len(Art))
#print(Art[0:3])


#i=0
#while i!=100:
#    i=i+1
#    print(i)
#print("while bitti")

#input int icin sayi=int(sayi)
#sayi =input("lutfen bir sayi giriniz  :=>  ");
#sayi=float(sayi) , sayi =int(sayi)
#if sayi<100:
#   print("bu sayi 100den azdir ")
#if sayi>100:
#    print("bu sayi 100den buyuktur")
#print("porgram  bitti ")

#Hour=input("Enter Hours : ")
#Hour =int(Hour)
#rate=input("Enter Rate : ")
#rate =float(rate)
#print("Pay : ",(Hour * rate))

#x= input("x ===> ")
#x=int(x)
#if x <2 :
#    print('small')
#elif x<10:
#    print('Medium')
#else:
#    print('LARGE')
#print('All done')


#astr ='Bob' 
#try:
#    print("Hello")
#    iste=int(astr)
#except:
#    print('error')
#try:
# a=input("enter Hours = >")
# a=int(a)
# b=input("enter Rate = >")
# b=int(b)
#except:
#    print("Error ,please enter numeric input")

#try:
# while True:
#    line=input(' > ')
 #   line=int(input(' > '))
#    if line==0:
#     break
#    print(line)
# print('Done ! ')
#except:
# print(" only you")
#for i in [5,4,3,2,1] :
#    print(i)
#print('done')
#n=0
#k="mahmut"
#while n<len(k):
#     print("turk",n)
#     n=n+1
#print("bitti")

#greet ="Hello WORD"
#zap=greet.upper()
#print(zap)



# python  dersten sonraki calismalar 
fp=open("romeo.txt")
my_lst = list()
my_lst =[]
for my_line in fp:
    my_lst2 = my_line.strip()
    my_w = my_lst2.split()
    my_lst.extend(my_w)
my_lst.sort()
my_new_list=[]
for n in my_lst :
    if n not in my_new_list :
        my_new_list.append(n)
print(my_new_list)
#output
#['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'and', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'is', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'sun', 'the', 'the', 'the', 'through', 'what', 'window', 'with', 'yonder']
word = "python"
h =0
for harf in word :
  print(word[h])
  #index'in artlamak icin yaptim 
  h=h+1
print("word yazdirildi")

#output
#p
#y
#t
#h
#o
#n
#word yazdirildi


list=["Abderrhman",34,"omer","islem"]
list.append("Mahmut 562")
#list'de eklemek icin
#list[len(list):]=["sa","as","vur","salmun"]
#bu listten sonra eklemek icin kullandim 
adilar=["sa","as","vur","salmun"]
list.extend(adilar)
print(list)
#output
#['Abderrhman', 34, 'omer', 'islem', 'Mahmut 562', 'sa', 'as', 'vur', 'salmun']




A=[1,2,5,8,5,5,877,4]
print(A)
A.append(658)
print(A)
B=[100,200,300,400,500,60,0]
A.extend(B)
print(A)
 #output
#[1, 2, 5, 8, 5, 5, 877, 4]
#[1, 2, 5, 8, 5, 5, 877, 4, 658]
#[1, 2, 5, 8, 5, 5, 877, 4, 658, 100, 200, 300, 400, 500, 60, 0]



A.insert(1,700)
#bunu silmek icin kullandim 
#A.clear()
print(A)
print()
#indesini bilmek icin kullandim 
print(A.index(2))
#output
#[1, 700, 2, 5, 8, 5, 5, 877, 4, 658, 100, 200, 300, 400, 500, 60, 0]
#2


A.insert(2,"Mhmut")
A.pop(2)
print(A)
#[1, 700, 2, 5, 8, 5, 5, 877, 4, 658, 100, 200, 300, 400, 500, 60, 0]




Adler=["M","A","S","9","A"]
Adler.extend(adilar)
print(Adler)
print()
Adler.pop(2)
print(Adler)
Adler.sort()
print("sortin halindeyiz")
print(Adler)
print("pop kullanarak  sonuc buldum ")
Adler.pop()
print(Adler)
print("index kullanarak  buldum")
indes =Adler.index("salmun")
print("salmun his index is : ",indes)
print("eklendi ")
Adler.insert(6,"as")
Adler.insert(5,"as")
Adler.insert(7,20)
print(" ekledikten sonra ",Adler)
print(" listteki elmenlerini sayisi bulmak icin")
S=Adler.count("as")
print(" as saysini bulma : => ",S)
print()
print("listini ters yazdirma icin ")
Adler.reverse()
print(Adler)

#['M', 'A', 'S', '9', 'A', 'sa', 'as', 'vur', 'salmun']
#['M', 'A', '9', 'A', 'sa', 'as', 'vur', 'salmun']
#sortin halindeyiz
#['9', 'A', 'A', 'M', 'as', 'sa', 'salmun', 'vur']
#pop kullanarak  sonuc buldum 
#['9', 'A', 'A', 'M', 'as', 'sa', 'salmun']
#index kullanarak  buldum
#salmun his index is :  6
#eklendi 
# ekledikten sonra  ['9', 'A', 'A', 'M', 'as', 'as', 'sa', 20, 'as', 'salmun']
# listteki elmenlerini sayisi bulmak icin
# as saysini bulma : =>  3
#listini ters yazdirma icin 
#['salmun', 'as', 20, 'sa', 'as', 'as', 'M', 'A', 'A', '9']


listtr=["A","B","C","D","R","P"]
print(" from collections import deque ")
from collections import deque
k=deque(listtr)
k.append("E")
print(k,"\n")
#bastan siliyor
k.popleft()
#sonudan siliyor
k.pop()
print(k)
#output
#from collections import deque 
#deque(['A', 'B', 'C', 'D', 'R', 'P', 'E']) 
#deque(['B', 'C', 'D', 'R', 'P'])

sayilar = []
#for 10 kere donup  power aliyor sayilar
for x in range(10) :
   sayilar.append(pow(x,2))
print(sayilar)
#range kac kere dondugunu  soyler
for i in range(3):
    sayilar.pop()
print(sayilar)
#output
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#[0, 1, 4, 9, 16, 25, 36]

num=[10,5,78,8,4]
#tek tek elmeni alip powerini aliyor ondan 
#list sekilde yazdiriyor
tatili=[(j,pow(j,2)) for j in num]
print(tatili)
#output
#[(10, 100), (5, 25), (78, 6084), (8, 64), (4, 16)]



#ikinci quiz cevabi 
#/////////////////////////////////////////////////////////////////
#file=open("haber.txt")
file=open("haber.txt")
#bir dosya actim
filelist = []
#listimi ekledim 
for line in file :
    #dosyadaki yazdirmak icin kullanilir 
    #print(line)
    #burada dosyanin  kelimleri burada listte ekledim
    #filelist.append(line)
    my_list=line.split()
    #split burada her satir bir listte ekliyor
    #yani  her satir alip () --> nullin gorenen kadar
    #ondan sonra her kilmenin ayir ayir bolumup bir list
    #sklinde gosteriyor
    #print(my_list)
    #output
    #birinici satir icin  
    #WASHINGTON — George Nader, a Lebanese-American busine --> bir satir
    #['WASHINGTON', '—', 'George', 'Nader,', --> liste sekilde eklendi
    #'a', 'Lebanese-American', 'busine']
    for w in my_list:
     #burada bakiyorum listte var mi yok mi 
     #eger var ise eklemeyceck 
     #yok ise ekler
     #boylece ayine kilme eklemez  
        if w not in filelist:
            filelist.append(w)
              
print(filelist,"\n")
#sirlama yapmak isterim
filelist.sort()
print(filelist,"\n")
#listteki ikincici elmeneyi yazdirmak icin  
#print(filelist[1])
count =0
harflar=[]
for k in filelist:
      #birinci index buarda aliyoru
         harf=k[0]
      #sonra buarda harf buyuk yapiyorum
         harf=harf.upper()
         if harf not in harflar:
            count=0
         #eger burada yok ise  o zaman liste ekliyor
            harflar.append(harf)
            for i in filelist:
           #gerck listeye bakip  orada  harfini sayisi artliyor
               if i[0].upper() == harf:
                  count+=1
            print(harf,"count is ",str(count))

#output
#['WASHINGTON', '—', 'George', 'Nader,', 'a', 'Lebanese-American', 'busine', 'ssman,', 'has', 'hovered', 'on', 'the', 'fringes', 'of', 'international', 'diplomacy', 'for', 'three', 'decad', 'es.', 'He', 'was', 'back-channel', 'negotiator', 'with', 'Syria', 'during', 'Clinton', 'administration,', 'reinvented', 'himself', 'as', 'an', 'Mr.', 'Nader', 'is', 'now', 'focus', 'investigation', 'by', 'Ro', 'bert', 'S.', 'Mueller', 'III,', 'special', 'counsel.', 'In', 'recent', 'weeks,', 'Mueller’s', 'i', 'nvestigators', 'have', 'questioned', 'and', 'pressed', 'witnesses', 'information', 'about', 'any', 'possible', 'attempts', 'The', 'investigators', 'also', 'asked', 'Nader’s'] 
#['Clinton', 'George', 'He', 'III,', 'In', 'Lebanese-American', 'Mr.', 'Mueller', 'Mueller’s', 'Nader', 'Nader,', 'Nader’s', 'Ro', 'S.', 'Syria', 'The', 'WASHINGTON', 'a', 'about', 'administration,', 'also', 'an', 'and', 'any', 'as', 'asked', 'attempts', 'back-channel', 'bert', 'busine', 'by', 'counsel.', 'decad', 'diplomacy', 'during', 'es.', 'focus', 'for', 'fringes', 'has', 'have', 'himself', 'hovered', 'i', 'information', 'international', 'investigation', 'investigators', 'is', 'negotiator', 'now', 'nvestigators', 'of', 'on', 'possible', 'pressed', 'questioned', 'recent', 'reinvented', 'special', 'ssman,', 'the', 'three', 'was', 'weeks,', 'with', 'witnesses', '—'] 
#C count is  2
#G count is  1
#H count is  5
#I count is  8
#L count is  1
#M count is  3
#N count is  6
#R count is  3
#S count is  4
#T count is  3
#W count is  5
#A count is  10
#B count is  4
#D count is  3
#E count is  1
#F count is  3
#O count is  2
#P count is  2
#Q count is  1
#— count is  1

#pyhtondaki dict
my_dict={}
#diksyoun pyhtonde oluşturmek icin kullanilan yetiyor 
my_dict={"Abderrhman":0,"Abdellatif":1}
#1 yontemi {object , key }
my_dict["omer"]=3
#2 yontemi []=keyini olsun
print(my_dict)
#output
#{'Abderrhman': 0, 'Abdellatif': 1, 'omer': 3}
my_dict["ense"]=5
print(my_dict)
# 1 yontemi listeye ekleme 
names_list=[my_dict.keys()]
print(names_list)
#output
#[dict_keys(['Abderrhman', 'Abdellatif', 'omer', 'ense'])]
#2 yontemi listeye ekleme
my_list_dict=[]
for p in names_list :
      my_list_dict.append(p)     
print(my_list_dict)    
#for skilnde yapmak istersek
seq={x : pow(x,2) for x in range(10)}
print("power almak icin ","\n",seq)
#output
#power almak icin  
#{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

#burada her rakemini keyinin pow 2 olsun istedim

#eger tum elemnleri baska yola atmak istersem boyle oluyor
kopya_list=seq.copy()
print(kopya_list)
#output 
#{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

#eger silmek istyorsam boyle olsun 

#kopya_list.clear()
#print(kopya_list)
#output
#{}
print()
#get valunu keyini gettiriyor
get_olsun=my_dict.get("ense")
print(my_dict)
print("ense keyini ----> ",get_olsun)
#output
#{'Abderrhman': 0, 'Abdellatif': 1, 'omer': 3, 'ense': 5}
#ense keyini ----> 5
setdefault_dict=my_dict.setdefault("Taha",64)
print(my_dict)
my_dict["hacar"]=87
print(my_dict)
#output
#{'Abderrhman': 0, 'Abdellatif': 1, 'omer': 3, 'ense': 5, 'Taha': 64}
#{'Abderrhman': 0, 'Abdellatif': 1, 'omer': 3, 'ense': 5, 'Taha': 64, 'hacar': 87}
#list yenilemek icin  kullanir
my_dict.update(seq)
print(my_dict)
#{'Abderrhman': 0, 'Abdellatif': 1, 'omer': 3, 'ense': 5, 'Taha': 64, 'hacar': 87, 0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}


