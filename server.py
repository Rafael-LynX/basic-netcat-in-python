import socket
import sys

### Specify Host and Port
# Vinculando HOST vazio para escutar em todas as interfaces
# PORT define local usado pelo servidor
HOST = ""
PORT = 5789

### Creation socket
# socket é uma interface de software que permite ser utilizada por programas de comunicação
# do sistema operacional através de uma rede.
# AF_INET: refere-se à uma família de endereços IPv4.
# SOCK_STREAM: significa protocolo TCP orientado a conexão.
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


### Binding socket
# bind() vai vincular um endereço IPv4 e uma porta ao socket (soc).
# Isso permite ele escutar todas as interfaces IPv4 na porta escolhida.
# O bind vai associar o socket ao endereço escolhido dentro do parênteses.
# A tupla de dentro com HOST e PORT contém as variáveis de endereço e porta.
# Aceitando somente sockets de IPv4.
# sys permite acessar variáveis e funções que interagem com o interpretador.
def binding_socket():
    try:
        # Associando o socket ao endereço escolhido.
        # Os parênteses dentro de bind é uma tupla, um único argumento que contém o endereço e a porta. Formato espearado.
        soc.bind((HOST, PORT))
    except OSError as e:
        print(f"Bind fail: {e}")
        sys.exit(1)
    print("Socket binding in operation...")


### Listening socket
# listen() permite o socket receber conexões, 5 é o parâmetro chamado backlog.
# se refere a fila de conexões pendentes. A quantidade de conexões simultaneas depende do programa.
# o accept() por padro é bloquante e aguarda conexão.
# conn de connection, é um outro socket específico para conversar com o cliente
# address, é o endereço do cliente IPv4.
def listening_connection():
    try:
        soc.listen(5)
        conn, address = soc.accept()
        print(f"Connected with {address[0]} + {str(address[1])}")
    except OSError as e:
        print(e)


def connection_establishing():
    pass


while True:
    try:
        binding_socket()
        listening_connection()
    except Exception as e:
        print(e)
    break
