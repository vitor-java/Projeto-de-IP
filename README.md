<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=130&color=2D6CDF&version=3&cache=99" />
</p>

<h1 align="center" style="margin-top: 10px; margin-bottom: 20px;">🥪 Missão pelo Sanduíche</h1>

<h2 align="center" style="margin-top: 10px; margin-bottom: 20px;">Projeto de Introdução à Programação</h2>

<h4 align="center" style="margin-top: 10px; margin-bottom: 20px;">
Relatório de desenvolvimento do jogo Missão pelo Sanduíche, desenvolvido para a disciplina de Introdução à Programação pelos alunos do Centro de Informática (CIn) - UFPE período letivo 2026.1 Equipe 02.</h4>


## Índice
* [1. Como Instalar e Rodar o Jogo](#como-instalar)
* [2. Itens e Coletáveis do Jogo](#itens-recursos)
* [3. Personagens Presentes no Jogo](#personagens)
* [4. Sobre o Jogo](#sobre-o-jogo)
* [5. Estrutura / Arquitetura do Projeto](#estrutura-projeto)
* [6. Tecnologias](#tecnologias-utilizadas)
* [7. Equipe](#equipe-desenvolvimento)

---

<a id="como-instalar"></a>
## Instalar e Rodar o Jogo

### Importe o projeto e execute os seguintes comandos no terminal, dentro da pasta do projeto:

#### 1º&nbsp;:&nbsp;&nbsp;Verifique se já existe uma pasta de virtual environment. Ela pode aparecer como ".venv", "venv", ou semelhantes. Caso não haja, crie uma virtual environment chamada 'venv':

```shell
python3 -m venv venv
```

#### 2º&nbsp;:&nbsp;&nbsp;Entre no ambiente virtual criado ou já existente para ser usado pelo projeto: Substitua "&lt;nome&gt;" pelo nome do virtual environment.

#### Comando caso esteja usando Sistemas Linux:
```shell
source <nome>/bin/activate
```

#### Comando caso esteja usando sistema Windows:
```shell
.\<nome>\Scripts\Activate.ps1
```

#### 3º&nbsp;:&nbsp;&nbsp;Instale o pygame com o comando:

```shell
pip install pygame
```

#### 4º&nbsp;:&nbsp;&nbsp;Inicie o jogo executando esse comando no terminal da raiz principal do projeto:

```shell
python3 -m main
```

---

<a id="itens-recursos"></a>
## Itens e Coletáveis do Jogo

| Item / Coletável | Sprite | Descrição e Utilidade |
| :---: | :---: | :--- |
| Bola Quadrada | <img src="data/coletaveis/bola.jpeg" width="40px"> | Item perdido pelo Quico. Chaves precisa recuperá-la dentro da Casa da Bruxa do 71, desviando do Gato Satanás, para dar início à negociação pelo sanduíche. |
| Marreta Biônica | <img src="data/coletaveis/marreta.jpeg" width="40px"> | Pertence ao Chapolin Colorado e está caída perto do Tanque de Lavar Roupas. Ao ser usada, invoca o Chapolin em um desfecho épico. |
| Sanduíche de Presunto | <img src="data/coletaveis/sanduiche.jpeg" width="40px"> | O objetivo final da missão. Cai da janela da Dona Florinda após o Chapolin bater na parede. Coletar este item encerra o jogo com a tela de vitória. |

---

<a id="personagens"></a>
## Personagens Presentes no Jogo

| Personagem | Sprite | Descrição |
| :---: | :---: | :--- |
| Chaves | <img src="data/chaves/chaves_parado.png" width="45px"> | Personagem principal e jogável. Está com fome e precisa encontrar um sanduíche de presunto a todo custo. |
| Quico | <img src="data/quico/4.png" width="45px"> | NPC que inicia a missão prometendo um sanduíche em troca da Bola Quadrada.
| Seu Madruga | <img src="data/madruga/1.png" width="45px"> | NPC que fornece a pista crucial: revela que a Bola Quadrada caiu na janela da Bruxa do 71. |
| Gato Satanás | | Inimigo que patrulha o interior da Casa da Bruxa. Encostar nele reseta o Chaves para o início da sala. |
| Chapolin Colorado | <img src="data/chapolim/3.png" width="45px"> | Invocado pela Marreta Biônica no ato final. Tenta ajudar, bate na parede sem querer e derruba o sanduíche da janela da Dona Florinda. |

---

<a id="sobre-o-jogo"></a>
## Sobre o Jogo

**Missão pelo Sanduíche** é um RPG 2D top-down feito em Python com Pygame, inspirado no universo do seriado Chaves.

### História

O Chaves acorda com fome no Pátio do Barril e topa qualquer coisa por um sanduíche de presunto. O Quico faz uma proposta: ele consegue o sanduíche se o Chaves achar a Bola Quadrada. A busca leva o Chaves pelo Pátio da Fonte, para dentro da assustadora Casa da Bruxa do 71 e de volta ao ponto de partida, num desfecho épico que só o Chapolin Colorado poderia protagonizar.

### Mecânicas de Jogo

- Movimentação por blocos via teclas W, A, S, D.
- Colisão com paredes, móveis e limites de mapa.
- Coleta de itens.
- Diálogos com NPCs acionados por proximidade.
- Gato Satanás com patrulha autônoma.

### Controles

| Tecla | Ação |
| :---: | :--- |
| ↑ | Mover para cima |
| ← | Mover para esquerda |
| ↓ | Mover para baixo |
| → | Mover para direita |

---

<a id="estrutura-projeto"></a>
## Estrutura / Arquitetura do Projeto

```text
Projeto-de-IP
├── classes
│   ├── jogo.py
│   ├── mapa.py
│   ├── personagem.py
│   └── utils.py
├── data
│   ├── cenarios
│   │   ├── cenario0.png
│   │   ├── cenario1.png
│   │   └── cenario2.png
│   ├── chapolim
│   │   └── 3.png
│   ├── chaves
│   │   ├── chaves_baixo_1.png
│   │   ├── chaves_baixo_2.png
│   │   ├── chaves_baixo_3.png
│   │   ├── chaves_baixo_4.png
│   │   └── chaves_parado.png
│   ├── coletaveis
│   │   ├── bola.jpeg
│   │   ├── marreta.jpeg
│   │   └── sanduiche.jpeg
│   ├── madruga
│   │   └── 1.png
│   └── quico
│       └── 4.png
├── .gitignore
├── .mailmap
├── main.py
└── README.md
```

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=130&color=2D6CDF&section=footer&v=99" alt="Footer Animado" />
</p>

---

<a id="tecnologias-utilizadas"></a>
<h1 align="center">Ferramentas/Tecnologias</h1>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=venom&height=40&fontSize=35&color=0:3776AB,100:1B263B&v=99" alt="Header .py" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=for-the-badge" alt="Python Badge" />&nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://img.shields.io/badge/Git-F03C2E?logo=git&logoColor=fff&style=for-the-badge" alt="Git Badge" />&nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=fff&style=for-the-badge" alt="GitHub Badge" />&nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://img.shields.io/badge/Pygame-3776AB?style=for-the-badge&logo=fort-awesome&logoColor=white" alt="Pygame" />&nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://img.shields.io/badge/PyCharm-000?logo=pycharm&logoColor=fff&style=for-the-badge" alt="PyCharm Badge">&nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://img.shields.io/badge/Google%20Gemini-8E75B2?logo=googlegemini&logoColor=fff&style=for-the-badge" alt="Google Gemini Badge">&nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://img.shields.io/badge/Markdown-000?logo=markdown&logoColor=fff&style=for-the-badge" alt="Markdown Badge">
  
</p>

---

<a id="equipe-desenvolvimento"></a>
<h2 align="center">👥 Equipe</h2>

<div align="center">
  <table>
    <tr>
      <td valign="middle" align="center">
        <a href="https://github.com/vitor-java">
          <img src="https://images.weserv.nl/?url=github.com/vitor-java.png&w=35&h=35&mask=circle" alt="Vitor"><br>Vitor
        </a>
      </td>
      <td valign="middle" align="center">
        <a href="https://github.com/eugeni1">
          <img src="https://images.weserv.nl/?url=github.com/eugeni1.png&w=35&h=35&mask=circle&v=10" alt="Eugênio"><br>Eugênio
        </a>
      </td>
      <td valign="middle" align="center">
        <a href="https://github.com/Arthur-Carvalh01">
          <img src="https://images.weserv.nl/?url=github.com/Arthur-Carvalh01.png&w=35&h=35&mask=circle" alt="José"><br>José
        </a>
      </td>
      <td valign="middle" align="center">
        <a href="https://github.com/Guilhermerlemos">
          <img src="https://images.weserv.nl/?url=github.com/Guilhermerlemos.png&w=35&h=35&mask=circle" alt="Guilherme"><br>Guilherme
        </a>
      </td>
      <td valign="middle" align="center">
        <a href="https://github.com/Rafael040305">
          <img src="https://images.weserv.nl/?url=github.com/Rafael040305.png&w=35&h=35&mask=circle" alt="Cagnin"><br>Cagnin
        </a>
      </td>
      <td valign="middle" align="center">
        <a href="https://github.com/PedroReis0310">
          <img src="https://images.weserv.nl/?url=github.com/PedroReis0310.png&w=35&h=35&mask=circle" alt="Pedro"><br>Pedro
        </a>
      </td>
    </tr>
  </table>
</div>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=130&color=2D6CDF&section=footer&v=99" alt="Footer Animado" />
</p>
