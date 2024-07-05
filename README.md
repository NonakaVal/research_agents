## Equipe de Pesquisa e Produção de Artigos com IA

<a href="https://www.crewai.com/">
    <img src="https://i.imgur.com/0FllxzQ.png" alt="Image" width="18%" style="display: block; margin: 0 auto;">
</a>

Sem dúvidas, o framework mais simples e intuitivo para utilizar modelos de linguagem e formar equipes que possam colaborar de forma eficiente na execução de tarefas mais complexas do que simplesmente interagir com o GPT.

### Como funciona
<a href="https://www.crewai.com/">
    <img src="https://i.imgur.com/PV4JKSN.png" alt="Image" width="50%" style="display: block; margin: 0 auto;">
</a>

[Video Aula](https://www.youtube.com/watch?v=sPzc6hMg7So&t=1055s&ab_channel=codewithbrandon) 

### Funcionalidades
#### Agentes e Ferramentas:
Utiliza agentes automatizados para realizar tarefas específicas.

#### Tarefas Automatizadas:
- Pesquisa de tendências.
- Validação de dados coletados.
- Revisão de conteúdo.
- Produção de artigos e posts baseados em dados.
- Estrutura do Projeto

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
python -m venv env 
```
```
env\Scripts\activate
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

