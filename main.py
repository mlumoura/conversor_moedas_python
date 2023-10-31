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

    real = request.args.get('real')
    segunda = request.args.get('moeda')

    if real and segunda:
        real = float(real)

        if ((segunda == 'Dolar') or (segunda == 'dolar')):
            # Acessando o website
            page = requests.get(
                "https://www.google.com/search?q=dolar&oq=dolar&gs_lcrp=EgZjaHJvbWUyCQgAEEUYORiABDIHCAEQABiABDIHCAIQABiABDIHCAMQABiABDIHCAQQABiABDIHCAUQABiABDIHCAYQABiABDIHCAcQABiABDIHCAgQABiABDIHCAkQABiABNIBCTIyNzdqMGoxNagCALACAA&sourceid=chrome&ie=UTF-8",
                headers=headers)
            soup = BeautifulSoup(page.content, 'html.parser')
            valor_dolar = soup.find_all("span", class_="DFlfde SwHCTb")[0]
            moeda = valor_dolar.text
            moeda = moeda.replace(',', '.')
            moeda = float(moeda)

            resultado = round((real * moeda), 3)

            # texto = str(real) + "R$ valem " + str(resultado) + "$"

    return render_template('index.html',
                           resultado=resultado, media="$")

if __name__ == '__main__':
    app.run(debug=True)  # Executa a aplicação
