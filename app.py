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
        moedas = ['dolar', 'euro', 'koruna', 'peso argentino', 'peso chileno', 'pound sterling', 'yuan', 'yen']
        if moeda in moedas:
            page = requests.get(
                f"""https://www.google.com/search?q={moeda}&oq={moeda}&sclient=gws-wiz-serp&sourceid=chrome&ie=UTF-8""",
                headers=headers)
            soup = BeautifulSoup(page.content, 'html.parser')

            valor = soup.find_all("span", class_="DFlfde SwHCTb")[0]
            cotacao = valor.text
            cotacao = cotacao.replace(',', '.')
            cotacao = float(cotacao)
            valor_convertido = round((real / cotacao), 3)
            resultado = f"""O valor R${real} convertido é: {valor_convertido} {moeda} (Cotação ={cotacao})"""

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
