
def Presion(FuerzaTotal,Area):
    Presion=FuerzaTotal/Area,2
    return Presion

def FuerzaTotal(Pabs,Area):
    Ftotal=Pabs*Area 
    return Ftotal

def PresionAbsoluta(Pman,Patm):
    Pabs = Pman + Patm
    return Pabs
