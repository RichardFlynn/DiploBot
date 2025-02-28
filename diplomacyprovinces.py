
import random

class prov:
    def __init__(self,name_in,sc_in):
        self.name = name_in
        self.armyConnections = []
        self.fleetConnections = []
        self.sc = sc_in
        self.occupied = False
        self.control = None

    def getName(self):
        return self.name

    def getConnections(self):
        print(self.name,"is connected by land to")
        for p in self.armyConnections:
            print(p.getName())
        print(self.name,"is connected by sea to")
        for p in self.fleetConnections:
            print(p.getName())

provs = []

london = prov("london",True)
wales = prov("wales",False)
york = prov("york",False)
liverpool = prov("liverpool",True)
edinburgh = prov("edinburgh",True)
clyde = prov("clyde",False)

paris = prov("paris",True)
brest = prov("brest",True)
marseilles = prov("marseilles",True)
picardy = prov("picardy",False)
burgundy = prov("burgundy",False)
gascony = prov("gascony",False)

berlin = prov("berlin",True)
kiel = prov("kiel",True)
munich = prov("munich",True)
prussia = prov("prussia",False)
ruhr = prov("ruhr",False)
silesia = prov("silesia",False)

vienna = prov("vienna",True)
budapest = prov("budapest",True)
trieste = prov("trieste",True)
galicia = prov("galicia",False)
tyrolia = prov("tyrolia",False)
bohemia = prov("bohemia",False)

rome = prov("rome",True)
venice = prov("venice",True)
naples = prov("naples",True)
apulia = prov("apulia",False)
tuscany = prov("tuscany",False)
piedmont = prov("piedmont",False)

moscow = prov("moscow",True)
sevastapol = prov("sevastapol",True)
stpetersburg = prov("st petersburg",True)
warsaw = prov("warsaw",True)
ukraine = prov("ukraine",False)
livonia = prov("livonia",False)
finland = prov("finland",False)

constantinople = prov("constantinople",True)
smyrna = prov("smyrna",True)
ankara = prov("ankara",True)
armenia = prov("armenia",False)
syria = prov("syria",False)

romania = prov("romania",True)
serbia = prov("serbia",True)
greece = prov("greece",True)
bulgaria = prov("bulgaria",True)

belgium = prov("belgium",True)
holland = prov("holland",True)

denmark = prov("denmark",True)
sweden = prov("sweden",True)
norway = prov("norway",True)

spain = prov("spain",True)
portugal = prov("portugal",True)

tunis = prov("tunis",True)
northafrica = prov("north africa",False)
albania = prov("albania",False)

provs = [london,wales,york,liverpool,edinburgh,clyde]
provs += [paris,brest,marseilles,picardy,burgundy,gascony]
provs += [berlin,kiel,munich,prussia,ruhr,silesia]
provs += [vienna,budapest,trieste,galicia,tyrolia,bohemia]
provs += [rome,venice,naples,apulia,tuscany,piedmont]
provs += [moscow,sevastapol,stpetersburg,warsaw,ukraine,livonia,finland]
provs += [constantinople,smyrna,ankara,armenia,syria]
provs += [romania,serbia,greece,bulgaria]
provs += [belgium,holland]
provs += [denmark,sweden,norway]
provs += [spain,portugal]
provs += [tunis,northafrica,albania]


london.armyConnections=[wales,york]
london.fleetConnections=[wales,york]
wales.armyConnections=[london,liverpool,york]
wales.fleetConnections=[london,liverpool]
york.armyConnections=[london,liverpool,edinburgh,wales]
york.fleetConnections=[london,edinburgh]
liverpool.armyConnections=[wales,york,clyde,edinburgh]
liverpool.fleetConnections=[wales,clyde]
edinburgh.armyConnections=[clyde,york,liverpool]
edinburgh.fleetConnections=[clyde,york]
clyde.armyConnections=[liverpool,edinburgh]
clyde.fleetConnections=[liverpool,edinburgh]


paris.armyConnections=[brest,gascony,burgundy,picardy]
paris.fleetConnections=[]
brest.armyConnections=[gascony,paris,picardy]
brest.fleetConnections=[gascony,picardy]
marseilles.armyConnections=[gascony,burgundy,piedmont,spain]
marseilles.fleetConnections=[piedmont,spain]
picardy.armyConnections=[brest,paris,belgium,burgundy]
picardy.fleetConnections=[brest,belgium]
burgundy.armyConnections=[paris,marseilles,picardy,belgium,ruhr,munich,gascony]
burgundy.fleetConnections=[]
gascony.armyConnections=[brest,paris,marseilles,spain,burgundy]
gascony.fleetConnections=[brest,marseilles,spain]

