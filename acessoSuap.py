import requests
from getpass import getpass

api_url = "https://suap.ifrn.edu.br/api/"

user = input("user: ")
password = getpass()

data = {"username": user, "password": password}

response = requests.post(api_url + "v2/autenticacao/token/", json=data)

if response.status_code == 200:
    token = response.json().get("access")
    print(response.json())

    headers = {
        "Authorization": f'Bearer {token}'
    }

    response_meus_dados = requests.get(api_url + "v2/minhas-informacoes/meus-dados/", headers=headers)

    if response_meus_dados.status_code == 200:
        print("Informações do Aluno:")
        print(response_meus_dados.json())
        print("")
        print(response_meus_dados.json()["matricula"])
        print(response_meus_dados.json()["tipo_vinculo"])
        vinculo = response_meus_dados.json()["vinculo"]
        #print(vinculo["categoria"])
        print(vinculo["campus"])
    else:
        print(f"Erro ao obter informações. Código de status: {response_meus_dados.status_code}")
else:
    print("Erro na autenticação. Verifique seu usuário e senha.")
