x = "Arhan"
y = 3
z = 3.5

if y > z:
    print("Büyük")

elif y < z:
    print("Küçük")

else :
    print("Eşit")

def agalar():
    ekip = ["berke","batu","bekir","furkan","arhan"]

    for k in ekip:
        print(k)

aracListesi = ["Araba","Uçak","Gemi"]

for l in range(len(aracListesi)):
    print(l)

for m in range(2,20,4):
    print(m)

print(x.upper())


bilgiler = "Arhan Gürsoy 18 Ankara"

print("Adı = " + bilgiler.split()[0])
print("Soyadı = " + bilgiler.split()[1])
print("Yaşı = "+ bilgiler.split()[2])
print("Yaşadığı şehir = " + bilgiler.split()[3])