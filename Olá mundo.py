from flask import Flask # Importa a biblioteca
app = Flask(__name__) # Inicializa a aplicação

@app.route("/") # Cria uma rota
def hello():
    return "Olá, mundo!"

if __name__ == "__main__":
    app.run()  # Executa a aplicação