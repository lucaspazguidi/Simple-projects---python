from flask import Flask, render_template, jsonify
app = Flask(__name__)
# Rota 1: Serve a "casca" da aplicação (o HTML vazio)
@app.route('/')
def pagina_app():
# Envia o "kit de montar" para o navegador
    return render_template('index.html')
# Rota 2: API que fornece os dados em formato JSON (os "ingredientes")
@app.route('/api/alunos')
def api_alunos():
    imagens = [
        {"nome":"static/assets/agostinho.png"},
        {"nome":"static/assets/agostinho2.jpeg"},
        {"nome":"static/assets/agostinho3.jpeg"},
        {"nome":"static/assets/agostinho-memphis.jpg"}
        
    ]
# Retorna os dados em formato JSON, que o JavaScript entende.
    return jsonify(imagens)
if __name__ == '__main__':
    app.run(debug=True, port=5001)