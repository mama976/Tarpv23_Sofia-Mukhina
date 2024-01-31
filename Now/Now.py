#print("Tund on alanud")
#hilinemine=input("Kas õpilane on hilinemine?")
# "JAH"-a.upper(), "Jah"-a.lower(), "Jah"-a.capitalize(), JAH
#if hilinemine.opper()=="JAH":
#    print("Õpilane ootab 30 min")
# print("Õpilane astub klassi")

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






 arv=randint(0,100) #juhuslik täisarv vahemikust 0....100
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
        pilet="täispilet"
    elif vanus<=100:
        pilet="sooduspilet"
    print(pilet) # Ilus ja õige vastus!"Vale vanus või on vaja osta ...

from random import
if "Juku"=
protsent=randit(-100,500) #0-100 0-6-"tasuta", 6-14-"lastepilet", 15-65"täispilet", 65-100-"sooduspilet", 0-100-"viga andmetega"

#8
arve_nr date.today()#datetime.now()
print(arve_nr)
tsekk="Arve: "str(arve_nr)+"\nToode Hind Kogus Summa\n"
summa=0

toode="Piim"
hind=randint(50,100)/100
v=inpyt("Toode: "+toode+" Hind: "+str(hind)+"\nKas tahad osta?").lower()
if v=="jah":
    mitu=int(input("Mity? "))
    tsekk+=toode+" "+str(hind)+" "+str(mitu*hind)+"\n"
    summa+=mitu*hind
toode="Leib"
hind=randint(90,300)/100
v=inpyt("Toode: "+toode+" Hind: "+str(hind)+"\nKas tahad osta?").lower()
if v=="jah":
    mitu=(int("Mity? "))
    tsekk+=toode+" "+str(hind)+" "+str(mitu)+" "str(mitu+hind)+"\n"
     summa+=mitu*hind
toode="Kommid"
hind=randint(600,1500)/100






#8-2
arve_nr date.today()#datetime.now()
print(arve_nr)
tsekk="Arve: "str(arve_nr)+"\nToode Hind Kogus Summa\n"
summa=0
for toode in ["Piim","Leib","Komm"]:
    hind=randint(50,100)/100
    v=inpyt("Toode: "+toode+" Hind: "+str(hind)+"\nKas tahad osta?").lower()
    if v=="jah":
           mitu=(int("Mity? "))
           tsekk+=toode+" "+str(hind)+" "+str(mitu)+" "+str(mitu*hind)+"\n"
           summa+=mitu*hind
tsekk="Kokku maksta: "+str(summa)
print(tsekk)
raha=float(input("Maksa "+str(summa))
if raha==summa:
    print("Tänan ostu eest!")
elif raha>summa:
    print("Tänan ostu eest! Tagasi "+str(raha-summa))
else:
    print("Maksa veel"+str(summa-raha))

#11
ta=date.today().year
sp=date()
sp=date(int(input("Sünniaasta: ")),int(input("sünnikuu: ")),int(input(""Sünnnipäev: "))).year
if (ta-sp)%5==0:
    print("Juubell")
else:
    print("Tavaline sünnipäev")

#14
maht=int(input("Bussi maht: "))
i=int(input("inimeste atv: "))
ba=round(1/maht) #2,3->2
if 1%maht!=0:
    ba+=1
vb1%maht
print("Kokku on vaja {0} bussi ja viimasel sõidavad {1} inimest".format(ba,vb))

