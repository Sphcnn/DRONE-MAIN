
#BU KOD HERHANGİ BİR SİMÜLASYONLA BAĞLANTILI OLMADIĞI İÇİN ÇALIŞMAYACAK
#SİMÜLASYON İÇİN SANAL BİLGİSAYAR KURUP ORADAN LİNUX UBUNTU KURULACAK. ARDUPILOT STL VE  GAZEBO SİMÜLASYONLARI EŞ ZAMANLI KULLANILACAK.

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


#BURADAN SONRASI GÖREV YÜKLEME

from dronekit import connect, VehicleMode,LocationGlobalRelative,LocationGlobal,Command,mavlink
import time
from pymavlink import mavutil



iha = connect("IP GELECEK",wait_ready=True)

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


def add_mission():
    global komut
    komut=iha.commands
   
    konum.clear()  
    time.sleep(1)
#TAKEOFF BEN KALKIŞ YAZMIŞTIM LİNUXTAN YAZARKEN DÜZELTECEĞİM KARIŞIYOR KOD
    komut.add(Command(0,0,0,mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,0,0,0,0,0,0,0,0,))
#BURADA BİR SÜRÜ PARAMETRE VAR
#target_system verdiğimiz değerin önemi yok çünkü dronekit bunu kendi MAVLİNK ID ile ayarlayacak
#target_component bu prmtre drone değill herhangi bir alt sisteme görev verir cam,mic,gun,etc.
#seq görev sıralaması için kullanılır buna sıfır versek bile dronekit kendi ayarlıyor
#frame (x,y,z) kordinatlarının neye göre referans alınacağını belirler. mavutil.mavlinkMAV_FRAME_GLOBAL_RELATIVE_ALT bu komut kalkış noktasından itibaren sıfır almasını sağlıyor
#**takeoff prmtresi drone gönderdiğimiz komutun ne olduğunu tanımlayan prmtre
#bundan sonraki  ikisi desteklenmediği için 0 yazmalıyız
#bu ikisinden sonra 7 tane daha parametre var 6 tanesi kullanılmnadığı için 0 yazacağız sonuncusuna istediğimiz değeri gireceğiz.
#sonuncusuna da dronun çıkmasını  istediğimiz irtifayı yazıyoruz


#WAYPOİNT(DRONEUN GİTMESİNİ İSTEĞİMİZ YER) KOMUTU
    komut.add(Command(0,0,0,mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,0,0,0,0,0,153153,453254,20,))
#Bunun ilk parametresi gittiği yerde kalnasını istediğimiz süreyi(delay) belirleyecek
#prm2,3,4 0 olacak kullanılmıyor
#prm5,6,7 droneun gitmesini istediğimiz konumu gireceğimiz yerler.
#prm5= enlem prm6=boylam prm7= yükseklik
    komut.add(Command(0,0,0,mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,0,0,0,0,0,8485424,44658,20,))

#Bu iki komut sayesinde drone önce üstteki konuma 20 metrelik irtifadan gidecek sonra diğer konua gidecek oradan da RTL komutu çalıştırdğımız zaman başlangıç noktasına dönecek.
#RTL
    komut.add(Command(0,0,0,mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,mavutil.mavlink.MAV_CMD_NAV_RTL,0,0,0,0,0,0,0,0,))
#RTL hiçbir parametre almadığı için son 7 parametrenin hepsi 0 olacak
#bu parametrelere ve komutlaraardupılot stl nin sitesinden ulaşabiliriz ve istediğimiz komutu verebiliriz

#DOĞRULAMA BU KOMUT DRONE ZATEN İNİŞ YAPMIŞ OLMACAĞ İÇİN HİÇBİR İŞE YARAMAYACAK SADECE GÖREVİN BİTİP BİTMEDİĞİNİ SORGULAYACAĞIMIZ İF İÇİN VAR OLACAK
komut.add(Command(0,0,0,mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,mavutil.mavlink.MAV_CMD_NAV_RTL,0,0,0,0,0,0,0,0,))

komut.upload()
print("Komutlar yükleniyor...")

kalkış(10)#komuttaki takeoff droneu arm etmediği için burada tekrar yazacağız

add_mission()

komut.next=0 #karışıklığı önlemek için en baştan başlasın diye

iha.mode=VehicleMode("AUTO")#AUTO modunda olmazsa verdiğim,z hazır komutları anlamıyor. Biz GUIDED da kullanıyorduk aslında ama o manuel sistem için kullanılor.

while True:
    next_waypoint = komut.next
    print(f"Sıradaki komut{next_waypoint}")
    time.sleep(1)


    if next_waypoint is 4:
     print("Görev başarıyla tamamlandı.")
    
    break


print("Döngüden çıkıldı")
#bu kodu kontrol edebilmek için var


#BUNDAN SONRASI HAREKET FONKSİYONLARI

from dronekit import connect,LocationGlobal,LocationGlobalRelative,LocationLocal,mavlink,mavutil,Vehicle,VehicleMod











