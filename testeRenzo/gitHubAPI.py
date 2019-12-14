import requests


def buscar_avatar(nome):
    '''
    - acompanhamneto do curso Renzo Python Pro - 
    esta função vai er eliminada logo a frente

    '''
     
    url = f'https://api.github.com/users/{nome}'
    resposta = requests.get(url)
    return resposta.json()['avatar_url']

if __name__ == '__main__':
    print(buscar_avatar('PGabriel-MB'))