from flask import Flask, render_template

app = Flask(__name__)

# Criar pagina do site
# Route -> camino depois do nome do dominio
# Função ->o que voce quer exibir na pagina
#template

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)

#colocar site no ar
if __name__ == "__main__":
    app.run(debug=True)

    # Servidor do heroku
    
