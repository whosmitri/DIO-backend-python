# Construtores e Destrutores em Python

Em Programação Orientada a Objetos (POO), construtores e destrutores são métodos especiais utilizados para controlar o ciclo de vida de um objeto, desde sua criação até sua remoção da memória.

## Método Construtor

O método construtor é um método especial que é executado automaticamente no momento em que uma nova instância de uma classe é criada.

### Funções principais do construtor
* Inicializar o estado interno do objeto (atributos).
* Garantir que o objeto seja criado em um estado válido.
* Receber parâmetros iniciais necessários para a instância.

### Declaração

Em Python, o construtor é declarado por meio do método especial:

```python
__init__(self, ...)
```
* O parâmetro self representa a própria instância do objeto.
* Os demais parâmetros são valores fornecidos no momento da criação do objeto.

### Exemplo de código
```python
class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
```
* **Explicação do exemplo**
    * nome, cor e acordado são atributos do objeto.
    * O parâmetro acordado=True possui um valor padrão, o que o torna opcional na criação da instância.
    * A palavra-chave self é utilizada para associar os parâmetros recebidos aos atributos do objeto.

## Métodos Especiais (`__nome__`)

Os métodos que possuem o padrão `__nome__` são chamados de métodos especiais (ou *magic methods* / *dunder methods*).

### Características:
* São invocados automaticamente pelo Python em situações específicas.
* Permitem personalizar comportamentos internos da linguagem.
* Exemplos comuns:
    * `__init__`: inicialização do objeto
    * `__del__`: destruição do objeto
    * `__str__`: representação em string
    * `__len__`: tamanho do objeto

## Método Destrutor

O método destrutor é executado quando uma instância está prestes a ser removida da memória.

### Declaração
Em Python, o destrutor é definido pelo método especial:
```python
__del__(self)
```

### Exemplo de código
```python
class Cachorro:
    def __del__(self):
        print("Destruindo a instância")
```

### Uso
```python
c = Cachorro('yongmeong', "branco")
del c
```

Ao executar `del c`, o Python remove a referência ao objeto e, se não houver outras referências ativas, o método `__del__` será chamado.

## Observações sobre destrutores
* Diferentemente de linguagens como C++, o uso de destrutores em Python é menos comum.
* Python possui um coletor de lixo (Garbage Collector) que gerencia automaticamente a memória.
* O método `__del__`:
    * Não garante execução imediata
    * Pode não ser chamado em situações como encerramento do programa
    * Deve ser evitado para lógica crítica


## Resumo
* `__init__`:
    * Inicializa o objeto
    * Define atributos
    * É essencial em POO

* `__del__`:
    * Executado na destruição do objeto
    * Uso limitado e não determinístico
    * Geralmente dispensável em Python moderno