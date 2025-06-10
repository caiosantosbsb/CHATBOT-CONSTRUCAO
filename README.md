# Chatbot de Construção

Este projeto é um MVP de um chatbot consultor de construção residencial para casas no Centro-Oeste do Brasil. Utiliza GPT-4 via OpenAI API e um backend simples em Flask.

## Estrutura do Projeto

- `backend/` – aplicação Flask e scripts de banco de dados
- `frontend/` – interface web em HTML, CSS e JavaScript
- `requirements.txt` – dependências Python

## Como executar

1. Instale as dependências Python:

```bash
pip install -r requirements.txt
```

2. Configure a variável de ambiente `OPENAI_API_KEY` com sua chave da OpenAI.

3. Inicialize o banco de dados (opcional):

```bash
python backend/database.py
```

4. Inicie o servidor Flask:

```bash
python backend/app.py
```

5. Abra `frontend/index.html` em seu navegador para utilizar o chatbot.

## Power BI Embedded

A integração com Microsoft Power BI Embedded pode ser adicionada no arquivo `frontend/index.html` onde indicado. Será necessário gerar os tokens e referências a relatórios segundo a documentação oficial da Microsoft.

## Licença

MIT
