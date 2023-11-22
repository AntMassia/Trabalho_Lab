A função retorna uma lista com as cinco palavras definidas na linha 2.

Função escolher_palavra():
Essa função escolhe uma palavra aleatória da lista de palavras.

O Passo a Passo é o Seguinte:
A função usa a função random.choice() para escolher uma palavra da lista de palavras.
A função remove a palavra escolhida da lista de palavras para que ela não seja escolhida novamente.
A função retorna a palavra escolhida.

Função validar_palavra():
Essa função verifica se uma palavra é composta apenas de letras.

A função usa a função isalpha() para verificar se cada letra da palavra é uma letra.
Retorna True se todas as letras da palavra forem letras, ou False caso contrário.

Função exibir_tabuleiro():
Essa função exibe o tabuleiro para o jogador, destacando as letras corretas na posição exata, as letras corretas, mas na posição errada, e as letras ausentes na palavra.

A função verifica se as palavras têm o mesmo tamanho. Se não tiverem, a função gera uma exceção.
Ela cria uma lista de índices das posições corretas.
A função itera sobre as letras da palavra e do palpite, comparando cada uma.
Se a letra está na posição correta, a função imprime o símbolo "🟩".
Se a letra está na palavra, mas não na posição correta, a função imprime o símbolo "🟨".
Caso contrário, a função imprime o símbolo "⬛".

Função processar_palpite():
Essa função processa o palpite do jogador, verificando se ele é válido e se acertou a palavra.

Essa função verifica se o palpite já foi digitado pelo jogador. Se sim, a função imprime uma mensagem de erro.
Ela adiciona o palpite a uma lista de palavras já digitadas.
A função verifica se o palpite é composto apenas de letras. Se não for, a função imprime uma mensagem de erro.
Retorna o palpite.

Função main():
Essa função é a função principal do jogo. Ela é responsável por escolher uma palavra aleatória, iniciar o jogo, e processar os palpites do jogador.

Ela escolhe uma palavra aleatória.
E inicia o jogo, definindo um número máximo de tentativas.
Enquanto o jogador ainda tiver tentativas:
A função pede um palpite ao jogador.
A função processa o palpite do jogador.
Se o palpite for correto, o jogo termina.
Caso contrário, a função exibe o tabuleiro para o jogador e decrementa o número de tentativas.
Se o jogador não acertar a palavra no número máximo de tentativas, o jogo termina e a palavra secreta é revelada.
