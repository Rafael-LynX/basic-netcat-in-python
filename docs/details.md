# Detalhes sobre o código

Aqui está um explicação detalhada do código `server.py` e `client.py`.

## Sockets

socket é uma interface de software que permite aos programas como meu script acessar aos recursos de comunicação do sistema operacional, possibilitando a comunicação entre eles. Dentro do nosso arquivo `server.py` e `client.py` acontece a criação de sockets, onde eles vão ser utilizados para fazer essa comunicação entre os scripts.

`with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:`

O `with` é utilizado para simplificar a conexão e garantindo que elas sejam fechadas com segurança mesmo que ocorram erros, ele ajuda a melhorar a legibilidade e reduzir os `try-except`. Já o `socket` na programação pode ser considerado um nó (dispositivo) que escuta em uma porta específica em um endereço IP, o server cria o `socket` de escuta e o cliente tenta se conectar à ele. Então criamos um nó com `socket` de forma simplificada com `with` dentro deles utilizamos dois parâmetros um é o `AF_INET` que se refere à família de endereços IPv4, e o outro é `SOCK_STREAM` que significa protocolo TCP orientado a conexão, isso quer dizer que vamos utilizar IPv4 e TCP como protocolo.

<img src="assets/socket.png" alt="" style="display: block; margin: 20px auto; max-width: 80%; height: auto; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.3);">

## Binding

`server.bind((HOST, PORT))` e `server.listen(1)`

`as server` seria como se eu tivesse criado uma variável para armazenar o contexto daquela operação. Consequentemente podemos usar ela para criar o `bind` que vai vincular um endereço IPv4 e uma porta ao `socket`, permitindo ele escutar no endereço e porta escolhida. O parênteses mais interior é uma tupla que espera o formato esperado de `HOST, PORT`. Já o `listen` serve para receber conexões, 1 significa que ela aceita somente uma conexão também conhecido como backlog.

## Accept

`conn, addr = server.accept()`

Aqui o server aceita a conexão, `conn` representa a conexão e o `addr` representa o endereço.

## Makefile

`with conn.makefile("r", encoding="utf-8") as entry:`

`makefile` transforma a conexão do socket `conn` em um objeto de arquivo, isso significa que você poderá ler os dados da rede exatamente da mesma forma que leria um arquivo de texto comum no seu computador. O `r` especifica que este objeto de arquivo está sendo aberto no modo de leitura, `encoding` instrui o python a decodificar automaticamente os bytes recebidos para texto utilizando o `utf-8` ao invés de usar o método bruto como `recv()`.

## Command

`command = input("lab> ").strip()`

É uma variável que representa o `input` do lado do servidor após a conexão, agora quando se conectar ele ficará assim: `lab> <digite algo>`.

## Order

`order = json.dumps({"command}) + "\n"`

A variável `order` utiliza a função `json.dumps()` para converter um objeto python como um dicionário ou lista em uma string formatada em `JSON`, no caso seria o `"command": command`, o json é padrão universal para troca de dados entre diferentes sistemas e linguagens de programação, isso permite que os dados do python sejam preparados para serem transmitidos por uma rede. O `\n` serve para indicar o fim da mensagem, no caso o fim do comando.

`conn.sendall(order.encode("utf-8")`

Os sockets só transmitem bytes brutos como esses em hexadeciamal `\x48\x65\x6c\x6f`, o `encode(utf-8)` transforma cada caractere em sua representação de bytes usando a regras do `utf-8`. Após isso o `conn.sendall()` é usado para garantir que todo o pacote de bytes sejam transmitidos integralmente pela conexão TCP.

`line = entry.readline()`

Aqui o script entra em estado de espera até receber uma resposta da rede. A variável `entry` representa aquele objeto de arquivo gerado pelo `makefile`, com ele conseguimos usar o `readline` para ler os dados recebidos de forma limpa, ele vai escutando a rede e acumulando cada byte que chega, exatamente até a quebra de linha `\n`.

## Response

`response = json.loads(line)`

`line` seria uma string bruta recebida do servidor, agora ela é apenas um texto sem estrutura no formato JSON. O `json.loads` é uma função inversa do `json.dumps`, a letra `s` em `loads` significa `string`, ela pega a variável `line` que contém o texto no formato JSON e a analisa sintática ou interpretação (parse) afim de identificar sua estrutura para que o script consiga entendê-la e trabalhar com ela. A ideia é usar o JSON para viajar pela rede e quando ele chegar no script ser reconstruído sua estrutura de dados original em python, então ele virará de novo um dicionário.

`if response["exit"]`

Isso verifica no dicionário `response` se a chave `exit` possui o valor avaliado como verdadeiro, isso indicaria o fechamento da conexão.

`print(response["exit"], end=""`

Imprime o conteúdo da chave `exit`. O argumento `end=""` evita que python adicione automaticamente uma nova linha após imprimir o valor, permitindo um controle mais fino sobre a formação do terminal.

`if not response["exit"].endswith("\n")`

Esta estrutura condicional verifica se a string impressa não terminou com uma quebra de linha. Se não terminou, o código força a impressão de uma linha em branco chamando `print()` sem argumentos. Isso evita que o próximo texto não fique colado não mesma linha da saída anterior, mantendo uma interface limpa e organizada.

## Execute

`subprocess.run`

Representa a maneira recomendada no python3 para executar comandos do sistema operacional substituindo o `check_output`.

`shell=True`

Instrui o python a rodar o comando através do shell real do sistema operacional como /bin/sh no linux ou cmd.exe no windows. Porém o `shell=True` não é recomendado para segurança ele está proposto a injeção de comandos no shell.

`stdin=subprocess.DEVNULL`

O `DEVNULL` descarta os dados escritos nele ou fornece uma entrada vazia, isso evita que o servidor trave.

`stdout=subprocess.PIPE`

Captura todo o texto gerado pelo comando `result` e o joga em tubo pipe interno, impedindo que seja impresso diretamente na tela do servidor e permitindo que seu script python armazene esse resultado na variável `result`

`stderr=subprocess.STDOUT`

Funde a saída de erros (Standard Error) na saída padrão (Standard Output). Se o usuário digitar um comando que não existe, a mensagem de erro comando não encontrado será capturado no mesmo pacote do resultado normal e envia de volta ao cliente.

`text=True`

Diz ao módulo `subprocess` para decodificar automaticamente a saída do comando de bytes brutos para uma string nativa do python, facilitando a manipulação antes do envio pela rede.

`errors="replace"`

É uma medida de segurança e estabilidade, quando o sistema operacional retornar algum caractere estranho ou malformado que `utf-8` não consiga decodificar, ele vai ser substituído por um símbolo de interrogação de erro ao invés de travar o programa.

`"exit": result.stdout`

Pega todo o texto que o comando gerou no terminal. Incluindo mensagens de erro normais do terminal, como arquivo não encontrada.

`"code": result.returncode`

Pega o código de status numérico que o sistema operacional devolveu.
