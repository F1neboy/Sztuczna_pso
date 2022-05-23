
import random
from decimal import Decimal
import matplotlib.pyplot as plt

czastki=list()
gb=float('-inf') #global_best
w=1  #Bezłwładność cząsteczki
lr=0.5  #współczynnik uczenia(wielkość skoku uczenia)
cp=0.1  #Dążenie do lokalnego rekordu
cg=0.9  #Dązenie do globalnego rekordu
gbx=0.0 #Wartość x dla global_best
gby=0.0 #Wartość y dla global_best
il=50 #Ilość cząstek
yy=100 #Ilość iteracji pętli PSO

class Czastka():
    def __init__(self):
        self.x=random.uniform(-10,10)
        self.y=random.uniform(-10,10)
        self.vx=0
        self.vy=0
        self.pbx=0
        self.pby=0
        self.f=0.0
        self.pb=float('-inf')

    def SetF(self, f):
        self.f=f

    def SetVx(self, vx):
        self.vx=vx
        return vx

    def SetVy(self, vy):
        self.vy=vy
        return vy


def Booth_func(x, y):
    f=float(Decimal(-1*(((x + 2 * y - 7)**2) + ((2 * x + y - 5)** 2))))
    return f


def Pso(v, w, cp, r1, cg, r2, gb, pb, x):
    pso=float(Decimal((w*v)+(cp*r1*(pb-x))+(cg*r2*(gb-x))))
    return pso

##INICJALIZACJA
for x in range (0, il+1):
    czastki.append(Czastka())
    czastki[x].SetF(Booth_func(czastki[x].x, czastki[x].y))
    if(czastki[x].pb>czastki[x].f):
        czastki[x].SetPb(czastki[x].f)
        czastki[x].pbx=czastki[x].x
        czastki[x].pby=czastki[x].y
    if(gb>czastki[x].pb):
        gb=czastki[x].pb
        mx=czastki[x].pbx
        my=czastki[x].pby



##PĘTLA PSO
for y in range (1, yy):
    for x in range(0, il+1):
        r1 = random.uniform(0, 1)
        r2 = random.uniform(0, 1)
        czastki[x].x+=lr*czastki[x].SetVx(Pso(czastki[x].vx, w, cp, r1, cg, r2, gbx, czastki[x].pbx, czastki[x].x))
        czastki[x].y+=lr*czastki[x].SetVy(Pso(czastki[x].vy, w, cp, r1, cg, r2, gby, czastki[x].pby, czastki[x].y))
        czastki[x].SetF(Booth_func(czastki[x].x,czastki[x].y))
        if(czastki[x].pb<=czastki[x].f):
            czastki[x].pb=czastki[x].f
            czastki[x].pbx=czastki[x].x
            czastki[x].pby=czastki[x].y
        if(czastki[x].pb>gb):
            gb=czastki[x].pb
            mx=czastki[x].pbx
            my=czastki[x].pby
            print("Iteracja ",y,  " najlepszy globalny wynik: ", gb, "Dla wspolrzednych: (", mx, ";", my,")")