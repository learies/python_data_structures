# Односвязный список

### Реализованные методы списка
- append — добавить узел в конец список. Если список пуст, узел будет добавлен в начало списка.
- print — выводит все значения списка по порядку.

### Пример
```python
from singly_linked_list import LinkedList


def main():
    mylist = LinkedList()

    mylist.append(12)
    mylist.append(42)
    mylist.append(11)

    mylist.print()


if __name__ == '__main__':
    main()
```
```
out: 12 42 11
```