# Raspberry-Pi-ile-1.3-inc-Oled-Waveshare-HAT-Ornekleri-ve-Kurulumu
This repository includes translated and modified codes of real owners.
All of these SH1106 HAT examples uses Python3.
-
Merhaba, eger siz de benim gibi ucuza ekran arayip ya da kendi isteginizle bu ekrani ( 1.3 OLED Waveshare HAT) aldiysaniz ve bir türlü calistiramadiysaniz  dogru yerdesiniz. 
Cihazi takip da calistiramayinca bozuk sandim vallahi basta. Ancak sonra uzun süren lehim ve kod kurulumu sonunda yüzüm güldü. 

-Burada bulacaginiz kodlarin tümü baskalari tarafindan yazilmis olup, bazi kodlarin tamami farkli cihazlara yönelik yazildigi icin tarafimdan düzenlenmistir.

-Ben ekrani Raspberry Pi Zero ile kullandim. (Cihazin GPIO cikislarinda Header olmayan versiyon.) Eger sizinkinde de Header yoksa mutlaka "2x20 Erkek Pin Header" da almalisiniz ve bu Headerin kisa uclu olan tarafini Pi Zeroya oturtarak arka tarafindan lehimlemelisiniz. Yoksa temas olmadigi icin calismayacaktir taktiklariniz. Arama motoruna "Pi Zero Header Soldering" yazabilirsiniz veya biraz riskli olan cekicle oturtma teknigi "pi zero header solderless" seklinde arayarak ulasabilirsiniz. 

-Pi Zero'ya "Rasbian" kurulumunuzu yapin, benimkinde önerilen programli olan en büyük boyutlu versiyonu yüklü. 

# Sürücü Kurulumu: (En önemli kisim)
Asagidaki kodlari @pangduckwai github kullanicisinin yazilarindan ekliyorum. Satir satir Terminal icerisine yazip, enterleyip ilerliyoruz. Tabii bekleyin kod yüklenene kadar eger terminal bilginiz yoksa birakin burayi linux terminal basics falan izleyin youtubede. 
###cok önemli! Asagidaki python kelimesi iceren kodlari yazarken kodlarin aynisini python3 olacak sekilde de yazin. Bastakine ben yazdim ama sorun olmamasi icin öneririm.
( Örnegin sudo python setup.py install olan kodu sudo python3 setup.py install seklinde de yazdim ki garanti olsun cünkü biz python3 kullaniyor olacagiz.)

sudo apt-get update

sudo apt-get install python-dev

-Tarayiciyi acip RPi.GPIO yu https://pypi.python.org/pypi/RPi.GPIO adresinden indirin ve Icindekileri klasöre cikartin

Klasörün icine Terminalden girin:

sudo python setup.py install

sudo python3 setup.py install

-Tekrar tarayiciyi acip https://pypi.python.org/pypi/spidev adresinden Spidev indirin ve icini klasöre cikartin.

sudo apt-get install python-smbus

sudo apt-get install python-serial

Terminalden spidev klasörüne girin:

sudo python setup.py install

sudo apt-get install python-imaging

----------------------------------------------

-Simdi ayarlardan portlari acacagiz.

sudo raspi-config

'5 Interfacing Options' Secin

'P4 SPI' Secin

'Yes' deyin

'P5 I2C' Secin

'Yes' deyin

-------------------------

Terminali kapatin ve tekrar acin.

sudo apt-get install python-pip libfreetype6-dev libjpeg-dev

sudo -H pip install --upgrade pip

sudo apt-get purge python-pip

sudo -H pip install --upgrade luma.oled

Bu kadardi. Simdi yapmaniz gereken benim github'dan indirdiklerinizi bir klasör icerisine atin ve kodlari denemeye baslayin. (config.py , SH1106.py sürücü dosyalaridir onlari kullanmayin ancak her klasörde bulunmasi gerekiyor.)
-Örnek kod kullanimi
: sudo python3 time.py


