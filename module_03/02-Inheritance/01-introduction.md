# Herança em Programação Orientada a Objetos (POO)

## O que é herança em programação?

Herança é um dos pilares da Programação Orientada a Objetos.
Ela representa a capacidade de uma classe filha (subclasse) herdar atributos e métodos de uma classe pai (classe base ou superclasse).

Por meio da herança, uma nova classe pode reaproveitar comportamentos já definidos, estendendo ou especializando funcionalidades existentes.

Em termos conceituais, a herança representa uma relação do tipo “é um” (is-a).
Exemplo: um `Aluno` é uma `Pessoa`.

## Benefícios da herança

* **Representação de relacionamentos do mundo real**: facilita a modelagem de entidades que compartilham características comuns.

* **Reutilização de código**: evita repetição, pois métodos e atributos definidos na classe pai podem ser reutilizados pelas classes filhas.

* **Facilidade de manutenção**: alterações feitas na classe base refletem automaticamente nas classes derivadas, quando apropriado.

* **Extensibilidade**: permite adicionar ou sobrescrever funcionalidades sem modificar diretamente a classe pai.

* **Herança transitiva**: se a 'classe B' herda da 'classe A', e a 'classe C' herda de 'B', então 'C' também herda os membros de 'A'.

## Sintaxe básica da herança em Python

Em Python, a herança é definida passando a classe pai como argumento na definição da classe filha.

```py
class A:
    pass

class B(A):
    pass
```

* Nesse exemplo:
    * `A` é a classe base (pai)
    * `B` é a classe derivada (filha)
    * `B` herda todos os atributos e métodos públicos de `A`

## Herança simples e herança múltipla

### Herança simples
* Uma classe filha herda apenas de uma classe pai
* É o tipo mais comum e mais simples de herança
* Facilita a leitura, manutenção e compreensão do código

* Exemplo:
    ```py
    class A:
        pass

    class B(A):
        pass
    ```

### Herança múltipla
* Uma classe filha herda de duas ou mais classes pai
* Python permite herança múltipla, mas nem todas as linguagens suportam
* Deve ser usada com cuidado, pois pode aumentar a complexidade do código

* Exemplo:
    ```py
    class A:
        pass

    class B:
        pass

    class C(A, B):
        pass
    ```
* Nesse caso, a classe C herda os membros de A e de B.

## Observações importantes
* A classe filha pode:
    * Usar métodos da classe pai
    * Sobrescrever métodos da classe pai
    * Adicionar novos atributos e métodos

* Caso existam métodos com o mesmo nome em mais de uma classe pai (na herança múltipla), o Python utiliza a ordem de resolução de métodos (MRO – Method Resolution Order) para decidir qual método será executado.

* Nem sempre herança é a melhor solução. Em alguns casos, composição (usar uma classe dentro de outra) é mais adequada.

## Boas práticas
* Utilize herança apenas quando existir uma relação clara de especialização (“é um”)
* Evite hierarquias muito profundas
* Prefira herança simples sempre que possível
* Mantenha as classes base genéricas e reutilizáveis