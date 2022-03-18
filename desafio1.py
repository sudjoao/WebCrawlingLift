from bs4 import BeautifulSoup
import requests


def getAllProcesses(name):
  params = (
      ('secao', 'TRF1'),
  )
  data = {
    'nome': name,
    'secao': 'TRF1',
    'pg': '2',
    'enviar': 'Pesquisar',
    'g-recaptcha-response': '',
    'nomeParte': '03AGdBq27fMWgSAR8gK0EQ7E21xXNo4qh6uS1UIRS4-C-wcqJx-FMkqZO1-pcuBmbj8ygCzCyrrAHWkFVPvOrt-5MoMaBr7jik3eHgAWL739jujsN01OIIzi_gdtRdJDIH2QhwZbgdAwKItBY_X5jUQJScV97yKPdMvAAhBMrV0a87EUvAIv2he0RX_ZkMXh7y097WojJUdhAxcsR2LsIT5Ddhzij3U3P9DZs8VSjb3oOFMtuGO69ObQosHZBjjbd64bAk0cD9_bFgh7C4VQ7u6FejrVJedSpJ9rAyatgQCcu4Dez5F0yGrQeYNMSpP0RPySNKnrBNeRbqGApuy5OWAzgf6IJPCyZFkouP5M38vFTiPT3F6p8CWYOTrAwa2wCRLRpOg_hkKlp3X5Dkb7hWgSYRViPhMS8SLsjA-p7pDJX6DbxdMDBT3HkDescYTEgHol5KqQW0NRZYQBhpV4qAaOlXHWqk7AxfHw',
    'nmToken': 'nomeParte'
  }
  response = requests.post('https://processual.trf1.jus.br/consultaProcessual/parte/listar.php', params=params,data=data).content
  soup = BeautifulSoup(response, 'html.parser')
  processes = soup.find_all("a", class_="listar-processo")
  return processes

def getProcessReference(process):
  href = process.get('href')
  response = requests.get(f'https://processual.trf1.jus.br{href}').content
  soup = BeautifulSoup(response, 'html.parser')
  process_data = soup.find("a")
  process_reference = process_data.get('href')
  return process_reference

def getProcessParams(href):
  splitted_info = href.split('?')
  spplited_params = splitted_info[1].split('&')
  for params in spplited_params:
    param_info = params.split('=')
    if param_info[0] == 'proc':
      procNumber = param_info[1]
    elif param_info[0] == 'nome':
      name = param_info[1]
  process_params = (
    ('proc', procNumber),
    ('secao', 'TRF1'),
    ('nome', name),
    ('mostrarBaixados', 'N'),
  )
  return process_params


process_list = getAllProcesses("João Silva")
for process in process_list:
  process_reference = getProcessReference(process)
  process_params = getProcessParams(process_reference)
  # response = requests.get('https://processual.trf1.jus.br/consultaProcessual/processo.php', params=process_params).content
  # soup = BeautifulSoup(response, 'html.parser')
  # print(soup.prettify())