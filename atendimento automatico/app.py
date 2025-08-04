from flask import Flask, render_template, request

app = Flask(__name__)

def responder(mensagem):
    mensagem = mensagem.lower()
    if "ola" in mensagem or "oi" in mensagem:
        return "Olá! Como posso ajudar?"
    elif "preço" in mensagem:
        return "Depende, de qual produto você precisa?"
    elif "obrigado" in mensagem:
        return "De nada, precisando é só chamar!"
    else:
        return "Não entendi, pode repetir por favor?"

@app.route("/", methods=["GET", "POST"])
def index():
    resposta = ""
    if request.method == "POST":
        mensagem = request.form["mensagem"]
        resposta = responder(mensagem)
    return render_template("index.html", resposta=resposta)

if __name__ == '__main__':
    app.run(debug=True)

