from flask import Flask, render_template, request,  session, redirect, url_for
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
logins = {"Eduardo":"123",
          "Sabrina":"12345"}

@app.route("/")

def home():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    session["nome"] = request.form.get("nome-usuario")
    nome = session.get("nome")
    senha = request.form.get("senha-usuario")
    mensagem = "Login inválido"
    for usuario in logins:
        if session.get("nome") == nome and senha == logins[usuario]:
            logado = True
            return redirect(url_for('perfil'))
        else:
            logado = False
            return mensagem
@app.route("/perfil")
def perfil():
    usuario = session.get("nome")
    return render_template("perfil.html", usuario = usuario)

if __name__ == "__main__":
    app.run(debug=True)