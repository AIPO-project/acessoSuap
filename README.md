# [Script simples para acesso ao SUAP](https://suap.ifrn.edu.br/api/docs/#/)

Este é um script simples para testar a API do SUAP utilizando python e requests. Esse script consegue um token jwt do SUAP e utiliza esse token para fazer um acesso aos dados de um servidor.

Os endpoints utilizados:

- /api/token/pair
- /api/rh/meus-dados/

O script em questão solicita a matrícula e senha do SUAP e utiliza esses dados para conseguir da API um token JWT, esse token é utilizado para requisitar informações do servidor que colocou a senha e a matrícula.

Para requisitar informações de um aluno é necessário utilizar o endpoint a baixo:

- /api/ensino/meus-dados-aluno/


A documentação da API do SUAP pode ser acessada através do link:
[https://suap.ifrn.edu.br/api/docs/#/](https://suap.ifrn.edu.br/api/docs/#/)
