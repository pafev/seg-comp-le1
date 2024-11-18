# Lista de Exercícios 1

## Ex1

### Criptografia

A priori, foi realizada uma funcao para criptografia por deslocamento (shift cipher).

Ela possui declaracao no formato:

`encrypt(plain_text: str, key: int) -> str`

ou seja, eh uma funcao que recebe um texto plano (plain text) e uma chave arbitraria (key), sendo ela o numero de deslocamento, para retornar o texto criptografado (cipher_text).

### Ataque (CipherText-only)

Foram realizadas duas funcoes para um ataque a criptografia de deslocamento.

Ambas as funcoes retornam um dicionario, onde a chave do dicionario eh a possivel chave utilizada na criptografia e o valor do dicionario eh o possivel texto plano, considerando sua respectiva chave.

- Por Força Bruta

A funcao tem declaracao:

`descrypt_with_brute_force(cypher_text: str) -> dict`

e apresentou uma ordem de complexidade aproximada de O(26\*n), considerando o fator mais dominante da equacao de complexidade do algoritmo.

- Por Distribuicao de Frequencia

A funcao tem declaracao:

`decrypt_with_frequency_distribution(cypher_text: str) -> dict`

e apresentou uma ordem de complexidade aproximada de O(4\*n), considerando o fator mais dominante e considerando o fato de ela devolver apenas os tres textos planos mais prováveis, com suas respectivas chaves.

Em suma, percebe-se que o ataque a essa criptografia pode ser feita por meio de algoritmos simples, com ordem de complexidade polinomial em grau 1, tendo em vista que a quantidade de valores para a chave (key) eh limitada pela quantidade de algarismos no alfabeto utilizado, tendo em vista que o calculo do deslocamento utilizara o modulo dessa quantidade.

Ademais, o ganho que se percebeu em utilizar a distribuicao de frequencia de ocorrencia dos algarismos do alfabeto utilizado deve-se ao fato de conseguirmos diminuir a quantidade de iteracoes entre os possiveis valores para a chave. Portanto, em vez de, por exemplo, termos que testar a descriptografia para os valores de `key` pertencente ao conjunto [1, 26], podemos testar apenas para os 4 valores mais provaveis para key.

## Ex2

### Criptografia

Foi realizada uma funcao para criptografia por transposicao colunar simples.

Ela possui declaracao no formato:

`encrypt(plain_text: str, key: str) -> str`

ou seja, eh uma funcao que recebe um texto plano (plain text) e uma chave arbitraria (key) para transposicao em colunas, a fim de se retornar o texto criptografado (cipher text).

### Ataque (CipherText-only)

O algoritmo de ataque a criptografia por transposicao nao foi implementado, devido a toda sua complexidade. Em suma, para se atacar essa criptografia e recuperar o texto plano sem conhecimento da chave, percebi que seria necessario sempre testar todas as permutacoes possiveis, ja que a distribuicao de frequencia dos algarismos do alfabeto nao se aplica de forma util a esse ataque, tendo em vista que a permutacao dos caracteres ou o valor da chave independe da quantidade de ocorrencia de cada caractere.

Assim, para um texto curto de 20 caracteres, seria necessario testar 20! casos de permutacao, representando uma ordem de complexidade inviavel caso se deseja executar um ataque a criptografia em tempo habil
