#Importa a biblioteca HTMLSession da bibliotece requests_html
from requests_html import HTMLSession

#cria uma sessão HTTP usando a classe HTMLSession
sessao = HTMLSession()

# Define a URL da páigna que será acessada
url = 'https://www.olx.com.br/eletronicos-e-celulares/estado-sp?q=iphone'

# Faz um requisição GET à página da web usando a sessão criada
resposta = sessao.get(url)

# Cria uma lista vazia que irá armazenar as informações dos anúnicos
anuncios = []

# Usa o método find do obeto html retornado na resposta encontrar todos os links dos anúncios
links = resposta.html.find('#ad-list li a')

#Itera sobre todos os links encontrados na página
for link in links:
    #estrai o URL de cada anúnio do atributo 'href' do elemento
    url_iphone = link.attrs['href']

    # Faz um requisição GET ao URL de cada anúnico usando a sessão criada
    resposta_iphone = sessao.get(url_iphone)

    # Extrai o título e o preço de cada anúncio
    titulo = resposta_iphone.html.find('h1', first = True).text
    preco = resposta_iphone.html.find('h2', first = True).text

    #Adiciona as informações do anúncio na lista de anúncios
    anuncios.append({
        'url': url_iphone,
        'titulo': titulo,
        'preco': preco
    })

    print(anuncios)

