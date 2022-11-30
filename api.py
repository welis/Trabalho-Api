from flask import Flask, Response, request
import mysql.connector
import json

#contas a receber
app = Flask(__name__)

# create table itens(
#     id serial primary key,
#     descricao varchar(100),
#     quantidade int,
#     preco float
# );

# create table venda(
#     id_num_venda serial primary key,
#     data_venda varchar(10),
#     cpf_cnpj varchar(11),
#     nome varchar(100),
#     cpf_vendedor varchar(11),
#     itens_id int references itens(id)
#     valor_entrada float,
#     quantidade_parcelas int
# );
# create table contas_receber(
#     id serial primary key,
#     id_venda int references venda(id_num_venda),
#     data_vencimento varchar(10),
#     valor float,
# );

#conecta ao banco de dados
try:
    con = mysql.connector.connect(user = 'root', password = '', host = 'localhost', database = 'db_receber')
    cursor = con.cursor()
except Exception as e:
    print('Erro ao conectar no banco de dados')

#converte para Json
def gera_response(status, nome_conteudo, conteudo, mensagem=False):
    body = {}
    body[nome_conteudo] = conteudo
    if mensagem:
        body["mensagem"] = mensagem
    return Response(json.dumps(body), status=status, mimetype="application/json")

#Selecionar tudo
@app.route("/receber", methods=["GET"])
def seleciona_vendas():
    cursor.execute("SELECT * FROM venda")
    vendas = cursor.fetchall()
    vendas_json = json.dumps(vendas)
    return gera_response(200, "vendas", vendas_json)

#Selecionar Individual
@app.route("/receber/<id>", methods=["GET"])
def seleciona_venda(id):
    cursor.execute("SELECT * FROM venda WHERE id_num_venda = %s", (id,))
    vendas = cursor.fetchall()
    vendas_json = json.dumps(vendas)
    return gera_response(200, "vendas", vendas_json)

#deletar
@app.route("/receber/<id>", methods=["DELETE"])
def deleta_venda(id):
    cursor.execute("DELETE FROM venda WHERE id_num_venda = %s", (id,))
    con.commit()
    return gera_response(200, "vendas", "Deletado com sucesso", True)

#inserir
@app.route("/receber", methods=["POST"])
def insere_venda():
    dados = request.get_json()
    cursor.execute("INSERT INTO venda (data_venda, cpf_cnpj, nome, cpf_vendedor, itens_id, valor_entrada, quantidade_parcelas) VALUES (%s, %s, %s, %s, %s, %s, %s)", (dados["data_venda"], dados["cpf_cnpj"], dados["nome"], dados["cpf_vendedor"], dados["itens_id"], dados["valor_entrada"], dados["quantidade_parcelas"]))
    con.commit()
    return gera_response(201, "vendas", "Inserido com sucesso", True)

#selecionar contas a receber
@app.route("/contas_receber/<id>", methods=["GET"])
def seleciona_contas_receber(id):
    cursor.execute("SELECT * FROM contas_receber WHERE id_venda = %s", (id,))
    contas_receber = cursor.fetchall()
    contas_receber_json = json.dumps(contas_receber)
    return gera_response(200, "contas_receber", contas_receber_json)



app.run(debug=True)
