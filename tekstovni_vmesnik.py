import model

def izpis_igre(igra):
    return """
        Napačne črke: {}
        Pravilne črke: {}
        Število napak: {}
        Pravilni del gesla: {}
        """.format(igra.napacne_crke(), igra.pravilne_crke(), igra.stevilo_napak(), igra.pravilni_del_gesla())

def izpis_zmage(igra):
    if igra.zmaga():
        return "Čestitke, zmagali ste!"

def izpis_poraza(igra):
    if igra.poraz():
        return "Žal ste bili obešeni :("

def zahtevaj_vnos():
    crka = input("Napiši črko: ")
    return crka

def pozeni_vmesnik():
    