## RPI3GPIO Roll of roof
**Remote Roll of roof service**

Jest to skrypt za pomocą którego możemy zautomatyzować zamykanie dachu
w naszym obserwatorium.

## JAK TO DZIAŁA

RPI3(serwer) z ośmio przekaźnikowym mudułem (SRD-05VDC-SL-C) łączy się po sieci LAN z drugim RPI3(setup), na którym uruchomiony
jest Kstars+Ekos. 

Skrypt w pętli sprawdza pozycje enkoderów silników krokowych
> 'indi_getprop -1 -h 192.168.1.10 -p 7624 "EQMod Mount.CURRENTSTEPPERS.DEStepsCurrent"'

i porównuje z pozycją silników zapizaną w zmiennej
> DE = "7504887"   i    RA = "10530800"

Jeżeli parametry się zgadzają
> if DE == parkDE and RA == parkRA:

zostaje uruchomiona funkcja roof
> def roof():
