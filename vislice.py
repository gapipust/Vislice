from model import *
import bottle

vislice = Vislice()

@bottle.get("/")
def index():
    return bottle.template("index.tpl")

@bottle.get("/igra/<id_igre>/")
def nova_igra():
    id_igre = vislice.nova_igra()
    return id_igre

@bottle.post("/igra/<id_igre:int>/")
def pokazi_igro():
    

@bottle.post("/igra/<id_igre:int>/")
def ugibaj()

bottle.run(reloader=True, debug=True)