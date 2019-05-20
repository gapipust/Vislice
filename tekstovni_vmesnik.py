import model

def izpis_igre(igra):
    return """
        Napačne črke: {}
        Pravilne črke: {}
        Število napak: {}
        Pravilni del gesla: {}
        Nepravilni ugibi: {}
        """.format(igra.napacne_crke(), igra.pravilne_crke(), igra.stevilo_napak(), igra.pravilni_del_gesla(), igra.nepravilni_ugibi())

def izpis_zmage(igra):
    if igra.zmaga():
        return "Čestitke, zmagali ste!"

def izpis_poraza(igra):
    if igra.poraz():
        return "Žal ste bili obešeni :("

def zahtevaj_vnos():
    crka = input("Napiši črko: ")
    return crka.upper()

def pozeni_vmesnik():
    igra = model.nova_igra()
    while True:
        crka = zahtevaj_vnos()
        rezultat = igra.ugibaj(crka)
        if rezultat == model.PONOVLJENA_CRKA:
            print("Ta črka je že bila izbrana. Izberite drugo črko!")
            izpis_igre(igra)
        elif rezultat == model.ZMAGA:
            izpis_zmage(igra)
            break
        elif rezultat == model.PORAZ:
            izpis_poraza(igra)
            break
        elif rezultat == model.PRAVILNA_CRKA:
            igra.pravilne_crke().append(crka)
            izpis_igre(igra)
        elif rezultat == model.NAPACNA_CRKA:
            igra.napacne_crke().append(crka)
            izpis_igre(igra)