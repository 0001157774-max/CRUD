import sqlite3

def criar_banco():
    conexao = sqlite3.connect("inventario.db")
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS jogos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        estoque INTEGER NOT NULL,
        valor REAL NOT NULL
    )
    """)

    conexao.commit()
    conexao.close()

    print("Banco criado com sucesso!")


if __name__ == "__main__":
    criar_banco()