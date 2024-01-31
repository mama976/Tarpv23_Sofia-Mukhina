using System.IO.Ports;

Tõlgi suhtlemise laused eesti keele ja lisa kommentaare koodi seletamiseks.

print("***NUMBRIDEGA MÄNGUD ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1:
    try:
        a = (abs(int(input("Sisestage täisarv => ")))
        break
    except ValueError:
         print("See ei ole täisarv")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a == 0:
    print("Nulliga pole mõtet midagi ette võtta")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Määrake, kui palju paaris ja mitu paaritu numbrit on arvus")
    print()
    c=b=a
    paaris=0
    paaritu=0
    while b > 0:
        if b % 2 = 0:
                    paaris+=1
            else:
                    paaritu = +1
            b = b // 10


    print("Paarisarvud: "+string(paaris))
    print("Paaritud arvud: "+string(paaritu))
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("*Selle ümber pööramine* sisestatud number")
    print()
    b = 0
    while a > 0
        number = a % 10
        a = a // 10
        b = b * 10+ number
    print("Pööratud atv "+string(b))
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print(("Siracuse hüpoteesi testimine")
    print()
    if c % 2 = 0:
        print("c - paarisarv. Jagage 2.")
    else:
        print("с - paaritu number. Korrutage arvuga3, lisage 1 ja jagage 2-ga.")
    while c != 1:
            if c % 2 = 0:
                    c == c / 2
            else:
                    c == (3 * c + 1) / 2
            print(c, end = ")
    print()
    print("Hüpotees on õige")