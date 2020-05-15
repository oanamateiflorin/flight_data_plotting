import math
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use("TkAgg")

while True:
    try:
        h0 = int(input("Bitte geben Sie die Flughöhe ein! (in KM): "))
    except ValueError:
        print("Ich nehme an, Sie wollten 10 KM schreiben...")
        h0 = 10
        break
    else:
        if(h0 < 0):
            print("Du bist seit lange tot")
        elif(h0 > 172):
            print("Du willst zu hoch fliegen...so müsstest du die Sinkphase anfangen, bevor du mit der Steigphase fertig bist")
        else:
            break


strecke_steigphase = h0/math.sin(math.radians(25))
strecke_steigphase_horizontal = math.cos(math.radians(25)) * strecke_steigphase
t1 = strecke_steigphase/800
t1_minuten = t1 * 60
strecke_sinkphase = h0/math.sin(math.radians(30))
t3 = strecke_sinkphase/800
t3_minuten = t3 * 60
strecke_sinkphase_horizontal = h0/math.tan(math.radians(30))
strecke_flugphase = 738 - (strecke_steigphase_horizontal+strecke_sinkphase_horizontal)
print("gesamt(KM): " + str(strecke_steigphase_horizontal+strecke_sinkphase_horizontal+strecke_flugphase))
t2 = strecke_flugphase/800
t2_minuten = t2 * 60
print("Steigphase: "+ str(t1_minuten) + " min |", "Flugphase:" + str(t2_minuten) + " min |", "Sinkphase:"+ str(t3_minuten) + " min")

### UNTERPUNKT B ###

plt.plot([0, strecke_steigphase_horizontal, strecke_sinkphase_horizontal + strecke_flugphase, 738], [0, h0, h0, 0])
plt.xlabel('Strecke [km]')
plt.ylabel('Flughöhe [km]')
plt.show()


### UNTERPUNKT C ###

treibstoffkonsum_steigphase_tonnen_stunde = 5 * (1 + math.sin(math.radians(25)))
treibstoffkonsum_sinkphase_tonnen_stunde = 5 * (1 - math.sin(math.radians(30)))

konsum_steigphase = t1 * treibstoffkonsum_steigphase_tonnen_stunde
konsum_flugphase = 5 * (t2 - t1)
konsum_sinkphase = treibstoffkonsum_sinkphase_tonnen_stunde * t3
plt.plot([0, t1, t1 + t2, t1 + t2 + t3], [0, konsum_steigphase, konsum_steigphase + konsum_flugphase, konsum_steigphase + konsum_flugphase + konsum_sinkphase ])
plt.xlabel('Zeit [h]')
plt.ylabel('Verbrauchter Treibstoff [t]')
plt.show()

### UNTERPUNKT D ###

while True:
    try:
        t_darst_min = float(input("Nach wie viel Zeit von der Abflug wollen Sie die Position des Flugzeuges beobachten ? Dauer des Fluges: " + str(t1_minuten + t2_minuten + t3_minuten) + " min "))
    except ValueError:
        print("Sie haben eine falsche Eingabe eingegeben, sagen wir mal, Sie wollten 14 min schreiben")
        t_darst = 0.3
        break
    else:
        if(t_darst_min > t1_minuten + t2_minuten + t3_minuten):
           t_darst = 0.3
        else:
            t_darst = t_darst_min / 60
            break


def hoehe(h0,v,t,a,b,t1,t2,t3):
    if t < t1:
        return v*t*math.sin(math.radians(a))
    elif t1 <= t < t1+t2:
        return h0
    elif t1 +t2 <= t <= t1 + t2 + t3:
        return h0 - v * (t - t1 - t2) * math.sin(math.radians(b))
def leange(h0,v,t,a,b,t1,t2,t3):
    if t < t1:
        return v*t*math.cos(math.radians(a))
    elif t1 <= t < t1+t2:
        return v * t1 * math.cos(math.radians(a)) + v * (t - t1)
    elif t1 +t2 <= t <= t1 + t2 + t3:
        return v * t1 * math.cos(math.radians(a)) + v * t2 + v * (t - t1 - t2) * math.cos(math.radians(b))

plt.plot([0, strecke_steigphase_horizontal, strecke_sinkphase_horizontal + strecke_flugphase, 738], [0, h0, h0, 0])
plt.plot(leange(h0, 800, t_darst, 25, 30, t1, t2, t3), hoehe(h0, 800, t_darst, 25, 30, t1, t2, t3), 'bo')
plt.text(leange(h0, 800, t1 + t2, 25, 30, t1, t2, t3), hoehe(h0, 800, t1 + t2, 25, 30, t1, t2, t3),'Top of Descent')
plt.text(leange(h0, 800, t1 + t2 + t3 - 0.01, 25, 30, t1, t2, t3), hoehe(h0, 800, t1 + t2 + t3 - 0.01, 25, 30, t1, t2, t3),'Approach Phase')
plt.text(leange(h0, 800, t1 + t2 + t3 - 0.005, 25, 30, t1, t2, t3), hoehe(h0, 800, t1 + t2 + t3 - 0.005, 25, 30, t1, t2, t3),'Landing Phase')
plt.xlabel('Strecke [km]')
plt.ylabel('Flughöhe [km]')
plt.show()
