
---

# Sistema de Gerenciamento de Campeonato

Este é um sistema simples de gerenciamento de campeonato, desenvolvido com **FastAPI**. Ele permite o gerenciamento de **times**, **jogadores** e **partidas**.

## Funcionalidades

1. **Times**: Cadastro e listagem de times participantes.
2. **Jogadores**: Cadastro e listagem de jogadores, vinculados aos times.
3. **Partidas**: Cadastro de partidas entre os times, incluindo informações como data e resultado.

## Estrutura do Projeto

```
/campeonato
    ├──main.py         # Arquivo principal com a aplicação FastAPI
    ├── /venv              # Ambiente virtual
    ├── requirements.txt   # Arquivo de dependências do projeto
    └── README.md          # Este arquivo
```

## Requisitos

- **Python 3.8+**
- **FastAPI** para criação da API
- **Uvicorn** para servir a aplicação

## Instalação

### 1. Criando o Ambiente Virtual

Para criar um ambiente virtual, execute os seguintes comandos:

```bash
# Crie o ambiente virtual
python3 -m venv venv

# Ative o ambiente virtual
# No Linux/MacOS:
source venv/bin/activate

# No Windows:
venv\Scripts\activate
```

### 2. Instalando Dependências

Com o ambiente virtual ativado, instale as dependências necessárias com o seguinte comando:

```bash
pip install fastapi uvicorn
```

Ou, se você já tiver um arquivo `requirements.txt` com as dependências listadas:

```bash
pip install -r requirements.txt
```

### 3. Rodando o Servidor

Com o ambiente configurado e as dependências instaladas, execute o servidor com o **Uvicorn**:

```bash
uvicorn app.main:app --reload
```

A aplicação será iniciada em `http://127.0.0.1:8000`.

## Endpoints da API

### 1. **Times**

- **GET /times**: Lista todos os times.
- **POST /times**: Cria um novo time.
- **GET /times/{id}**: Exibe os detalhes de um time específico.

### 2. **Jogadores**

- **GET /jogadores**: Lista todos os jogadores.
- **POST /jogadores**: Adiciona um jogador a um time.
- **GET /jogadores/{id}**: Exibe os detalhes de um jogador específico.

### 3. **Partidas**

- **GET /partidas**: Lista todas as partidas.
- **POST /partidas**: Cria uma nova partida entre dois times.
- **GET /partidas/{id}**: Exibe os detalhes de uma partida específica.

## Exemplo de Requisição

### Criando um Time

**POST /times**

```json
{
  "nome": "Time A"
}
```

### Criando um Jogador

**POST /jogadores**

```json
{
  "nome": "Jogador 1",
  "time_id": 1
}
```

### Criando uma Partida

**POST /partidas**

```json
{
  "time1_id": 1,
  "time2_id": 2,
  "data": "2024-12-10T15:00:00",
  "resultado": "2-1"
}
```

## Contribuição

Se você deseja contribuir com o projeto, siga os passos abaixo:

1. Faça um fork deste repositório.
2. Crie uma nova branch (`git checkout -b minha-feature`).
3. Realize suas alterações.
4. Commit as alterações (`git commit -am 'Adiciona nova funcionalidade'`).
5. Faça push para a branch (`git push origin minha-feature`).
6. Abra um pull request.

## Licença

Este projeto está sob a licença **MIT**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

