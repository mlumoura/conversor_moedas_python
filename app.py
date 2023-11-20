import requests
# Importando um objeto da biblioteca BeutifulSoap
from bs4 import BeautifulSoup
from flask import Flask, request, render_template  # Importa as bibliotecas

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

app = Flask(__name__)  # Inicializa a aplicação


@app.route('/')  # Nova rota
def main():
    resultado = None
    mensagem = None
    cotacao = 0
    valor_convertido = 0

    real = request.args.get('real')
    moeda = request.args.get('moeda')

    if real and moeda:
        real = float(real)
        moeda = moeda.lower()

        if moeda == 'dolar':
            # Acessando o website
            page = requests.get(
                "https://www.google.com/search?q=dolar&oq=dolar&gs_lcrp=EgZjaHJvbWUyCQgAEEUYORiABDIHCAEQABiABDIHCAIQABiABDIHCAMQABiABDIHCAQQABiABDIHCAUQABiABDIHCAYQABiABDIHCAcQABiABDIHCAgQABiABDIHCAkQABiABNIBCTIyNzdqMGoxNagCALACAA&sourceid=chrome&ie=UTF-8",
                headers=headers)
            soup = BeautifulSoup(page.content, 'html.parser')

            print(moeda)
            
        elif moeda == 'euro':
            page = requests.get(
                "https://www.google.com/search?q=euro&sca_esv=575718203&sxsrf=AM9HkKnWg3K76hgvQSf8zj5eitfIL69XJw%3A1698046617170&ei=mSI2ZeCDCs685OUPhqCmoAo&ved=0ahUKEwigtLbL1IuCAxVOHrkGHQaQCaQQ4dUDCBA&uact=5&oq=euro&gs_lp=Egxnd3Mtd2l6LXNlcnAiBGV1cm8yCBAAGIoFGJECMggQABiKBRiRAjIHEC4YigUYQzIHEAAYigUYQzIHEAAYigUYQzIHEC4YigUYQzIFEAAYgAQyBRAAGIAEMgUQLhiABDIFEAAYgARIrBRQAFj4A3AAeAGQAQCYAd0BoAHXBaoBBTAuMy4xuAEDyAEA-AEBwgIEECMYJ8ICBxAjGIoFGCfCAg4QLhiKBRjHARjRAxiRAsICCxAuGIAEGMcBGNEDwgIIEC4YigUYkQLiAwQYACBBiAYB&sclient=gws-wiz-serp",
                headers=headers)
            soup = BeautifulSoup(page.content, 'html.parser')

        elif moeda == 'peso argentino':
            page = requests.get(
                "https://www.google.com/search?q=moedaargentina&sca_esv=575718203&sxsrf=AM9HkKl-qbbCSpz0kT2UALGk1lj033xz_A%3A1698046865456&ei=kSM2Zey-G-j35OUPuuEC&ved=0ahUKEwisy-jB1YuCAxXoO7kGHbqwAAAQ4dUDCBA&uact=5&oq=moedaargentina&gs_lp=Egxnd3Mtd2l6LXNlcnAiDm1vZWRhYXJnZW50aW5hMgcQABgNGIAEMgcQABgNGIAEMgcQABgNGIAEMgcQABgNGIAEMgcQABgNGIAEMgcQABgNGIAEMgcQABgNGIAEMgcQABgNGIAEMgYQABgeGA0yBhAAGB4YDUj7HlDdEFjNGnABeAGQAQCYAdwBoAH9CaoBBTAuOC4xuAEDyAEA-AEBwgIKEAAYRxjWBBiwA8ICChAAGIoFGLADGEPCAgcQIxixAhgnwgIKEAAYywEYgAQYCuIDBBgAIEGIBgGQBgk&sclient=gws-wiz-serp",
                headers=headers)
            soup = BeautifulSoup(page.content, 'html.parser')

        elif moeda == 'yuan':
            page = requests.get(
                "https://www.google.com/search?q=moeda+da+china&sca_esv=575718203&sxsrf=AM9HkKnbfmTba0HMFi5j-rDxkgBiBo57rg%3A1698046758104&ei=JiM2ZcT9BcHE5OUP24uYoAY&ved=0ahUKEwjEqNCO1YuCAxVBIrkGHdsFBmQQ4dUDCBA&uact=5&oq=moeda+da+china&gs_lp=Egxnd3Mtd2l6LXNlcnAiDm1vZWRhIGRhIGNoaW5hMg0QABjLARiABBhGGIICMggQABjLARiABDIIEAAYywEYgAQyCBAAGMsBGIAEMggQABjLARiABDIIEAAYywEYgAQyCBAAGMsBGIAEMggQABjLARiABDIIEAAYywEYgAQyCBAAGMsBGIAESNqIAVD_bljiggFwAngBkAEAmAHjAaABnxCqAQYwLjEyLjK4AQPIAQD4AQHCAgoQABhHGNYEGLADwgIKEAAYigUYsAMYQ8ICBBAjGCfCAg0QLhjHARjRAxiKBRgnwgIHEAAYigUYQ8ICBRAAGIAEwgIFEC4YgATCAgcQLhiKBRhDwgIWEC4YigUYQxiXBRjcBBjeBBjfBNgBAcICChAAGIAEGBQYhwLiAwQYACBBiAYBkAYKugYGCAEQARgU&sclient=gws-wiz-serp",
                headers=headers)
            soup = BeautifulSoup(page.content, 'html.parser')
        else:
            cotacao = None

        if cotacao != None:
            valor = soup.find_all("span", class_="DFlfde SwHCTb")[0]
            print(valor)
            cotacao = valor.text
            print(cotacao)
            cotacao = cotacao.replace(',', '.')
            cotacao = float(cotacao)
            valor_convertido = round((real * cotacao), 3)
            resultado = f"""O valor R${real}0 convertido é: {valor_convertido} {moeda} (Cotação ={cotacao})"""
        else:
            resultado = "Esta moeda é inválida ou não está disponível para conversão"

    return render_template('index.html', resultado=resultado)


if __name__ == '__main__':
    app.run(debug=True)  # Executa a aplicação
