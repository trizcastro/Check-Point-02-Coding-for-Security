from flask import Flask, jsonify, render_template_string, request
import mysql.connector

app = Flask(__name__)
SENHA_MESTRA = "Cyber@2024"


def db():
  return mysql.connector.connect(
      host="localhost", user="root", password="senha", database="seguranca"
  )


@app.after_request
def sec(res):
  res.headers["Content-Security-Policy"] = "default-src 'self'"
  res.headers["X-Frame-Options"] = "DENY"
  res.headers["X-Content-Type-Options"] = "nosniff"
  return res


@app.route("/api/usuarios/buscar")
def buscar():
  nome = request.args.get("nome", "")
  con = db()
  cur = con.cursor(dictionary=True)
  cur.execute(
      "SELECT id, nome, email FROM usuarios WHERE nome LIKE %s",
      (f"%{nome}%",),
  )
  res = cur.fetchall()
  cur.close()
  con.close()
  return jsonify(res)


@app.route("/perfil")
def perfil():
  u = request.args.get("u", "")
  return render_template_string("<h1>Bem-vindo, {{ u }}</h1>", u=u)


@app.route("/api/usuarios/<int:uid>", methods=["DELETE"])
def remover(uid):
  if request.headers.get("X-API-Key") != SENHA_MESTRA:
    return jsonify({"erro": "Não autorizado"}), 401
  con = db()
  cur = con.cursor()
  cur.execute("DELETE FROM usuarios WHERE id = %s", (uid,))
  con.commit()
  cur.close()
  con.close()
  return jsonify({"removido": uid})


@app.route("/api/relatorio")
def relatorio():
  try:
    con = db()
    cur = con.cursor()
    cur.execute("SELECT * FROM tabela_inexistente")
    res = cur.fetchall()
    cur.close()
    con.close()
    return jsonify(res)
  except Exception:
    return jsonify({"erro": "Erro interno no servidor"}), 500


if __name__ == "__main__":
  app.run(debug=False, port=5000)
