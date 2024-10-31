
def Presion(FuerzaTotal,Area):
    Presion=FuerzaTotal/Area
    return Presion

def FuerzaTotal(Pabs,Area):
    Ftotal=Pabs*Area 
    return Ftotal

def PresionAbsoluta(Pman,Patm):
    Pabs = Pman + Patm
    return Pabs
