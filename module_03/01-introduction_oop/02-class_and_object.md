# Conceitos de Classes e Objetos em Python

A Programação Orientada a Objetos (POO) é um paradigma de programação que organiza o código em torno de objetos, os quais representam entidades do mundo real ou conceitos abstratos. Esses objetos são criados a partir de classes, que funcionam como modelos.

## Classe

Uma classe é uma estrutura que define:
* Características (atributos)
* Comportamentos (métodos)

Ela funciona como um molde ou modelo, mas não pode ser utilizada diretamente para executar ações. Para isso, é necessário criar objetos a partir dela.

### Características principais de uma classe
* Define a estrutura dos objetos
* Agrupa dados e funções relacionadas
* Facilita reutilização de código
* Melhora organização, manutenção e escalabilidade

### Exemplo de definição de classe

```python
class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def latir(self):
        print("au au")

    def dormir(self):
        self.acordado = False
        print("zzz")
```

**Anotações importantes**
* `class Cachorro`: define uma nova classe chamada Cachorro.

* `__init__`: é o método construtor, executado automaticamente quando um objeto é criado, serve para inicializar os atributos do objeto.

* `self`: referência ao próprio objeto que está sendo criado ou manipulado. É obrigatório como primeiro parâmetro dos métodos de instância.

* `acordado=True`: define um valor padrão, permitindo que o parâmetro seja opcional.

* `Métodos (latir, dormir)`: representam os comportamentos que os objetos da classe podem executar.

## Objeto

Um objeto é uma instância concreta de uma classe. Ele possui estado próprio (valores dos atributos) e pode executar os comportamentos definidos na classe.

Em outras palavras: *a classe é o modelo, o objeto é a aplicação prática desse modelo.*

### Exemplo de criação de objetos

```py
cao_1 = Cachorro("chappie", "amarelo", False)
cao_2 = Cachorro("nico", "branco e preto")
```

**Anotações**
* Cada objeto possui seus próprios valores de atributos.
* `cao_1` e `cao_2` são objetos diferentes, mesmo sendo da mesma classe.
* No segundo objeto, o atributo `acordado` usa o valor padrão (`True`).

## Uso de métodos e atributos

### Chamando métodos
```python
cao_1.latir()
# saída: au au
```

### Acessando atributos
```python
print(cao_2.acordado)
# saída: True
```

### Modificando o estado do objeto
```python
cao_2.dormir()

print(cao_2.acordado)
# saída: False
```

### Observações importantes
* Métodos podem alterar o estado interno do objeto.
* O uso de `self` garante que a modificação afete apenas o objeto que chamou o método.
* Cada objeto mantém seu próprio estado independentemente dos outros.

## Instância

Instanciar significa *criar um objeto a partir de uma classe*.

```python
cao_1 = Cachorro("chappie", "amarelo", False)
```

**Conceito-chave**
* Classe: definição
* Instância (objeto): materialização da definição

**Pode-se afirmar que:**
* Toda instância é um objeto, e todo objeto é uma instância de alguma classe.

## Boas práticas iniciais em POO com Python
* Utilize nomes de classes em PascalCase (`Cachorro`, `ContaBancaria`)
* Utilize nomes de métodos e atributos em snake_case
* Mantenha métodos curtos e com responsabilidades bem definidas
* Evite acessar atributos diretamente quando a lógica ficar complexa (prefira métodos)
* Pense em classes como representações conceituais, não apenas como agrupamentos de código

## Resumo conceitual
* **Classe:** modelo que define atributos e comportamentos
* **Objeto:** entidade concreta criada a partir da classe
* **Instância:** ato de criar um objeto
* **Atributos:** características do objeto
* **Métodos:** ações que o objeto pode executar