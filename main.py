from fastapi import FastAPI
# Aquí importamos el "robot" y las "llaves" de las bases de datos
from database import run_query, get_pedidos_connection, get_aprovisionamiento_connection
from pydantic import BaseModel

# Esto crea un "Schema" personalizado
class Pedido(BaseModel):
    PedidoID: int
    Cliente: str
    CantidadUmv: float

app = FastAPI(title="Mi API de Práctica")

@app.get("/pedidos-resumen")
def obtener_resumen():
    # Añadimos ORDER BY para que ordene por ID de mayor a menor (los últimos creados)
    sql = """
        SELECT PedidoID, Cliente, CantidadUmv, Denominacion 
        FROM pedidospendientes 
        ORDER BY PedidoID DESC 
        LIMIT 10
    """
    return run_query(get_pedidos_connection, sql)

@app.get("/forecast")
def obtener_forecast():
    # La misma lógica, pero cambiando la conexión
    sql = "SELECT * FROM forecast_estandar LIMIT 5"
    return run_query(get_aprovisionamiento_connection, sql)
# Añadimos una nueva ruta para buscar un pedido específico por su ID
@app.get("/pedido/{pedido_id}")
def obtener_pedido_por_id(pedido_id: int):
    """Busca un pedido específico usando su ID"""
    sql = f"SELECT * FROM pedidospendientes WHERE PedidoID = {pedido_id}"
    resultado = run_query(get_pedidos_connection, sql)
    return resultado
@app.get("/buscar-pedido/{nombre_cliente}")
def buscar_por_cliente(nombre_cliente: str):
    """
    Busca todos los pedidos de un cliente específico.
    Escribe el nombre (o parte de él) en la web de /docs.
    """
    # Usamos LIKE para que si escribes 'Zer' te encuentre 'Zermatt'
    sql = f"SELECT * FROM pedidospendientes WHERE Cliente LIKE '%{nombre_cliente}%' LIMIT 20"
    
    resultado = run_query(get_pedidos_connection, sql)
    
    # Si no encuentra nada, avisamos
    if not resultado:
        return {"mensaje": f"No se encontraron pedidos para: {nombre_cliente}"}
        
    return resultado
if __name__ == "__main__":
    import os

    import uvicorn

    uvicorn.run(
        "app:app",
        host=DEPLOY_HOST,
        port=DEPLOY_PORT,
        reload=True,
    )