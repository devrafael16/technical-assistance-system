import sqlite3
from typing import Any
from typing import Any

def criar_tabelas() -> None:

    conexao: sqlite3.Connection = sqlite3.connect('assistencia.db')
    cursor: sqlite3.Cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cpf TEXT NOT NULL,
        telefone TEXT NOT NULL,
        endereco TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ordens_servico(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        numero_os TEXT NOT NULL,
        cliente TEXT NOT NULL,
        aparelho TEXT NOT NULL,
        marca_modelo TEXT NOT NULL,
        senha_aparelho TEXT NOT NULL,
        defeito TEXT NOT NULL,
        status TEXT NOT NULL,
        valor REAL,
        observacoes TEXT,
        data_entrada TEXT NOT NULL
    )
    """)

    conexao.commit()

    conexao.close()

def salvar_cliente(nome, cpf, telefone, endereco) -> None:

    conexao: sqlite3.Connection = sqlite3.connect('assistencia.db')
    cursor: sqlite3.Cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO clientes
    (nome, cpf, telefone, endereco)
    VALUES (?, ?, ?, ?)
    """, (nome, cpf, telefone, endereco))

    conexao.commit()
    conexao.close()

def listar_clientes() -> list[Any]:

    conexao: sqlite3.Connection = sqlite3.connect('assistencia.db')
    cursor: sqlite3.Cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM clientes
    """)

    clientes: list[Any] = cursor.fetchall()

    conexao.close()

    return clientes

def salvar_os(
        numero_os,
        cliente,
        aparelho,
        marca_modelo,
        senha_aparelho,
        defeito,
        status,
        valor,
        observacoes,
        data_entrada
):
    
    conexao: sqlite3.Connection = sqlite3.connect('assistencia.db')
    cursor: sqlite3.Cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO ordens_servico
    (numero_os, cliente, aparelho, marca_modelo, senha_aparelho, defeito, status, valor, observacoes, data_entrada)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (numero_os, cliente, aparelho, marca_modelo, senha_aparelho, defeito, status, valor, observacoes, data_entrada))

    conexao.commit()
    conexao.close()


def listar_os():
    
    conexao: sqlite3.Connection = sqlite3.connect('assistencia.db')
    cursor: sqlite3.Cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM ordens_servico
    """)

    ordens = cursor.fetchall()
    conexao.close()
    return ordens


def buscar_os_numero(numero_os):

    conexao = sqlite3.connect("assistencia.db")
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT * FROM ordens_servico
        WHERE numero_os = ?
    """, (numero_os,))

    os_encontrada = cursor.fetchone()
    conexao.close()

    return os_encontrada


def buscar_os_nome(nome_cliente):

    conexao = sqlite3.connect("assistencia.db")
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT * FROM ordens_servico
        WHERE cliente LIKE ?
    """, (f"%{nome_cliente}%",))

    ordens = cursor.fetchall()
    conexao.close()

    return ordens



if __name__ == '__main__':

    criar_tabelas()

    
    