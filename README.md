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

## Passo a passo caso queira rodar esse meu projeto de estudo.

### Chaves de API
- https://platform.openai.com
- https://serper.dev/
- https://www.browserless.io/

### Windowns

```
git clone https://github.com/NonakaVal/research_agents.git
```
```
cd .\research_agents\
```
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
```
setx SERPER_API_KEY "sua chave"
```
```
setx OPENAI_API_KEY "sua chave"
```
### Alterando Projeto 
Para definir qual pesquisa os quatro agentes farão e de qual forma,  basta alterar os prompts dos arquivos _agent.json_ e _tasks.json_ presentes na pasta _config_
e para saber mais acesse a [documentação](https://docs.crewai.com/).

