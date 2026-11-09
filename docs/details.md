# Detalhes sobre o código

## Sockets

socket é uma interface de software que permite aos programas como meu script acessar aos recursos de comunicação do sistema operacional, possibilitando a comunicação entre eles. Dentro do nosso arquivo `server.py` e `client.py` acontece a criação de sockets, onde eles vão ser utilizados para fazer essa comunicação entre os scripts.

`with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:`

O `with` é utilizado para simplificar a conexão e garantindo que elas sejam fechadas com segurança mesmo que ocorram erros, ele ajuda a melhorar a legibilidade e reduzir os `try-except`. Já o `socket` na programação pode ser considerado um nó (dispositivo) que escuta em uma porta específica em um endereço IP, o server cria o `socket` de escuta e o cliente tenta se conectar à ele. Então criamos um nó com `socket` de forma simplificada com `with` dentro deles utilizamos dois parâmetros um é o `AF_INET` que se refere à família de endereços IPv4, e o outro é `SOCK_STREAM` que significa protocolo TCP orientado a conexão, isso quer dizer que vamos utilizar IPv4 e TCP como protocolo.

<img src="assets/client-server.png" alt="" style="display: block; margin: 20px auto; max-width: 80%; height: auto; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.3);">

## Binding

`server.bind((HOST, PORT))` e `server.listen(1)`

`as server` seria como se eu tivesse criado uma variável para armazenar o contexto daquela operação. Consequentemente podemos usar ela para criar o `bind` que vai vincular um endereço IPv4 e uma porta ao `socket`, permitindo ele escutar no endereço e porta escolhida. O parênteses mais interior é uma tupla que espera o formato esperado de `HOST, PORT`. Já o `listen` serve para receber conexões, 1 significa que ela aceita somente uma conexão também conhecido como backlog.

## Accept

`conn, addr = server.accept()`

Aqui o server aceita a conexão, `conn` representa a conexão e o `addr` representa o endereço.

## Makefile

`with conn.makefile("r", encoding="utf-8") as entry:`

`makefile` transforma a conexão do socket `conn` em um objeto de arquivo, isso significa que você poderá ler os dados da rede exatamente da mesma forma que leria um arquivo de texto comum no seu computador. O `r` especifica que este objeto de arquivo está sendo aberto no modo de leitura, `encoding` instrui o python a decodificar automaticamente os bytes recebidos para texto utilizando o `utf-8`.

## Command

`command = input("lab> ").strip()`

É uma variável que representa o `input` do lado do servidor após a conexão, agora quando se conectar ele ficará assim: `lab> <digite algo>`.

## Order
