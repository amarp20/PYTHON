import pymongo

cliente = pymongo.MongoClient("mongodb://admin:admin123@localhost:27017/?authSource=admin") 

db=cliente["banco"]
cuentas=db["cuentas"]

def transferencia(monto, de, a):
    with cliente.start_session() as sesion:
        with sesion.start_transaction():
            try:
                cuenta_origen=cuentas.find_one({"usuario":de})
                if cuenta_origen["saldo"] < monto:
                    raise Exception("Saldo insuficiente para realizar la transferencia.")
                cuentas.update_one({"usuario": de}, {"$inc": {"saldo": -monto}}, session=sesion)
                cuentas.update_one({"usuario": a}, {"$inc": {"saldo": monto}}, session=sesion)
                sesion.commit_transaction()
                print(f"Transferencia de {monto} realizada de {de} a {a} con éxito.")
            except Exception as e:
                sesion.abort_transaction()
                print(f"Error en la transferencia: {e}. Se ha revertido la transferencia.")
                
test_monto = 500
test_origen = "Juan"
test_destino = " Maria"
transferencia(test_monto, test_origen, test_destino)
                