berlin.armyConnections=[kiel,prussia,silesia,munich]
berlin.fleetConnections=[kiel,prussia]
kiel.armyConnections=[denmark,berlin,munich,holland,ruhr]
kiel.fleetConnections=[denmark,berlin,holland]
munich.armyConnections=[kiel,berlin,ruhr,silesia,bohemia,tyrolia]
munich.fleetConnections=[]
prussia.armyConnections=[berlin,livonia,warsaw,silesia]
prussia.fleetConnections=[berlin,livonia]
ruhr.armyConnections=[berlin,holland,kiel,burgundy,munich]
ruhr.fleetConnections=[]
silesia.armyConnections=[berlin,prussia,warsaw,galicia,munich,bohemia]
silesia.fleetConnections=[]

vienna.armyConnections=[tyrolia,bohemia,budapest,trieste,galicia]
vienna.fleetConnections=[]
budapest.armyConnections=[vienna,galicia,romania,serbia,trieste]
budapest.fleetConnections=[]
trieste.armyConnections=[venice,vienna,budapest,albania,serbia]
trieste.fleetConnections=[venice,albania]
galicia.armyConnections=[silesia,warsaw,vienna,budapest,ukraine,romania,bohemia]
galicia.fleetConnections=[]
tyrolia.armyConnections=[munich,venice,piedmont,vienna,bohemia,trieste]
tyrolia.fleetConnections=[]
bohemia.armyConnections=[tyrolia,vienna,galicia,munich,silesia]
bohemia.fleetConnections=[]

rome.armyConnections=[naples,apulia,venice,tuscany]
rome.fleetConnections=[naples,tuscany]
venice.armyConnections=[tuscany,piedmont,tyrolia,trieste,apulia]
venice.fleetConnections=[apulia,trieste]
naples.armyConnections=[apulia,rome]
naples.fleetConnections=[apulia,rome]
apulia.armyConnections=[venice,rome,naples]
apulia.fleetConnections=[venice,naples]
tuscany.armyConnections=[rome,piedmont,venice]
tuscany.fleetConnections=[rome,piedmont]
piedmont.armyConnections=[marseilles,tuscany,venice,tyrolia]
piedmont.fleetConnections=[marseilles,tuscany]

moscow.armyConnections=[stpetersburg,sevastapol,warsaw,livonia]
moscow.fleetConnections=[]
sevastapol.armyConnections=[armenia,romania,ukraine,moscow]
sevastapol.fleetConnections=[armenia,romania]
stpetersburg.armyConnections=[finland,norway,moscow,livonia]
stpetersburg.fleetConnections=[finland,norway,livonia]
warsaw.armyConnections=[livonia,moscow,ukraine,galicia,silesia,prussia]
warsaw.fleetConnections=[]
ukraine.armyConnections=[moscow,sevastapol,warsaw,galicia,romania]
ukraine.fleetConnections=[]
livonia.armyConnections=[stpetersburg,warsaw,moscow,prussia]
livonia.fleetConnections=[stpetersburg,prussia]
finland.armyConnections=[sweden,norway,stpetersburg]
finland.fleetConnections=[sweden,stpetersburg]

constantinople.armyConnections=[bulgaria,smyrna,ankara]
constantinople.fleetConnections=[bulgaria,smyrna,ankara]
smyrna.armyConnections=[ankara,constantinople,syria]
smyrna.fleetConnections=[constantinople,syria]
ankara.armyConnections=[constantinople,smyrna,armenia]
ankara.fleetConnections=[constantinople,armenia]
armenia.armyConnections=[syria,ankara,sevastapol]
armenia.fleetConnections=[ankara,sevastapol]
syria.armyConnections=[armenia,ankara,smyrna]
syria.fleetConnections=[smyrna]

romania.armyConnections=[bulgaria,serbia,budapest,ukraine,sevastapol,galicia]
romania.fleetConnections=[bulgaria,sevastapol]
serbia.armyConnections=[vienna,trieste,albania,greece,romania,bulgaria]
serbia.fleetConnections=[]
greece.armyConnections=[albania,serbia,bulgaria]
greece.fleetConnections=[albania,bulgaria]
bulgaria.armyConnections=[constantinople,greece,serbia,romania]
bulgaria.fleetConnections=[constantinople,greece,romania]

belgium.armyConnections=[picardy,burgundy,holland,ruhr]
belgium.fleetConnections=[picardy,holland]
holland.armyConnections=[belgium,ruhr,kiel]
holland.fleetConnections=[belgium,kiel]

denmark.armyConnections=[sweden,kiel]
denmark.fleetConnections=[sweden,kiel]
sweden.armyConnections=[denmark,norway,finland]
sweden.fleetConnections=[denmark,norway,finland]
norway.armyConnections=[finland,stpetersburg,sweden]
norway.fleetConnections=[stpetersburg,sweden]

