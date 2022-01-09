<h1>Anotações sobre o livro <strong>"Entendo Algoritmos"</strong> de Aditya Y. Bhargava</h1>

<https://github.com/egonSchiele/grokking_algorithms>


<h2>

Capítulos

 - [1 - Introdução a algoritmos](#1---introdução-a-algoritmos)
 - [2 - Ordenação por seleção](#2---ordenação-por-seleção)
 - [3 - Recursão](#3---recursão)
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
  - Lógica da busca binária:
    1. Ache o elemento central
    2. O elemento cetral é o elemento procurado? Se sim, retorna o index dele
    3. Se o elemento central é menor do que o procurado, então elimine todos os itens menores do que o elemento central
    4. Se o elemento central é maior do que o procurado, então elimine todos os itens maiores do que o elemento central
    5. Repetir os passos anteriores até encontrar
    6. Se o elemento não é encontrado, então retorne None
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
  - De maneira geral, a notação big O pode ser escrita como O(f(n)), onde f(n) é uma função que fornece o número de operações que um algoritmo realiza em função do tamanho da entrada
  - ***A notação Big O conta o número de operações***
  - A notação big O nos dá a taxa de crescimento do tempo de execução em função do tamanho da entrada
  - A notação Big O leva em conta a pior das hipóteses para contar o número de operações
  - Além do tempo de execução para o pior caso, é importante analisar o tempo de execução para o caso médio. Isso é tratado em [4 - Quicksort](#4---quicksort)
  - Alguns exemplos comuns de tempo de execução Big O (ordenado do mais rápido para o mais lento)
    - O(log n), tempo logarítmico. Exemplo: pesquisa binária
    - O(n), tempo linear. Exemplo: pesquisa simples (ou linear)
    - O(n * log n). Exemplo: quicksort
    - O(n²). Exemplo: selection sort
    - O(n!). Exemplo: caixeiro-viajante
  - **Principais pontos**:
    - ***A rapidez de um algoritmo não é medida em segundos, mas pelo crescimento do número de operações***
    - Discutimos sobre o quão rapidamente o tempo de execução de um algoritmo aumenta conforme o número de elementos (tamanho do input) aumenta
    - O tempo de execução em algoritmos é expresso na notação Big O
    - O(log n) é mais rápido do que O(n), e O(log n) fica ainda mais rápido conforme a lista aumenta

## 2 - Ordenação por seleção

- Como funciona a memória
  - O computador se parece com um grande conjunto de gavetas, e cada gaveta tem seu endereço. O conjunto de gavetas é chamado de memória. Podemos armazenar coisas nas gavetas. Cada 'gaveta' é um slot/espaço na memória
  - Cada vez que queremos armazenar um item na memória, pedimos ao computador um pouco de espaço e ele nos dá um endereço no qual podemos armazenar o item que queremos
  - ***Se quisermos armazenar múltiplos itens, existem duas maneiras para fazer isso: arrays e listas encadeadas***

- Arrays e listas encadeadas
  - Arrays armazenam itens contiguamente (um do lado do outro) na memória
  - Se você quiser adicionar um novo item ao array, você precisa solicitar ao computador uma área de momória que caiba todos os itens contiguamente
  - Adicionar novos itens a um array é lento
  - Um jeito de contornar o problema de adição de itens a um array é 'reservar lugares', mesmo que não utilize todos. Porém, isso traz desvantagens:
    - Você pode não precisar dos espaços extras reservados, então a memória será desperdiçada. Vocẽ nao está utilizando memória, mas ninguém pode usá-la também
    - Você pode precisar adicionar mais itens (além do número de espaços reservados), então você terá de mover todos os itens para um novo espaço de memória que caiba todos
  - Listas encadeadas resolvem o problema da adição de itens

- Listas encadeadas
  - Com listas encadeadas, seus itens podem estar em qualquer lugar da memória. Cada item armazena o endereço do próximo item da lista, endereços de aleatórios de memória ficam ligados
  - Adicionar um item a uma lista encadeada é fácil: você o coloca em qualquer lugar da memória e armazena o endereço no item anterior
  - Com listas encadeadas, nunca precisamos mover seus itens
  - Listas encadeadas são muito melhores do que arrays para inserções de novos itens
  - Só podem lidar com acesso sequencial
  - É uma prática comum acompanhar o primeiro e o último item de uma lista encadeada para que o tempo de execução para deletá-los seja O(1)

- Arrays
  - Listas encadeadas são ótimas se você quiser ler todos os itens, um de cada vez, mas se você quiser pular de um item para outro, as listas encadeadas são terríveis. Se quiser ler apenas o último item da lista, você precisa percorrer todos os outros itens antes, perguntando a cada um deles o endereço de memória do próximo item até chegar no último, pois não tem como saver seu endereço de memória sem perguntar para o item anterior
  - Com arrays isso é diferente, você sabe o endereço de memória de cada item
  - Arrays são ótimos se você deseja ler elementos aleatórios, pois pode encontrar qualquer elemento instantaneamente
  - Com listas encadeadas, os elementos não estão próximos uns dos outros, não há como calcular instantaneamente a posição de um endereço na memória
  - Podem lidar com acesso aleatório
  - **Terminologia:**
    - Os elementos de um array são numerados. Essa numeração começa no item 0
    - A posição de um elemento é chamado de índice
  
- Tempo de execução para operações comuns de arrays e listas:
  - Obs.: inserções e eliminações terão tempo de execução constante se, e somente se, o elemento a ser deletado ou inserido puder ser acessado instantaneamente
  - O(n) = tempo de execução linear
  - O(1) = tempo de execução constante
  - Leitura:
    - arrays: O(1)
    - listas: O(n)
  - Inserção:
    - arrays: O(n)
    - listas: O(1)
  - Eliminação:
    - arrays: O(n)
    - listas: O(1)

- Tipos de acesso:
  - Sequencial: ler os elementos, passando um por um
  - Aleatório: ler os elementos diretamente

- Ordenação por seleção
  - É um algoritmo bom, mas não muito rápido
  - Serve para ordenar elementos numa lista
  - Você precisa buscar o menor item e colocar na primeira posição, achar o segundo menor item e botar na segunda posição e assim por diante
  - Para achar o menor item numa lista é preciso percorrer n elementos, ou seja isso tem um tempo de execução O(n)
  - Achar o menor item precisa ser repetido n vezes a operação O(n)
  - Ache o menor elemento dentre os n elementos, depois o segundo menor dentre os n - 1 elementos, isso se repete até checar apenas um elemento. A soma dessas operações dá (n² + n) / 2
  - Ou seja, o tempo de execução da ordenação por selecção é O(n²)
  - A lógica da ordenação por seleção:
    1. Ache o menor item, coloque-o na primeira posição
    2. Ache o segundo menor item, coloque-o na segunda posição
    3. Ache o terceiro menor item, coloque-o na terceira posição
    4. Ache o quarto e assim por diante até que o array esteja ordenado
  - [Algoritmo da ordenação por seleção](algorithms/selection_sort.py):

    ```python
    def get_smallest_element_index(array):
        smallest_element_index = 0 # Current smallest element index
        smallest_element = array[0] # Current smallest element

        for index in range(1, len(array)):
            if array[index] < smallest_element:
                smallest_element = array[index]
                smallest_element_index = index

        return smallest_element_index


    def selection_sort(array):
        new_array = []

        for _ in range(len(array)):
            smallest_index = get_smallest_element_index(array) # Find the smallest element index
            new_array.append(array.pop(smallest_index))

        return new_array
    ```

- ***Principais pontos***
  - A memória do computador é como um conjunto gigante de gavetas
  - Quando se quer armazenar múltiplos elementos, usa-se array ou list encadeada
  - No array, todos os elementos são armazenados um do lado do outro
  - Na lista, os elementos estão espalhados e um elemento armazena o endereço do próximo elemento
  - Arrays permitem leituras rápidas
  - Listas encadeadas permitem rápidas inserções e eliminações
  - Todos os elementos de um array deve, ser do mesmo tipo
  - ***Arrays e listas encadeadas são os blocos fundamentais para estruturas de dados mais complexas***

## 3 - Recursão

- Recursão é quando uma função chama a si mesma
- *Ela é usada para tornar a resposta mais clara*
- Não há benefício quanto ao desempenho ao utilizar recursão
- Loops algumas vezes são melhores para o desempenho de um programa

- Caso-base e caso recursivo
  - Devido ao fato de a função recursiva chamar a si mesma, é mais fácil escrevê-la erroneamente e acabar em um loop infinito
  - Quando você escreve uma função recursiva, deve informar quando a recurção deve parar
  - *Por isso, toda função recursiva tem duas partes:*
    - ***Caso-base:*** é quando a função nao chama a si mesma novamente, de forma que o programa não se torne um loop infinito
    - ***Caso recursivo:*** é quando a função chama a si mesma

- A pilha
  - Pilha de chamada ou *call stack*, é um conceito importante em programção e indispensável para entender a recursão
  - É uma estrutura de dados simples. Quando se insere um item, ele é colocado no topo da pilha. Quando se lê um item, lê apenas o topo da pilha e ele é retirado da pilha.
  - Inserir um novo item ao topo (push)
  - Remover o item do topo e lê-lo (pop)

- A pilha de chamada
  - Seu computador usa uma pilha interna denominada *pilha de chamada*
  - Seu computador, a cada chamada de função, aloca um caixa na memória para a chamada e então salva na memória os valores para todas as variáveis
  - Quando você chama uma função a partir de outra, a chamada de função fica pausada em um estado parcialmente completo. Todos os valores das variáveis para aquela função ainda estão armazenados na memória
  - É utilizado uma pilha para guardar as chamadas de funções a partir de funções
  - A pilha de chamada é usada para guardar as variáveis de múltiplas funções

- A pilha de chamada com recursão
  - As funções recursivas também utilizam a pilha de chamada
  - Usar pilha é bom, porém, existe um custo: salvar toda essa informação pode ocupar muita memória
  - Para a situação de muito espaço de memória ocupado, há duas opções:
    - Reescrever o código utilizando loops
    - Utilizar tail recursion

- ***Principais pontos***
  - Recursão é quando uma função chama a si mesma
  - Toda função recursiva tem dois casos: o caso-base e o caso recursivo
  - Uma pilha tem duas operações: push e pop
  - Todas as chamadas de função vão para a pilha de chamada
  - A pilha de chamada pode ficar muito grande e ocupar muita memória

## 4 - Quicksort

- Dividir para conquistar (DC)
  - É uma técnica recursiva muito conhecida para resolução de probleas
  - ***Os algoritmos DC são recursivos***
  - Para resolver um problema utilizando DC, deve-se seguir dois passos:
    1. ***Descobrir o caso-base, que deve ser o caso mais simples possível***
    2. ***Dividir ou diminuir o problema até que ele se torne o caso-base***
  - **A cada recursão deve-se reduzir o problema**
  - O algoritmo DC não é um simples algoritmo que se aplica em um problema, mas sim **uma maneira de pensar sobre o problema**

- Quicksort
  - É um algoritmo de ordenação
  - É muito mais rápido do que o selection sort
  - O algoritmo quicksort também utiliza a estratégia dividir para conquistar
  - Qual é o array mais simples que um algoritmo de ordenação pode ordenar? Arrays vazios ou arrays com apenas um elemento serão o **caso-base**
  - A lógica do quick sort:
    1. Escolha um elemento do array, que será chamado de pivô
    2. Particione o array em dois subarrays, seperando-os entre elementos menores que o pivô e elementos maiores que o pivô
    3. Execute o quicksort recursivamente em ambos os subarrays
  - [Algoritmo do quicksort](algorithms/quick_sort.py)

    ```python
    def quicksort(array):
        if len(array) < 2:
            return array

        pivot = array[0]
        smallers = [i for i in array[1:] if i <= pivot]
        biggers = [i for i in array[1:] if i > pivot]

        return quicksort(smallers) + [pivot] + quicksort(biggers)
    ```
  
- Notação Big O para o quicksort
  - A velocidade do quicksort depende do pivô escolhido
  - Na pior situação, o quicksort tem tempo de execução O(n²)
  - No caso médio, o quicksort tem tempo de execução O(n log n)

- ***Principais pontos***
  - A estratégia DC funciona por meio da divisão do problema em problemas menores. Se você estiver utilizando DC em uma lista, o caso-base provavelmente será um array vazio ou um array com apenas um elemento
  - Se você estiver implementando o quicksort, escolha um elemento aleatório como pivô. O tempo de execução do quicksort é O(n log n)
  - A costante, na notação Big O, pode ser relevante em alguns casos. Está é a razão pela qual o quicksort é mais rápido do que o merge sort
