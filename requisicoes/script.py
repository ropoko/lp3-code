import requests

url = 'https://dadosabertos.camara.leg.br/api/v2/deputados'

def get_list_deputados() -> list:
  deps = []

  res = requests.get(url=url).json()
  
  for dep in res['dados']:
    deps.append({ 'id': dep['id'], 'nome': dep['nome'] })

  return deps


def get_despesa_deputado(id: int) -> int:
  url_despesa = f'{url}/{id}/despesas'

  res = requests.get(url=url_despesa).json()

  valor_liquido_total = 0

  for v in res['dados']:
    valor_liquido_total += v['valorLiquido']

  return valor_liquido_total

lista_deputados = get_list_deputados()

for dep in lista_deputados:
  gasto_total = get_despesa_deputado(dep['id'])

  print(f'Deputado: {dep["nome"]}, Gastou ao total {gasto_total}')

