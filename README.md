# Projeto-de-IP

1. Importe o projeto e rode os seguintes comandos no console/terminal, na pasta do projeto :

2. Verifique se já existe uma pasta de virtual environment. Ela pode aparecer como ".venv", "venv", ou semelhantes.
Caso não haja, crie um virtual environment chamado 'venv':

```shell
python3 -m venv venv
```

3. Sete o virtual criado ou já existente para ser usado pelo projeto:
Substitua "&lt;nome&gt;" pelo nome do virtual environment. 
Caso tenha sido criado na etapa anterior, substitua por "venv".

Comando caso esteja usando Ubuntu:
```shell
source <nome>/bin/activate
```

Comando, caso esteja usando Windows:
```shell
.\venv\Scripts\Activate.ps1
```

4. Instale o pygame:

```shell
pip install pygame
```

5. Teste se o pygame tá rodando:

```shell
python3 -m pygame.examples.aliens
```
