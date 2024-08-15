from flask import Flask, render_template, jsonify # Importe o modulo jsonify
from cotacoes import get_currency_rates # importação da função para consultar as cotações# Importando o Blueprint
# Registrando o Blueprint

app = Flask(__name__)


# Rota para renderizar a página de cotações
@app.route('/cotacoes')
def cotacoes():
    return render_template('cotacoes.html')

# Rota para fornecer as cotações em formato JSON
@app.route('/rates')
def rates():
    return jsonify(get_currency_rates())

if __name__ == "__main__":
    app.run(debug=True)