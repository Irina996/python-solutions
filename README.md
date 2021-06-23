# Задачи
## Задача 1
### Напишите генератор сочетний C(n, m)

**Решение:** [здесь](./main1.py)
## Задача 2
### Напишите генератор размещений A(n,m)

**Решение:** [здесь](./main2.py)
## Задача 3
### Напишите генератор перестановок P(n)

**Решение:** [здесь](./main3.py)
## Задача 4
### Неизвестно

**Решение:** [нет](https://vk.com/video303007735_456239505)
## Задача 5
### Неизвестно

**Решение:** [нет](https://vk.com/video303007735_456239505)
## Задача 6
### Напишите итератор, который возвращает размещения A(n,m)

**Решение:** [здесь](./main6.py)
## Задача 7
### Удаление дубликатов из Sorted Linked List
Реализовать функцию delete_duplicates(head: Node) -> Node

Kласс Node имеет следующее представление:

```python
class Node:
  def __init__ (self, value=0, next=None):
    self.value = value 
    self.next = next
```

**Решение:** [здесь](./main7.py)
## Задача 8
### Разделение Linked List
Реализовать функцию partition(head: Node, x: int) -> Node, которая принимает голову Linked List и число x, и разделяет его по следующим правилам:
- все узлы списка меньше чем x должны идти до узлов, которые больше или равны x
- оригинальный порядок должен быть сохранён

Класс Node имеет следующее представление
```python
class Node:
	def __init__(self, value=0, next=None):
		self.value = value
		self.next = next
```

Примеры:
Input | Output
----- | ------
head = [1,4,3,2,5,2], x = 3 | [1,2,2,4,3,5]
head = [2,1], x = 2 | [1,2]

**Решение:** [здесь](./main8.py)
## Задача 9
### Вставка интервала
Реализовать функцию, которая принимает список непересекающихся интервалов, вам нужно вставить новый интервал и смержить интервалы (если необходимо).

Примеры:
Input | Output
----- | ------
intervals = [[6,9], [1,3]], newInterval = [2,5] | [[1,5],[6,9]]
intervals = [[3,5],[8,10],[1,2],[6,7],[12,16]], newInterval = [4,8] | [[1,2],[3,10],[12,16]]

**Решение:** [здесь](./main9.py)
## Задача 10
### Количество островов
Дана матрица n x m, которая представляет собой карту области 1 - земля, 0 - вода. Остров – это связная область земли (связи могут быть только горизонтально и вертикально). Необходимо посчитать количество островов.

**Решение:** [здесь](./main10.py)
## Задача 11
### Неизвестно

**Решение:** [нет](https://vk.com/video303007735_456239505)
## Задача 12
### Глубина бинарного дерева
Дан корень бинарного дерева, необходимо найти его глубину.

Узел дерева представляет собой:
```python
class Node:
  def __init__(self, value=0, left=None, right=None):
    self.value = value 
    self.left = left 
    self.right = right
```

**Решение:** [здесь](./main12.py)
## Задача 13
### Неизвестно

**Решение:** [нет](https://vk.com/video303007735_456239505)
## Задача 14
### Реализовать сортировку слиянием

**Решение:** [здесь](./main14.py)
## Задача 15
### Реализуйте алгоритм быстрой сортировки

**Решение:** [здесь](./main15.py)
## Задача 16
### Реализуйте паттерн Singleton с помощью декоратора

**Решение:** [нет](https://vk.com/video303007735_456239505)
## Задача 17
### Реализуйте паттерн Singleton с помощью метакласса

**Решение:** [нет](https://vk.com/video303007735_456239505)
## Задача 18
### Реализуйте паттерн Singleton (base class)

**Решение:** [нет](https://vk.com/video303007735_456239505)
## Задача 19
### Параметризированный декоратор (общий вид)

**Решение:** [нет](https://vk.com/video303007735_456239505)
## Задача 20
### Параметризованный декоратор expired_cache
Декоратор @expired_cache(t), который возвращает значении функции при каждом вызове на время t. Если функция вызвана повторно с теми же аргументами, то возвращается сохранённое значение, а функция не вычисляется. Учесть как позиционные, так и именованные аргументы.

**Решение:** [здесь](./main20.py)
## Задача 21
### Параметризованный декоратор cached с ограничением на размер
Декоратор @cached(size), который сохраняет значение функции при каждом вызове. Если функция вызвана повторно с теми же аргументами, то возвращается сохранённое значение, а функция не вычисляется. Учесть как позиционные, так и именованные аргументы.

**Решение:** [здесь](./main21.py)
## Задача 22
### Параметризованный декоратор (сортировка аргументов)
Параметризованный декоратор, который сортирует переданные аргументы с помощью переданного компаратора: при создании декоратора, делать проверку на то, что переданный параметр функция

**Решение:** [здесь](./main22.py)
## Задача 23
### Класс n-мерный вектор
Реализовать класс и методы: сложение, вычитание, сравнение на равенство, строковое представление

**Решение:** [нет](https://vk.com/video303007735_456239505)
## Задача 24
### Проверить математическое выражение на корректность записи
Математическое выражение может содержать только целые числа и операции +, -, /, *, а также скобки разных видов

Ожидается проверка по 2-м пунктам:

- регулярное выражение
- баланс скобок

**Решение:** [нет](https://vk.com/video303007735_456239505)
## Задача 25
### Проверить выражение на баланс скобок (три вида скобок: “{}”, “()”, “[]”)

**Решение:** [нет](https://vk.com/video303007735_456239505)
## Задача 26
### Проверить выражение на баланс скобок
Пар скобок может быть сколько угодно, пары скобок задаются аргументами, где каждая пара это кортеж, где 1-й элемент - это открывающаяся, 2-й - закрывающаяся.

Необходимо реализовать функцию check, которая будет работать следующим образом:
```python
print (check “([]”, (“(“, ”)”))) #True
print (check “([)]”, (“(“, ”)”))) #False
print (check “({{}]})”, (“{“, ”}”), (“(“, ”)”))) #True
print (check “({{}]})”, (“{“, ”}”), (“(“, ”)”)), (“[“, ”]”))) #False
```

**Решение:** [нет](https://vk.com/video303007735_456239505)
## Задача 27
### Task Scheduler
Дан массив символов задач, представляющих задачи, которые должен выполнить CPU, где каждая задача представляет отдельную задачу. Задания можно выполнять в любом порядке. Каждая задача выполняется за одну единицу времени. За каждую единицу времени CPU мог выполнить либо одну задачу, либо бездействовать.

Существует неотрицательное число n, которое представляет период восстановления между двумя одинаковыми задачами. То есть между любыми двумя одинаковыми задачами должно быть не менее n единиц времени.

Необходимо найти минимальное количество времени, которое потребуется CPU для завершения всех задач.

**Input:** tasks = ["A","A","A","B","B","B"], n = 2
**Output:** 8
**Explanation:** A -> B -> idle -> A -> B -> idle -> A -> B

**Решение:** [здесь](./main27.py)
## Задача 28
### Последовательность с фильтрацией
Реализовать класс, соответствующий некоторой последовательности объектов и имеющий следующие методы:
- Создать объект на основе произвольного iterable объекта.
- Итерирование (**iter**) по элементам (неистощимое - можно несколько раз использовать объект в качестве iterable для for).
- Отфильтровать последовательность с помощью некоторой функции и вернуть новую сокращенную последовательность, в которой присутствуют только элементы, для которых эта функция вернула True.

**Решение:** [нет](https://vk.com/video303007735_456239505)
## Задача 29
### Метакласс, берущий поля класса из файла
Реализовать метакласс, который позволяет при создании класса добавить к нему произвольные атрибуты (классу, не экземпляру класса), которые загружаются из файла. В файле должны быть имена атрибутов и их значения. Нужно уметь передавать путь к файлу как изменяемый параметр.

**Решение:** [нет](https://vk.com/video303007735_456239505)
## Задача 30
### Binary Search Tree Iterator
Реализуйте класс BSTIterator, который представляет собой итератор по обходу бинарного дерева по порядку

Узел представляет собой
```python
class Node:
  def  __init__(self, value=0, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right
```

**Решение:** [здесь](./main30.py)
## Задача 31
### Binary Search Tree Generator
Реализуйте класс BSTGenerator, который представляет собой генератор по обходу бинарного дерева по порядку

Узел представляет собой
```python
class Node:
  def  __init__(self, value=0, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right 
```

**Решение:** [здесь](./main31.py)
## Задача 32
### Flatten Nested List Iterator
Вам дан вложенный список целых чисел. Каждый элемент списка – это или целое число, или вложенный список.
Вам необходимо написать итератор, который будет возвращать числа по порядку.

Примеры:
Input | Output
----- | ------
[1,1],2,[1,1]] | 1 1 2 1 1
[[1,[1, 3]],2,[1,4, [6]]]] | 1 1 3 2 1 4 6

**Решение:** [здесь](./main32.py)
## Задача 33
### Flatten Nested List Generator
Вам дан вложенный список целых чисел. Каждый элемент списка – это или целое число, или вложенный список.
Вам необходимо написать генератор, который будет возвращать числа по порядку.

Примеры:
Input | Output
----- | ------
[1,1],2,[1,1]] | 1 1 2 1 1
[[1,[1, 3]],2,[1,4, [6]]]] | 1 1 3 2 1 4 6

**Решение:** [здесь](./main33.py)
