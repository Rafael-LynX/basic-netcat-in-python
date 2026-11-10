# Basic Netcat in Python

<img src="assets/netcat-connection.png" alt="" style="display: block; margin: 20px auto; max-width: 80%; height: auto; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.3);">

_Netcat_ é uma ferramenta ótima de linha de comando, a minha versão seria uma mais básica dela em python, ela faz apenas a conexão cliente-servidor para comunicação entre os scripts e permite comandos no outro lado como se fosse uma _reverse shell_.

## Functions

- **Listening mode:** Ele atua como um servidor para aceitar conexões de entrada do script `client`.
- **Client mode:** Faz a conexão no endereço do servidor utilizando a mesma porta.

## Installation

### 1

```sh
git clone https://github.com/Rafael-LynX.git
```

### 2

```python
## ligar o servidor
python3 server.py
## Depois ligar o client
python3 client.py
## Após isso testar os comandos no terminal do server.py
```

## Built with

Ele foi construído em python.

[![Python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

## Details

Para entender detalhadamente como o código funciona, acesse os [Detalhes](/docs/details.md).

## Autor

[<img loading="lazy" src="https://avatars.githubusercontent.com/u/109623407?s=400&u=19dac11507a1cbd81c5c6ceb1526c24eb6033cce&v=4" width=115><br><sub>Rafael Vieira</sub>](https://github.com/Rafael-LynX)
