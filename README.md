# Como rodar o projeto localmente

## Pré-requisitos

Antes de rodar o projeto, certifique-se de ter as seguintes ferramentas instaladas:

- [Python 3.8+](https://www.python.org/downloads/)
- [Pip](https://pip.pypa.io/en/stable/)
- [Git](https://git-scm.com/)

## Clonar o repositório
Clone o repositório para o seu computador:

```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
```
## Configurar variáveis de ambiente
Crie um arquivo .env na raiz do projeto e adicione sua chave da API Gemini

```bash
GEMINI_API_KEY=sua_chave_de_api
```
## Iniciar o servidor
No console da sua IDE digite:
```bash
uvicorn app.main:app --reload
```
O servidor será iniciado em http://localhost:8000

---

## Endpoints
### /gerar-pergunta
```bash
{
  "topico": "AWS"
}
```
### Resposta esperada:
```bash
{
	"resposta": "```json\n[\n  {\n    \"pergunta\": \"Qual serviço da AWS permite que você execute código sem provisionar ou gerenciar servidores?\",
\n    \"alternativas\": [\n      \"Amazon EC2\",\n      \"AWS Lambda\",\n      \"Amazon S3\",\n      \"Amazon RDS\"\n    ],\n
 \"correta\": \"AWS Lambda\",\n\"feedbacks\": {\n      \"Amazon EC2\": \"Errado. Amazon EC2 fornece servidores virtuais na
nuvem, exigindo gerenciamento.\",\n      \"AWS Lambda\":
\"Correto. AWS Lambda permite executar código sem gerenciar servidores.\",\n      \"Amazon S3\": \"Errado. Amazon S3 é um
serviço de armazenamento de objetos.\",\n
 \"Amazon RDS\": \"Errado. Amazon RDS é um serviço de banco de dados relacional.\"\n    }\n  },\n  {\n    \"pergunta\":
\"Qual serviço da AWS é usado para hospedar bancos de dados relacionais?\",\n
 \"alternativas\": [\n      \"Amazon EC2\",\n      \"Amazon S3\",\n      \"Amazon RDS\",\n      \"Amazon CloudFront\"\n
 ],\n    \"correta\": \"Amazon RDS\",\n    \"feedbacks\": {\n
  \"Amazon EC2\": \"Errado. Amazon EC2 fornece servidores virtuais, mas não é especificamente para bancos de dados.\",\n
 \"Amazon S3\": \"Errado. Amazon S3 é um serviço de armazenamento de objetos.\",\n
[...]
}
```

## Exemplo de como formatar o JSON (remover o markdown de código e converter para JSON legível) no frontend
```bash
 getPerguntas(): Observable<any> {
    return this.http.get('URL_DA_API');
  }

  processarResposta(resposta: string): any {
    const jsonLimpo = resposta.replace(/```json\n|\n```/g, '');
    return JSON.parse(respostaLimpa);
  }
```
