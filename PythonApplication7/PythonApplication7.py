#1
from string import punctuation
vokaali=["a","e","u","i","ü","ö","õ","ä"]
konsonanti="qwrtpsdfghklzxcvbnmj"
markid=punctuation

tekst=input("Sisesta sõna või lause: ").lower()#"ABCD"->!"abcd!"
tekst_list=list(tekst) #["a","b","c","d","!"]
for sümbol in vokaali:
    v+=1
elif sümbol in konsonanti:
    k+=1
elif sümbol in markid:
    m+=1
elif sümbol==" ":
    t+1
print("Vokaali:",v,"/nkonsonanti:",k)
print("Kirjuvahemärgid:",m)
print("Tühikud:",t)

#2
for i in range(5):
    nimi = input("Sisesta nimi: ")
    nimed.append(nimi)

    nimed.sort()
print("Nimed tähestikulises järjekorras:", nimed)
viimane_nimi = nimed[-1]
print("Viimati lisatud nimi on:", viimane_nimi)

uus_nimi = input("Sisesta uus nimi: ")
nimed[-1] = uus_nimi
print("Nimed pärast muutmist:", nimed)

unik_nimed = list(set(nimed))
print("Nimed ilma kordusteta:", unik_nimed)

vanused = [25, 30, 20, 35, 28]
min_vanus = min(vanused)
max_vanus = max(vanused)
keskmine_vanus = sum(vanused) / len(vanused)
kokku_vanus = sum(vanused)

print("Minimaalne vanus:", min_vanus)
print("Maksimaalne vanus:", max_vanus)
print("Keskmine vanus:", keskmine_vanus)
print("Kokku vanus:", kokku_vanus)

 #2
for i in range(5):
     nimi=imput("Sisesta nimi: ").capitalize()
     nimi.append(nimi)


print("Loetelu oli: ",nimed) 
nimed.sort() 
print("Loetelu sorteeritud: ",nimed)
for i in range(len(nimed)):
    print(n+1,".",nimed[n],sep="")
print("Vimasena oli lisatud: ",nimi)

uued_nimed=[]
for iimi in nimed:
    if nimi not in uued_nimed:
        uued_nimed.append(nimi)
