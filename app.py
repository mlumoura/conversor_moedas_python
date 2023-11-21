import requests
# Importando um objeto da biblioteca BeutifulSoap
from bs4 import BeautifulSoup
from flask import Flask, request, render_template  # Importa as bibliotecas

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}

app = Flask(__name__)  # Inicializa a aplicação


@app.route('/')  # Nova rota
def main():
    resultado = None
    mensagem = None
    cotacao = 0
    valor_convertido = 0

    def cotacao(moeda):
        # Lista das moedas disponíveis para apurar cotação
        # moedas_sigla = [('dolar', 'USD'), ('euro', 'EUR'), ('peso argentino', 'ARS'), ('peso chileno', 'CLP'),
        #                 ('pound sterling', 'GBP'),('yuan', 'CNY'), ('iene', 'JPY')]

        moedas = ['dolar', 'euro', 'libra esterlina', 'peso argentino', 'peso chileno', 'pound sterling', 'yuan',
                  'iene']

        if moeda in moedas:
            if moeda == 'dolar': sigla = 'USD'
            if moeda == 'euro': sigla = 'EUR'
            if moeda == 'peso argentino': sigla = 'ARS'
            if moeda == 'peso chileno': sigla = 'CLP'
            if moeda == 'pound sterling': sigla = 'GBP'
            if moeda == 'libra esterlina': sigla = 'GBP'
            if moeda == 'yuan': sigla = 'CNY'
            if moeda == 'iene': sigla = 'JPY'

            page = requests.get(
                f"""https://www.google.com/finance/quote/{sigla}-BRL""", headers=headers)

            soup = BeautifulSoup(page.content, 'html.parser')

            # valor = soup.find_all("span", class_="DFlfde SwHCTb")[0]
            valor = soup.find_all("div", class_="YMlKec fxKbKc")[0]

            cotacao = valor.text
            cotacao = cotacao.replace(',', '.')
            cotacao = float(cotacao)
            valor_convertido = round((real / cotacao), 3)
            resultado = f"""O valor R${real} convertido, equivale a {valor_convertido} {moeda} (Cotação = {cotacao})"""

            return resultado
        else:
            resultado = "Esta moeda é inválida ou não está disponível para conversão"
            return resultado

    real = request.args.get('real')
    moeda = request.args.get('moeda')

    if real and moeda:
        real = float(real)
        moeda = moeda.lower()

        resultado = cotacao(moeda)

    return render_template('index.html', resultado=resultado)


if __name__ == '__main__':
    app.run(debug=True)  # Executa a aplicação

# gunicorn -w 3 app:app
