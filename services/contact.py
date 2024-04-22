from flask import Blueprint, request, jsonify
from model.contact import Contact
from utils.db import db

contacts=Blueprint('contacts', __name__)

@contacts.route('/contactos/v1', methods=['GET'])
def getMensaje():
    result={}
    result["data"]='flask-crud-backend'
    return jsonify(result)

@contacts.route('/contactos/v1/list', methods=['GET'])
def getContactos():
    result={}
    contactos=Contact.query.all()
    result["data"]=contactos
    result["status_code"]=200
    result["msg"]="Se recupero los contactos si inconvenientes"
    return jsonify(result), 200


# ****************** MY INSERT ******************
# @contacts.route('/contactos/v1/insertxd', methods=['POST'])
# def insert():
#     result = {}
#     bodies = request.get_json()  # Obtener la lista de contactos del cuerpo de la solicitud
    
#     for body in bodies:
#         id = body.get('id')
#         fullname = body.get('fullname')
#         email = body.get('email')
#         phone = body.get('phone')
        
#         # Validaciones de los datos aquí, si es necesario
        
#         contacto = Contact(id, fullname, email, phone)
#         db.session.add(contacto)
    
#     db.session.commit()
    
#     result["status_code"] = 201
#     result["msg"] = "Se agregaron los datos exitosamente"
#     return jsonify(result), 201

@contacts.route('/contactos/v1/insertxd', methods=['POST'])
def insertxd():
    result = {}
    #bodies = request.get_json()  # Obtener la lista de contactos del cuerpo de la solicitud
    
    starting_id = 787  # ID inicial
    
    for idx in range(10):  # Iterar 20 veces para insertar 20 contactos
        id = starting_id + idx
        
        # Obtener datos del cuerpo de la solicitud
        body=request.get_json()
        fullname = body.get('fullname')
        email = body.get('email')
        phone = body.get('phone')
        
        # Validaciones de los datos aquí, si es necesario
        
        contacto = Contact(id, fullname, email, phone)
        db.session.add(contacto)
    
    db.session.commit()
    
    result["status_code"] = 201
    result["msg"] = "Se agregaron los datos exitosamente"
    return jsonify(result), 201



# ****************** END ******************


@contacts.route('/contactos/v1/insert', methods=['POST'])
def insert():
    result={}
    body=request.get_json()
    fullname=body.get('fullname')
    email=body.get('email')
    phone=body.get('phone')

    if not fullname or not email or not phone:
        result["status_code"]=400
        result["msg"]="Faltan datos"
        return jsonify(result),400
    
    contacto=Contact(fullname,email,phone)
    db.session.add(contacto)
    db.session.commit()
    result["data"]=contacto
    result["status_code"]=201
    result["msg"]="Se agrego los datos"
    return jsonify(result),201

@contacts.route('/contactos/v1/update', methods=['POST'])
def update():
    result={}
    body=request.get_json()
    id=body.get('id')
    fullname=body.get('fullname')
    email=body.get('email')
    phone=body.get('phone')

    if not id or not fullname or not email or not phone:
        result["status_code"]=400
        result["msg"]="Faltan datos"
        return jsonify(result),400
    
    contacto=Contact.query.get(id)
    if not contacto:
        result['status_code']=400
        result["msg"]="Contacto no existe"
        return jsonify(result),400
    
    contacto.fulname= fullname
    contacto.email=email
    contacto.phone=phone
    db.session.commit()

    result["data"]=contacto
    result["status_code"]=202
    result["msg"]="se modifico contacto"
    return jsonify(result),202


@contacts.route('/contactos/v1/delete', methods=['POST'])
def delete():
    result={}
    body=request.get_json()
    id=body.get('id')
    if not id:
        result['status_code']=400
        result["msg"]="Debe consignar un id"
        return jsonify(result),400
    
    contacto=Contact.query.get(id)
    if not contacto:
        result["status_code"]=400
        result["msg"]="Contacto no existe"
        return jsonify(result),400
    
    db.session.delete(contacto)
    db.session.commit()

    result["data"]=contacto
    result['status_code']=200
    result["msg"]="se modifico contacto"
    return jsonify(result),200