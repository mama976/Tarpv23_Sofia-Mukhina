#print("Tund on alanud")
#hilinemine=input("Kas �pilane on hilinemine?")
# "JAH"-a.upper(), "Jah"-a.lower(), "Jah"-a.capitalize(), JAH
#if hilinemine.opper()=="JAH":
#    print("�pilane ootab 30 min")
# print("�pilane astub klassi")

 from random import
 protsent=randit(-100,500) #0-100 0-60-"2", 61-75-"3", 76-89"4", 90-100-"5"
 print(protsent,"% on testi tulemus")
 if protsent<0 or protsent>100:
     tulemus="valed andmed"
 elif 0<protsent<60:    #protsent>0 and protsent<60, protsent<60
     tulemus="hinne 2"
 elif 60<=protsent<75:
    tulemus="hinne 3"
 elif 75<=protsent<90:
    tulemus="hinne 4"
 else:      #= elif 90<protsent<=100:
     tulemus="hinne 5"
 print(tulemus)






 arv=randint(0,100) #juhuslik t�isarv vahemikust 0....100
 print(arv)
 if arv=%2==0:
     print(arv,"on paaris arv")
 else:
    print(arv,"on paaritu arv")

#1
nimi=input("Mis on sinu nimi?").capitalize() #"anna"
print("Tere,",nimi) #"Tere,Anna"
if nimi=="Juku":
    print("Lahme kinno")
    vanus=int(input("Kui vana sa oled?"))
    if vanus<0 or vanus>100:
        pilet="vale vanus"
    elif vanus<6:
        pilet="tasuta pilet"
    elif vanus<=14: #<15
        pilet="Lastepilet"
    elif vanus<65:
        pilet="t�ispilet"
    elif vanus<=100:
        pilet="sooduspilet"
    print(pilet) # Ilus ja �ige vastus!"Vale vanus v�i on vaja osta ...

from random import
if "Juku"=
protsent=randit(-100,500) #0-100 0-6-"tasuta", 6-14-"lastepilet", 15-65"t�ispilet", 65-100-"sooduspilet", 0-100-"viga andmetega"
if 