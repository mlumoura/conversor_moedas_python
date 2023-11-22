import requests
# Importando um objeto da biblioteca BeutifulSoap
from bs4 import BeautifulSoup
from flask import Flask, request, render_template  # Importa as bibliotecas

headers = {
    'User-Agent':
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}

app = Flask(__name__)  # Inicializa a aplicação


@app.route('/')  # Nova rota
def main():
    resultado = None
    cotacao = 0
    valor_convertido = 0

    def cotacao(moeda):
         # Dicionário com as siglas das moedas disponíveis para apurar cotação
        moedas = {'dolar': 'USD', 'euro': 'EUR', 'peso argentino': 'ARS', 'peso chileno': 'CLP', 'pound sterling': 'GBP', 'libra esterlina': 'GBP', 'yuan': 'CNY', 'iene': 'JPY'}

        if moeda in moedas: 
            # Obtenho a respectiva sigla
            sigla = moedas[moeda]

            page = requests.get(
                f"""https://www.google.com/finance/quote/{sigla}-BRL""", headers=headers)

            soup = BeautifulSoup(page.content, 'html.parser')

            # valor = soup.find_all("span", class_="DFlfde SwHCTb")[0]
            valor = soup.find_all("div", class_="YMlKec fxKbKc")[0]

            cotacao = valor.text
            cotacao = cotacao.replace(',', '.')
            cotacao = float(cotacao)
            valor_convertido = round((real / cotacao), 2) if cotacao >= 1 else round(real * (1/cotacao),2)
            resultado = f"""O valor de R$ {real} convertido em {moeda.upper()} equivale a {valor_convertido} {sigla} - Cotação = {cotacao}"""

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
