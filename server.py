from fastapi import FastAPI
import psycopg2

app = FastAPI()


@app.get("/retoibm/sumar/{sumando01}/{sumando02}")
async def read_item(sumando01 : int,sumando02 : int):
    resultado=sumando01 + sumando02
    insertar(sumando01, sumando02, resultado)
    return {resultado}
    
def insertar(var1, var2, var3):
    conn = psycopg2.connect(user="postgres", password="root", host="0.0.0.0", port="5432", database="my_database")
    mycursor=conn.cursor()
    sql="INSERT INTO sumar_enteros VALUES (%s,%s,%s)"
    datos=(var1, var2, var3)
    mycursor.execute(sql, datos)
    conn.close()