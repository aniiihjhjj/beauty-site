from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # Aqui você precisa garantir que a página index.html esteja na pasta "templates"

@app.route("/enviar", methods=["POST"])
def enviar():
    nome = request.form["nome"]
    email = request.form["email"]
    pagamento = request.form["pagamento"]

    # Aqui você pode salvar esses dados se quiser (em arquivo, banco etc.)

    return redirect(url_for("confirmacao"))

@app.route("/confirmacao")
def confirmacao():
    return render_template("confirmacao.html")  # Certifique-se de que confirmacao.html esteja na pasta "templates"

if __name__ == "__main__":
    app.run(debug=True)
