from utils.db import db
from dataclasses import dataclass

@dataclass
class Predio(db.Model):
    id_predio: int
    id_tipo_predio: int
    descripcion: str
    ruc: str
    telefono: str
    correo: str
    direccion: str
    idubigeo: str
    id_persona: int
    url_imagen:str

    id_predio=db.Column(db.Integer, primary_key=True)
    id_tipo_predio=db.Column(db.Integer)
    descripcion=db.Column(db.String(100))
    ruc=db.Column(db.String(60))
    telefono=db.Column(db.String(60))
    correo=db.Column(db.String(60))
    direccion=db.Column(db.String(60))
    idubigeo=db.Column(db.String(60))
    id_persona=db.Column(db.Integer)
    url_imagen=db.Column(db.String(60))

    def __init__(self, id_tipo_predio, descripcion , ruc, telefono, correo, direccion,idubigeo, id_persona, url_imagen):
        self.id_tipo_predio=id_tipo_predio
        self.descripcion=descripcion
        self.ruc=ruc
        self.telefono=telefono
        self.correo=correo
        self.direccion=direccion
        self.idubigeo=idubigeo
        self.id_persona=id_persona
        self.url_imagen=url_imagen
        

    