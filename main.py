from fastapi import FastAPI
import psycopg2
import os
from pydantic import BaseModel

class Evento(BaseModel):
    nome_evento: str
    data_anual: str
    descricao: str
    alcance: int = None
    engajamento: int = None
    status: str = None
    fonte: str = None
    
app = FastAPI()

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("POSTGRES_HOST", "postgres_container"),
        database=os.getenv("POSTGRES_DB", "meubanco"),
        user=os.getenv("POSTGRES_USER", "admingle"),
        password=os.getenv("POSTGRES_PASSWORD", "novasenha123")
    )

@app.get("/")
def read_root():
    return {"status": "API está funcionando!"}

@app.post("/eventos/")
def create_event(evento: Evento):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        sql = """
        INSERT INTO eventos (nome_evento, data_anual, descricao, alcance, engajamento, status, fonte)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        RETURNING id;
        """
        
        cur.execute(sql, (
            evento.nome_evento, 
            evento.data_anual, 
            evento.descricao, 
            evento.alcance, 
            evento.engajamento, 
            evento.status, 
            evento.fonte
        ))
        event_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return {"message": "Evento adicionado com sucesso", "id": event_id}
    except Exception as e:
        return {"error": str(e)}

@app.get("/eventos/")
def list_eventos():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT nome_evento, data_anual, descricao, alcance, engajamento, status, fonte FROM eventos;")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return {"eventos": [dict(zip(["nome_evento", "data_anual", "descricao", "alcance", "engajamento", "status", "fonte"], row)) for row in rows]}
    except Exception as e:
        return {"error": str(e)}

@app.get("/eventos/{nome_evento}")
def get_evento(nome_evento: str):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        sql = """
        SELECT nome_evento, data_anual, descricao, alcance, engajamento, status, fonte
        FROM eventos
        WHERE nome_evento = %s;
        """
        
        cur.execute(sql, (nome_evento,))
        row = cur.fetchone()
        cur.close()
        conn.close()
        
        if row:
            return {
                "nome_evento": row[0],
                "data_anual": row[1],
                "descricao": row[2],
                "alcance": row[3],
                "engajamento": row[4],
                "status": row[5],
                "fonte": row[6]
            }
        else:
            return {"message": "Evento não encontrado"}
    except Exception as e:
        return {"error": str(e)}

@app.put("/eventos/{nome_evento}")
def update_evento(nome_evento: str, evento: Evento):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        sql = """
        UPDATE eventos
        SET nome_evento = %s, data_anual = %s, descricao = %s, alcance = %s, engajamento = %s, status = %s, fonte = %s
        WHERE nome_evento = %s
        RETURNING id;
        """
        
        cur.execute(sql, (
            evento.nome_evento,
            evento.data_anual,
            evento.descricao,
            evento.alcance,
            evento.engajamento,
            evento.status,
            evento.fonte,
            nome_evento
        ))
        
        if cur.rowcount == 0:
            return {"message": "Evento não encontrado"}
        
        event_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        
        return {"message": "Evento atualizado com sucesso", "id": event_id}
    except Exception as e:
        return {"error": str(e)}

@app.delete("/eventos/{nome_evento}")
def delete_evento(nome_evento: str):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        sql = """
        DELETE FROM eventos
        WHERE nome_evento = %s;
        """
        
        cur.execute(sql, (nome_evento,))
        
        if cur.rowcount == 0:
            return {"message": "Evento não encontrado"}
            
        conn.commit()
        cur.close()
        conn.close()
        
        return {"message": "Evento excluído com sucesso"}
    except Exception as e:
        return {"error": str(e)}