spain.armyConnections=[portugal,marseilles,gascony]
spain.fleetConnections=[portugal,marseilles,gascony]
portugal.armyConnections=[spain]
portugal.fleetConnections=[spain]

tunis.armyConnections=[northafrica]
tunis.fleetConnections=[northafrica]
northafrica.armyConnections=[tunis]
northafrica.fleetConnections=[tunis]
albania.armyConnections=[greece,serbia,trieste]
albania.fleetConnections=[greece,trieste]

class unit:

    def __init__(self,type_in,prov_in):
        self.type=type_in
        self.prov=prov_in

    def plan(self):
        if self.type==a:
            return random.choice(self.prov.armyConnections)
        else:
            return random.choice(self.prov.fleetConnections)

    def move(self,prov_in):
        if self.type==a:
            if prov_in in self.prov.armyConnections:
                self.prov.occupied=False
                self.prov = prov_in
                self.prov.occupied=True
            else:
                print("error")
        else:
            if prov_in in self.prov.fleetConnections:
                self.prov.occupied=False
                self.prov = prov_in
                self.prov.occupied=True
            else:
                print("error")
        

class power:

    def __init__(self,name_in):
        self.name=name_in
        self.units=[]
        self.centres=0
        self.home=[]

f="fleet"
a="army"

england = power("england")
france = power("france")
germany = power("germany")
austria = power("austria")
italy = power("italy")
russia = power("russia")
turkey = power("turkey")

#powers = [england,france,germany,austria,italy,russia,turkey]
powers = [france,austria]

#england.units=[unit(f,edinburgh),unit(f,london),unit(a,liverpool)]
france.units=[unit(f,brest),unit(a,paris),unit(a,marseilles)]
#germany.units=[unit(f,kiel),unit(a,berlin),unit(a,munich)]
austria.units=[unit(f,trieste),unit(a,vienna),unit(a,budapest)]
#italy.units=[unit(f,naples),unit(a,rome),unit(a,venice)]
#russia.units=[unit(f,stpetersburg),unit(a,moscow),unit(a,warsaw),unit(f,sevastapol)]
#turkey.units=[unit(f,ankara),unit(a,constantinople),unit(a,smyrna)]

for p in powers:
    for u in p.units:
        u.prov.occupied=True
        u.prov.control=p
        p.centres+=1
        p.home.append(u.prov)

def gamestate():
    for p in powers:
        print(p.name + ":")
        for u in p.units:
            print(u.prov.name)
        print()

def move(power,prov1,prov2):
    for u in power.units:
        if u.prov==prov1:
            u.move(prov2)
            return

phase = 0

def turn():
    global phase
    phase+=1
    moves = []
    dupes = {}
    for p in provs:
        dupes[p]=0
    #print(dupes)
    for p in powers:
        for u in p.units:
            moves.append((u,u.plan()))
            #print(moves[-1][0].prov.name,moves[-1][1].name)
            dupes[moves[-1][1]]+=1

    #print(dupes)

    valid_moves=[]
    
    while len(moves)>0:
        #print(len(moves))
        for m in moves:
            
            #print()
            #print("evaluating",m[0].prov.name)
            if dupes[m[1]]==0:
                print("error")
            elif dupes[m[1]]>1:
                print(m[0].prov.name,"bounced in",m[1].name)
                moves.remove(m)
            else:
                if not m[1].occupied:
                    moves.remove(m)
                    print(m[0].prov.name,"moved to",m[1].name)
                    m[0].move(m[1])
                else:
                    invalid = True
                    for mv in moves:
                        if mv[0].prov==m[1]:
                            if mv[1]==m[0].prov:
                                print(mv[0].prov.name,"failed to move to occupied",mv[1].name)
                                moves.remove(mv)
                            else:
                                invalid=False
                    if invalid:
                        print(m[0].prov.name,"failed to move to occupied",m[1].name)
                        moves.remove(m)
    print("Phase",phase)
    if phase%2==0:
        builds()


def evaluate(m):
    pass

def dturn():
    turn()
    turn()


def builds():
    for p in powers:
        for u in p.units:
            if u.prov.sc:
                if u.prov.control != p:
                    if u.prov.control != None:
                        u.prov.control.centres-=1
                    u.prov.control = p
                    p.centres+=1

    for p in powers:
        print(p.centres)
        while p.centres<len(p.units):
            temp = random.randint(0,len(p.units)-1)
            p.units[temp].prov.occupied=False
            del p.units[temp]
        hc = []
        for c in p.home:
            if c.control==p and not c.occupied:
                hc+=[c]
        while p.centres>len(p.units) and len(hc)>0:
            temp = random.choice(hc)
            p.units.append(unit(a,temp))
            temp.occupied=True
            hc.remove(temp)
    
        
    print("builds")


