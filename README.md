## Minha Equipe de Pesquisa e Produção de Artigos com IA

powered by [crewAI](https://crewai.com) project.

Sem dúvidas, o framework mais simples e intuitivo para utilizar modelos de linguagem e formar equipes que possam colaborar de forma eficiente na execução de tarefas mais complexas do que simplesmente interagir com o GPT.

### Funcionalidades
#### Agentes e Ferramentas:
Utiliza agentes automatizados para realizar tarefas específicas.

#### Tarefas Automatizadas:
- Pesquisa de tendências.
- Validação de dados coletados.
- Revisão de conteúdo.
- Produção de artigos e posts baseados em dados.


##  Estrutura do Projeto
```
pdf_summarizer/
├── articles/
│   └── output.md
├── config/
│   └── agents.json
│   └── tasks.json 
├── agents.py
├── main.py
├── tasks.py
├── requirements.txt
└── README.md
```

## Requisitos
- Python 3.10 or higher
- [Poetry](https://python-poetry.org/) for dependency management
- An [OpenAI](https://platform.openai.com) API key
- A [Serper](https://serper.dev/) API key
- A [Browserless](https://www.browserless.io/) API key

## Uso e Testes

1. Clone o Repositório:
```sh
git clone https://github.com/NonakaVal/research_agents.git
cd .\research_agents\
```
2. Upgrade pip:
```sh
python -m pip install --upgrade pip
```
3. Instalar dependencias com requirements.txt
```sh
pip install -r requirements.txt
```
4. Configurar Chaves de API
```sh
setx SERPER_API_KEY "sua chave"
setx OPENAI_API_KEY "sua chave"
```
ou
```.env
SERPER_API_KEY=your_serper_api_key
OPENAI_API_KEY=your_openai_api_key
BROWSERLESS_API_KEY=your_browserless_api_key
```
### Configurando Agentes

1. Altere os aquivos `agents.json` e `tasks.json` na pasta `config/`.
2. O resultado da sua pesquisa será criada no diretório  `articles/`

    
## CrewAI Support and Documentations 
For support, questions, or feedback regarding the SelfDevelopment Crew or crewAI:
- [documentation](https://docs.crewai.com)
- [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)


<a href="https://www.crewai.com/">
    <img src="https://i.imgur.com/0FllxzQ.png" alt="Image" width="15%" style="display: block; margin: 0 auto;">
</a>


