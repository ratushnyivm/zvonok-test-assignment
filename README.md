# Тестовые задания

## Задание 1

Даны две таблицы в PostgresSQL - таблица статей и таблица комментариев к этим статьям.

Необходимо написать запрос, который выведет все статьи без комментариев (у которых нет комментариев).

## Решение задания 1

```sql
SELECT a.id, a.title, a.text
FROM article a
LEFT JOIN comment c ON a.id = c.article_id
WHERE c.id IS NULL;
```

---

## Задание 2

На входе есть такие записи выполненных часов работниками
(по дням, дни можно опустить - они не имеют значения):

```bash
Андрей 9
Василий 11
Роман 7
X Æ A-12 45
Иван Петров 3
..
Андрей 6
Роман 11
...
```

Формат - имя, пробел, число.
Если имя повторяется, то это один и тот же работник. Имя может содержать пробелы и цифры.
Необходимо написать программу на python, которая выводит статистику по каждому работнику + сумму часов, например:

```bash
Андрей: 9, 6; sum: 15
Василий: 11; sum: 11
Роман: 7, 11: sum: 18
...
```

## Решение задания 2

### Описание

Cli-утилита, которая читает информацию об отработанных часах работников из файла и выводит статистику по каждому работнику (список отработанных часов и их сумма). Информация может выводиться как в окно терминала, так и в отдельный файл.

### Зависимости

prod:

- python 3.11.2

dev:

- flake8 6.0.0
- pytest 7.4.0

### Установка

Перед установкой убедитесь, что у вас установлен [Poetry](https://python-poetry.org/)

1. Склонируйте репозиторий и перейдите в папку с проектом

```bash
git clone https://github.com/ratushnyyvm/zvonok-test-assignment.git && cd zvonok-test-assignment
```

2. Установите программу

```bash
make setup
```

### Использование

Вызов справки

```bash
$ zvonok -h
usage: zvonok [-h] [-o OUTPUT] path_input

Shows the statistics of the time worked by the employee.

positional arguments:
  path_input

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        set path for writing results to file (default: "not specified")
```

Вызов для вывода статистики на экран

```bash
$ zvonok tests/fixtures/input.txt
X Æ A-12: 45; sum: 45
Андрей: 9, 6; sum: 15
Василий: 11; sum: 11
Иван Петров: 3; sum: 3
Настя: 40; sum: 40
Роман: 7, 11; sum: 18
Слава: 40; sum: 40
```

Вызов для записи статистики в файл (создаётся новый файл, путь к которому выводится в терминал)

```bash
$ zvonok tests/fixtures/input.txt -o tests/fixtures/output.txt
/home/slava/projects/zvonok-test-assignment/tests/fixtures/output.txt
```
