from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# CMudando a configuração do banco para SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventario.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Criando o objeto db que gerencia as conexões, sessões e queries
db = SQLAlchemy(app)


# Criando uma classe que representa a tabela jogos, substitui o sql manual
class Jogo(db.Model):
    __tablename__ = 'jogos'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    estoque = db.Column(db.Integer, default=0)
    valor = db.Column(db.Float, nullable=False)

    # Método para auxiliar a conversão em json
    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "estoque": self.estoque,
            "valor": self.valor
        }


# Criando as tabelas automaticamente
with app.app_context():
    db.create_all()


# Antigo GET
@app.route("/jogos", methods=["GET"])
@app.route("/jogos/<int:id_jogo>", methods=["GET"])
def obter_jogos(id_jogo=None):

    if id_jogo:
        # antes usava select manual, agora usa ORM
        jogo = Jogo.query.get(id_jogo)

        if not jogo:
            return jsonify({"erro": "Jogo não encontrado"}), 404

        return jsonify(jogo.to_dict())

    jogos = Jogo.query.all()
    return jsonify([j.to_dict() for j in jogos])


# Antigo porst para criar os jogos
@app.route("/jogos", methods=["POST"])
def adicionar_jogo():

    dados = request.get_json()

    novo_jogo = Jogo(
        titulo=dados.get("titulo"),
        estoque=dados.get("estoque"),
        valor=dados.get("valor")
    )

    # Antes executava SQL INSERT
    # Agora adiciona direto na sessão
    db.session.add(novo_jogo)
    db.session.commit()

    return jsonify({"msg": "Jogo adicionado", "id": novo_jogo.id}), 201


# Antigo PUT para editar os jogos
@app.route("/jogos/<int:id_jogo>", methods=["PUT"])
def editar_jogo(id_jogo):

    jogo = Jogo.query.get(id_jogo)

    if not jogo:
        return jsonify({"erro": "Jogo não encontrado"}), 404

    dados = request.get_json()

    # Atualiza os campos sem necessitar de SQL manual
    jogo.titulo = dados.get("titulo", jogo.titulo)
    jogo.estoque = dados.get("estoque", jogo.estoque)
    jogo.valor = dados.get("valor", jogo.valor)

    db.session.commit()

    return jsonify({"msg": "Atualizado com sucesso"})


# Antigo delete para remover os jogos
@app.route("/jogos/<int:id_jogo>", methods=["DELETE"])
def remover_jogo(id_jogo):

    jogo = Jogo.query.get(id_jogo)

    if not jogo:
        return jsonify({"erro": "Jogo não encontrado"}), 404

    db.session.delete(jogo)
    db.session.commit()

    return jsonify({"msg": f"Jogo '{jogo.titulo}' removido"})


if __name__ == "__main__":
    app.run(debug=True)