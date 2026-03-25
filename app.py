from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

DB_NAME = "inventario.db"

def abrir_conexao():
    conexao = sqlite3.connect(DB_NAME)
    conexao.row_factory = sqlite3.Row
    return conexao


def executar(sql, valores=(), retornar=False):
    conexao = abrir_conexao()
    cursor = conexao.cursor()

    resultado = None

    try:
        cursor.execute(sql, valores)

        if retornar:
            resultado = cursor.fetchall()
        else:
            conexao.commit()

    finally:
        conexao.close()

    return resultado

@app.route("/jogos", methods=["GET"])
@app.route("/jogos/<int:id_jogo>", methods=["GET"])
def obter_jogos(id_jogo=None):

    if id_jogo:
        jogo = executar(
            "SELECT * FROM jogos WHERE id = ?",
            (id_jogo,),
            retornar=True
        )

        if not jogo:
            return jsonify({"erro": "Jogo não encontrado"}), 404

        return jsonify(dict(jogo[0]))

    lista = executar("SELECT * FROM jogos", retornar=True)
    return jsonify([dict(item) for item in lista])


@app.route("/jogos", methods=["POST"])
def adicionar_jogo():

    info = request.get_json()

    executar(
        "INSERT INTO jogos (titulo, estoque, valor) VALUES (?, ?, ?)",
        (info["titulo"], info["estoque"], info["valor"])
    )

    return jsonify({"msg": "Jogo adicionado"}), 201


@app.route("/jogos/<int:id_jogo>", methods=["PUT"])
def editar_jogo(id_jogo):

    dados = request.get_json()

    existe = executar(
        "SELECT id FROM jogos WHERE id = ?",
        (id_jogo,),
        retornar=True
    )

    if not existe:
        return jsonify({"erro": "Jogo não encontrado"}), 404

    executar(
        "UPDATE jogos SET titulo = ?, estoque = ?, valor = ? WHERE id = ?",
        (dados["titulo"], dados["estoque"], dados["valor"], id_jogo)
    )

    return jsonify({"msg": "Atualizado com sucesso"})


@app.route("/jogos/<int:id_jogo>", methods=["DELETE"])
def remover_jogo(id_jogo):

    jogo = executar(
        "SELECT titulo FROM jogos WHERE id = ?",
        (id_jogo,),
        retornar=True
    )

    if not jogo:
        return jsonify({"erro": "Jogo não encontrado"}), 404

    executar(
        "DELETE FROM jogos WHERE id = ?",
        (id_jogo,)
    )

    return jsonify({"msg": f"Jogo '{jogo[0]['titulo']}' removido"})
    

if __name__ == "__main__":
    app.run(debug=True)




