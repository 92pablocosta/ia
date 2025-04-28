import psycopg2
from datetime import datetime

#conectar bdd

def conectar_bd():
    conn = psycopg2.connect(
        dbname = "faculdade"
        user = "usuario"
        password = "senha"
        host = "localhost"
        port = "5432"
    )
    return conn

#registrar informações

def registrar_aula(curso, periodo, disciplina, professor, data, assunto):
    conn = conectar_bd()
    cur = conn.cursor()

    #registrar curso
    cur.execute("INSERT INTO cursos (nome) VALUES (%s) ON CONFLICT (nome)" \
    " DO NOTHING RETURNING id", (curso,))
    if not curso_id:
        cur.execute("SELECT id FROM cursos WHERE nome = %s", (curso,))
        curso_id = cur.fetchone()[0]

#to be continued....
