<h1>Anotações sobre o livro <strong>"Entendo Algoritmos"</strong></h1>


<h2>

Capítulos

 - [1 - Introdução a algoritmos](#1-introdução-a-algoritmos)

</h2>

## 1 - Introdução a algoritmos

- Introdução
  - Um algoritmo é um conjunto de instruções que realizam uma tarefa

- Pesquisa Binária
  - É um algoritmo que resolve o problema de busca. Sua entrada é uma lista ordenada de elementos. Se o elemento buscado está na lista, a pesquisa binária retorna a sua localização. Senão, retorna None.
  - Com a pesquisa binária, você chuta um número intermadiário e elimina a metade dos números restantes a cada vez.
  - Para uma lista de n elementos, a pesquisa bínaria precisa de log2(n) (log de n na base 2) etapas para retornar o valor correto, enquanto que a pesquisa simples (ou linear) precisa de n etapas.
  - A pesquisa binária só funciona quando a *lista está ordenada*

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
