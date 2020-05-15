### BONUS AUFGABE ###

import math
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.use("TkAgg")

while True:
    try:
        h01 = int(input("Bitte geben Sie H01 ein! (in KM): "))
    except ValueError:
        print("Ich nehme an, Sie wollten 10 KM schreiben...")
        h01 = 10
        break
    else:
        if(h01 < 0):
            print("Du bist seit lange tot")
        elif(h01 > 150):
            print("Du willst zu hoch fliegen...so müsstest du die Sinkphase anfangen, bevor du mit der Steigphase fertig bist")
        else:
            break

while True:
    try:
        h02 = int(input("Bitte geben Sie H02 ein! (in KM): "))
    except ValueError:
        print("Ich nehme an, Sie wollten 10 KM schreiben...")
        h02 = 10
        break
    else:
        if(h02 < 0):
            print("Du bist seit lange tot")
        elif(h02 > 150):
            print("Du willst zu hoch fliegen...so müsstest du die Sinkphase anfangen, bevor du mit der Steigphase fertig bist")
        else:
            break
while True:
    try:
        h03 = int(input("Bitte geben Sie H03 ein! (in KM): "))
    except ValueError:
        print("Ich nehme an, Sie wollten 10 KM schreiben...")
        h03 = 10
        break
    else:
        if(h03 < 0):
            print("Du bist seit lange tot")
        elif(h03 > 150):
            print("Du willst zu hoch fliegen...so müsstest du die Sinkphase anfangen, bevor du mit der Steigphase fertig bist")
        else:
            break


### ich muss t1,2,3 fuer alle Fluege berechnen!

s1 = 936
s2 = 625
s3 = 936

a1 = 25
a2 = 15
a3 = 25

b1 = 25
b2 = 20
b3 = 15

v1 = 700
v2 = 750
v3 = 650

# bei der t variabeln bedeutet steht s fuer Steigphase, f fuer Flugphase und si fuer Sinkphase


def strecke_steigphase(h, a):
    strecke_steigphase = h / math.sin(math.radians(a))
    return strecke_steigphase


def strecke_sinkphase(h, b):
    strecke_sinkphase = h / math.sin(math.radians(b))
    return strecke_sinkphase


def strecke_steigphase_horizontal(strecke_steigphase, a):
    return math.cos(math.radians(a)) * strecke_steigphase


def strecke_sinkphase_horizontal(h, b):
    return h/math.tan(math.radians(b))


def strecke_flugphase(s, strecke_steigphase_horizontal, strecke_sinkphase_horizontal):
    return s - (strecke_steigphase_horizontal + strecke_sinkphase_horizontal)


def dauer(strecke, v):
    return strecke/v


t1_s = dauer(strecke_steigphase(h01,a1),v1)
t2_s = dauer(strecke_steigphase(h02,a2),v2)
t3_s = dauer(strecke_steigphase(h03,a3),v3)

t1_si = dauer(strecke_sinkphase(h01,b1),v1)
t2_si = dauer(strecke_sinkphase(h02,b2),v2)
t3_si = dauer(strecke_sinkphase(h03,b3),v3)

t1_f = dauer(strecke_flugphase(s1,strecke_steigphase_horizontal(strecke_steigphase(h01,a1),a1),strecke_sinkphase_horizontal(h01,b1)),v1)
t2_f = dauer(strecke_flugphase(s2,strecke_steigphase_horizontal(strecke_steigphase(h02,a2),a2),strecke_sinkphase_horizontal(h02,b2)),v2)
t3_f = dauer(strecke_flugphase(s3,strecke_steigphase_horizontal(strecke_steigphase(h03,a3),a3),strecke_sinkphase_horizontal(h03,b3)),v3)

print(t1_s + t1_f + t1_si)
print(t2_s + t2_f + t2_si)
print(t3_s + t3_f + t3_si)

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

