
#BU KOD HERHANGİ BİR SİMÜLASYONLA BAĞLANTILI OLMADIĞI İÇİN ÇALIŞMAYACAK


from dronekit import connect

drone=connect('buraya simülasyon için gerekli port gelecek',wait_ready=True)

print(f'Drone Arm Durumu {drone.armed}')

print(f'Global Frame{drone.location.global_frame}')
print(f'Global Relative Frame{drone.location.global_relative_frame}')


#Buradan sonra drone kalkış ve konum fonksiyonu başlıyor

from dronekit import connect,VehicleMode,LocationGlobalRelative
import time

iha =connect('buraya IP',wait_ready=True)

#kaldırmak için önce kalkmayacak şekilde drone motoru çalışıyor olmalı

print(iha.is_armable)

print(iha.armed)
#droneun kalkabilmesi için simülasyonda guided olması lazım
iha.mode = VehicleMode("GUIDED")

#BU KOD SAYESİNDE OTOMATİKMAN GUİDEDA GEÇECEK

iha.armed= True

iha.simple_takeoff(10) #bu paranteze aracın çıkmasını istediğimiz yüksekliği yazacağız

def kalkış(irtifa):
    while iha.is_armable is not True:
        print("İHA arm edilebilir durumda değil.")
        time.sleep(1)
        
    print('İHA arm edilebilir')
    iha.mode = VehicleMode("GUIDED")
    time.sleep(1)
        
    print(str(iha.mode) + "moduna alındı")

    iha.armed=True

    while iha.armed is not True:
            print("İHA arm ediliyor...")
            time.sleep(0.5)
    print("İHA arm edildi")

    iha.simple_takeoff(irtifa)
    while iha.location.global_relative_frame.alt < irtifa * 0.9 :
            print("İHA hedefe yükseliyor")
            time.sleep(1)    
    


    print("İHA arm edilebilir durumda değil.")
    time.sleep(1)    


kalkış(15) #bu şekide direkt simülasyonda 15 metrelik irtifaya çıkacak

konum = LocationGlobalRelative()#konum fonksiyonu bu bu şekilde bi konumu drone kit in anlayabilecğei şekilde gösterebiliyoruz.


iha.simple_goto(konum)#bu fonksiyon yukarıdaki konum değerini alacak

































