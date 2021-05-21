**_Построение схемы наследования_**

Вопрос +1 Что из родительского класса не наследуется потомком?
 * Метод __init__
 * Публичные переменные родительского класса
 * **Приватные методы родительского класса**
 * Публичные методы родительского класса
 * **Приватные переменные родительского класса**
 
Вопрос +2 Что относится к сильным сторонам наследования?
 * Концентрация всей информации об объекте и его методах в одном классе
 * **Отсутствие необходимости переписывания всех классов-потомков при изменениях в базовом классе**
 * **Отсутствие необходимости дублировать код**
 * Единый интерфейс для всех потомков базового класса
 
Вопрос +3 В чем заключается множественное наследование?
 * Все вышеперечисленное
 * В системе существуют разные базовые классы, от которых наследуются разные классы-потомки
 * У одного родительского класса есть несколько классов-потомков
 * **У одного класса-потомка есть несколько родительских классов**
 
Вопрос +4 Каким методом разрешается проблема Ромба Смерти?
 * **С3-линеаризация**
 * Обход графа наследования в ширину
 * Обход графа наследования в глубину
 * Алгоритм Тарьяна
 
Вопрос -5 Зачем нужны абстрактные классы?(не верно!!)
 * Абстрактные классы нигде не используются
 * Для реализации полиморфизма
 * **Для создания классов, которые не предполагают создания экземпляров**
 * Для решения проблемы Ромба Смерти
 
Вопрос +6 Для чего применяются абстрактные методы?
 * Чтобы предотвратить создание экземпляра класса
 * **Чтобы определить интерфейс, реализацию для которого необходимо реализовать в классах потомках**
 * Чтобы некоторый метод при наследовании был передан классу-потомку
 * Для указания конкретной реализации интерфейса на этапе выполнения кода

Вопрос +7 Что позволяют делать виртуальные методы?
 * Позволяют  определить интерфейс, реализацию для которого необходимо реализовать в классах потомках  
 * **Позволяют указывать конкретную реализацию интерфейса на этапе выполнения кода** 
 * Позволяют предотвратить создание экземпляра класса 
 * Позволяют определить функцию, которая может не иметь реализации

Вопрос +8 Какая библиотека используется для работы с абстрактными классами и методами?
 * xyz
 * abs
 * **abc**
 * abstract

Вопрос +9 Что выведет приведенный ниже код?
from abc import ABC, abstractmethod


class A(ABC):
  def __init__(self):
    self.var1 = 5
    self.var2 = 7
  
  @abstractmethod
  def do_something(self):
    print(self.var1 + self.var2)


class B(A):
  def __init__(self):
    self.var1 = 2


obj = B()
obj.do_something()

 * Ошибку, так как не определено значение var2 для B  
 * 12
 * 9
 * **Ошибку, так как нет реализации абстрактного метода**
 * 2