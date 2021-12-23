<h1>Anotações sobre o livro <strong>"Entendo Algoritmos"</strong></h1>


<h2>

Capítulos

 - [1 - Introdução a algoritmos](#1---introdução-a-algoritmos)
 - [2 - Ordenação por seleção](#2---ordenação-por-seleção)
 - [4 - Quicksort](#4---quicksort)

</h2>

## 1 - Introdução a algoritmos

- Introdução
  - Um algoritmo é um conjunto de instruções que realizam uma tarefa

- Pesquisa Binária
  - É um algoritmo que resolve o problema de busca. Sua entrada é uma lista ordenada de elementos. Se o elemento buscado está na lista, a pesquisa binária retorna a sua localização. Senão, retorna None.
  - Com a pesquisa binária, você chuta um número intermadiário e elimina a metade dos números restantes a cada vez.
  - Para uma lista de n elementos, a pesquisa bínaria precisa de log2(n) (log de n na base 2) etapas para retornar o valor correto, enquanto que a pesquisa simples (ou linear) precisa de n etapas.
  - A pesquisa binária só funciona quando a *lista está ordenada*
  - A pesquisa binária é executada com tempo logarítmico
  - [Algoritmo da busca binária](algorithms/binary_search.py):

    ```python
    # Binary Search
    def binary_search(array, item):
        low = 0
        high = len(array) - 1

        while low <= high:
            half = (low + high) // 2
            guess = array[half]

            if guess == item:
                return half
            elif guess <= item:
                low = half + 1
            else:
                high = half - 1

        return None
    ```

- Notação Big O
  - É uma notação especial que diz o quão rápido é um algoritmo
  - Tempo de execução dos algoritmos cresce a taxas diferentes
  - Não basta saber quanto tempo um algoritmo leva para ser executado, pois isso depende de fatores externos como processador, linguagem, memória etc.
  - É mais importante saber se o tempo de execução aumenta conforme o tamanho da entrada aumenta
  - A notação Big O informa quão rápido é um algoritmo, quão rapidamente ele cresce
  - A notação não fornece o tempo em segundos
  - Ela permite que você compare o número de operações
  - Por exemplo, a busca binária precisa de log n operações pra verificar uma lista de tamanho n. Logo, a notação Big O para o binary sort é O(log n)
  - De maneira geral, a notação big O pode ser escrita como O(f(n)), onde f(n) é uma função que fornece o número de operações que um algoritmo realiza
  - ***A notação Big O conta o número de operações***
  - A notação big O nos dá a taxa de crescimento do tempo de execução em função do tamanho da entrada
  - A notação Big O leva em conta a pior das hipóteses para contar o número de operações
  - Além do tempo de execução para o pior caso, é importante analisar o tempo de execução para o caso médio. Isso é tratado em [4 - Quicksort](#4---quicksort)
  - Alguns exemplos comuns de tempo de execução Big O (ordenado do mais rápido para o mais lento)
    - O(log n), tempo logarítmico. Exemplo: pesquisa binária
    - O(n), tempo linear. Exemplo: pesquisa simples (ou linear)
    - O(n * log n). Exemplo: quicksort
    - O(n²). Exemplo: selection sort
    - O(n!). Exemplo caixeiro-viajante
  - **Principais pontos**:
    - ***A rapidez de um algoritmo não é medida em segundos, mas pelo crescimento do número de operações***
    - Discutimos sobre o quão rapidamente o tempo de execução de um algoritmo aumenta conforme o número de elementos (tamanho do input) aumenta
    - O tempo de execução em algoritmos é expresso na notação Big O
    - O(log n) é mais rápido do que O(n), e O(log n) fica ainda mais rápido conforme a lista aumenta

## 2 - Ordenação por seleção

## 4 - Quicksort
