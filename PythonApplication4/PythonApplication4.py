print("Tere! Olen sinu uus sõber - Python")
nimi= input("Mis on sinu nimi?")
print(nimi +"oi kui ilus nimi!")
print(nimi + "Kas leian Sinu keha indeksi? 0-ei, 1-jah =>")
arv=int(input())
if arv ==1:
    print("jah")
else:
    print("viga")
if arv<16:
    print("Tervisele ohtlik alakaal")
if 16 <arv <=19:
    print("Alakaal")
if arv <19 <=25:
    print("Normaalkaal")
if arv <25  <=30:
    print("Ülekaal")
if arv <30  <=35:
    print("Rasvumine")
if arv <35   <=40:
    print("Tugev rasvumine")
if arv >40:
    print("Tervisele ohtlik rasvumine")
else:
    print("Kahju! See on väga kasulik info!")
try:
   a=float(input("A "))
except:
   ValueError

