from flask import Blueprint, request, jsonify
from model.predio import Predio
from utils.db import db

predios=Blueprint('predios', __name__)

@predios.route('/predios/v1', methods=['GET'])
def getMensaje():
    result={}
    result["data"]='flask-crud-backend'
    return jsonify(result)

@predios.route('/predios/v1/list', methods=['GET'])
def getPredios():
    result={}
    predios=Predio.query.all()
    result["data"]=predios
    result["status_code"]=200
    result["msg"]="Se recupero los predios si inconvenientes"
    return jsonify(result), 200

@predios.route('/predios/v1/insert', methods=['POST'])
def insert():
    result={}
    body=request.get_json()
    id_tipo_predio=body.get('id_tipo_predio')
    descripcion=body.get('descripcion')
    ruc=body.get('ruc')
    telefono=body.get('telefono')
    correo=body.get('correo')
    direccion=body.get('direccion')
    idubigeo=body.get('idubigeo')
    id_persona=body.get('id_persona')
    url_imagen=body.get('url_imagen')

    if not id_tipo_predio or not descripcion or not ruc or not telefono or not correo or not direccion or not idubigeo or not id_persona or not url_imagen:
        result["status_code"]=400
        result["msg"]="Faltan datos"
        return jsonify(result), 400
    
    predio = Predio(id_tipo_predio, descripcion, ruc, telefono, correo, direccion, idubigeo, id_persona, url_imagen)
    db.session.add(predio)
    db.session.commit()
    result["data"]=predio
    result["status_code"]=201
    result["msg"]="Se agrego los datos"
    return jsonify(result),201


@predios.route('/predios/v1/update', methods=['POST'])
def update():
    flag = False
    result = {}
    body = request.get_json()
    id_predio = body.get('id_predio')
    
    if not id_predio:
        result["status_code"] = 400
        result["msg"] = "Se requiere el ID del predio"
        return jsonify(result), 400
    
    predio = Predio.query.get(id_predio)
    
    if not predio:
        result['status_code'] = 400
        result["msg"] = "Predio no existe"
        return jsonify(result), 400
    
    fields_to_update = ['id_tipo_predio', 'descripcion', 'ruc', 'telefono', 'correo', 'direccion', 'idubigeo', 'id_persona', 'url_imagen']
    
    for field in fields_to_update:
        if field in body:
            setattr(predio, field, body[field])
            flag = True
    
    if not flag:
        result['status_code'] = 400
        result["msg"] = "Se requiere al menos un campo a modificar."
        return jsonify(result), 400


    db.session.commit()
    
    result["data"] = predio
    result["status_code"] = 202
    result["msg"] = "Predio modificado"
    return jsonify(result), 202


@predios.route('/predios/v1/delete', methods=['POST'])
def delete():
    result={}
    body=request.get_json()
    id_predio=body.get('id_predio')
    if not id_predio:
        result['status_code']=400
        result["msg"]="Debe consignar un id"
        return jsonify(result),400
    
    predio=Predio.query.get(id_predio)
    if not predio:
        result["status_code"]=400
        result["msg"]="Predio no existe"
        return jsonify(result),400
    
    db.session.delete(predio)
    db.session.commit()

    result["data"]=predio
    result['status_code']=200
    result["msg"]="Predio eliminado"
    return jsonify(result),200