plt.plot([0, strecke_steigphase_horizontal(strecke_steigphase(h01,a1),a1), strecke_sinkphase_horizontal(h01, b1) + strecke_flugphase(s1,strecke_steigphase_horizontal(strecke_steigphase(h01,a1),a1),strecke_sinkphase_horizontal(h01, b1)), s1], [0, h01, h01, 0])
plt.plot([0, strecke_steigphase_horizontal(strecke_steigphase(h02,a2),a2), strecke_sinkphase_horizontal(h02, b2) + strecke_flugphase(s2,strecke_steigphase_horizontal(strecke_steigphase(h02,a2),a2),strecke_sinkphase_horizontal(h02, b2)), s2], [0, h02, h02, 0])
plt.plot([0, strecke_steigphase_horizontal(strecke_steigphase(h03,a3),a3), strecke_sinkphase_horizontal(h03, b3) + strecke_flugphase(s3,strecke_steigphase_horizontal(strecke_steigphase(h03,a3),a3),strecke_sinkphase_horizontal(h03, b3)), s3], [0, h03, h03, 0])

plt.xlabel('Strecke [km]')
plt.ylabel('Flughöhe [km]')
plt.show()



x = np.linspace(0, 0.001, 2)
y = np.sin(x)

plt.ion()

i = 0

while i < 1.856:
    plt.plot([0, strecke_steigphase_horizontal(strecke_steigphase(h01, a1), a1),
              strecke_sinkphase_horizontal(h01, b1) + strecke_flugphase(s1, strecke_steigphase_horizontal(
                  strecke_steigphase(h01, a1), a1), strecke_sinkphase_horizontal(h01, b1)), s1], [0, h01, h01, 0])
    plt.plot([0, strecke_steigphase_horizontal(strecke_steigphase(h02, a2), a2),
              strecke_sinkphase_horizontal(h02, b2) + strecke_flugphase(s2, strecke_steigphase_horizontal(
                  strecke_steigphase(h02, a2), a2), strecke_sinkphase_horizontal(h02, b2)), s2], [0, h02, h02, 0])
    plt.plot([0, strecke_steigphase_horizontal(strecke_steigphase(h03, a3), a3),
              strecke_sinkphase_horizontal(h03, b3) + strecke_flugphase(s3, strecke_steigphase_horizontal(
                  strecke_steigphase(h03, a3), a3), strecke_sinkphase_horizontal(h03, b3)), s3], [0, h03, h03, 0])

    if i <= t1_s + t1_f + t1_si:
        plt.plot(leange(h01, v1, i, a1, b1, t1_s, t1_f, t1_si),hoehe(h01, v1, i , a1, b1, t1_s, t1_f, t1_si), 'ro')
    if i > t1_s + t1_f + t1_si:
        plt.plot(leange(h01, v1, t1_s + t1_f + t1_si, a1, b1, t1_s, t1_f, t1_si), hoehe(h01, v1, t1_s + t1_f + t1_si, a1, b1, t1_s, t1_f, t1_si), 'ro')
    if i >= 0.083 and i - 0.083 <= t2_s + t2_f + t2_si :
        plt.plot(leange(h02, v2, i - 0.083, a2, b2, t2_s, t2_f, t2_si), hoehe(h02, v2, i - 0.083, a2, b2, t2_s, t2_f, t2_si), 'bo')
    if i - 0.083 > t2_s + t2_f + t2_si :
        plt.plot(leange(h02, v2, t2_s + t2_f + t2_si, a2, b2, t2_s, t2_f, t2_si), hoehe(h02, v2, t2_s + t2_f + t2_si, a2, b2, t2_s, t2_f, t2_si), 'bo')
    if i >= 0.4 and i - 0.4 <= t3_s + t3_f + t3_si:
        plt.plot(leange(h03, v3, (t3_s + t3_f + t3_si) - (i - 0.4), a3, b3, t3_s, t3_f, t3_si), hoehe(h03, v3, (t3_s + t3_f + t3_si) - (i - 0.4), a3, b3, t3_s, t3_f, t3_si), 'go')
    if i - 0.4 > t3_s + t3_f + t3_si:
        plt.plot(leange(h03, v3, 0.001, a3, b3, t3_s, t3_f, t3_si), hoehe(h03, v3, 0.001, a3, b3, t3_s, t3_f, t3_si), 'go')
    plt.draw()
    plt.pause(0.005)
    plt.clf()
    i = i + 0.005