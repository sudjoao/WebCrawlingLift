from bs4 import BeautifulSoup
import requests
params = (
    ('secao', 'TRF1'),
)

data = {
  'nome': 'jo\xE3o silva',
  'secao': 'TRF1',
  'pg': '2',
  'enviar': 'Pesquisar',
  'g-recaptcha-response': '',
  'nomeParte': '03AGdBq27fMWgSAR8gK0EQ7E21xXNo4qh6uS1UIRS4-C-wcqJx-FMkqZO1-pcuBmbj8ygCzCyrrAHWkFVPvOrt-5MoMaBr7jik3eHgAWL739jujsN01OIIzi_gdtRdJDIH2QhwZbgdAwKItBY_X5jUQJScV97yKPdMvAAhBMrV0a87EUvAIv2he0RX_ZkMXh7y097WojJUdhAxcsR2LsIT5Ddhzij3U3P9DZs8VSjb3oOFMtuGO69ObQosHZBjjbd64bAk0cD9_bFgh7C4VQ7u6FejrVJedSpJ9rAyatgQCcu4Dez5F0yGrQeYNMSpP0RPySNKnrBNeRbqGApuy5OWAzgf6IJPCyZFkouP5M38vFTiPT3F6p8CWYOTrAwa2wCRLRpOg_hkKlp3X5Dkb7hWgSYRViPhMS8SLsjA-p7pDJX6DbxdMDBT3HkDescYTEgHol5KqQW0NRZYQBhpV4qAaOlXHWqk7AxfHw',
  'nmToken': 'nomeParte'
}

response = requests.post('https://processual.trf1.jus.br/consultaProcessual/parte/listar.php', params=params,data=data).content

# soup = BeautifulSoup(response, 'html.parser')
# processes = soup.find_all("a", class_="listar-processo")
# for single_process in processes:
#     href = single_process.get('href')
#     response = requests.get(f'https://processual.trf1.jus.br{href}').content
#     soup = BeautifulSoup(response, 'html.parser')
#     print(soup.prettify())

params = (
    ('proc', '2572005220094019198'),
    ('secao', 'TRF1'),
    ('nome', 'JOAO SILVA'),
    ('mostrarBaixados', 'N'),
)

response = requests.get('https://processual.trf1.jus.br/consultaProcessual/processo.php', params=params).content
soup = BeautifulSoup(response, 'html.parser')
print(soup.prettify())
