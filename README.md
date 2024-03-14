
```
🛠️ Проект предназначен для развертывания в GitLab. Выложен здесь в качестве портфолио.
```

> *Дисциплина:* Модели развертывания удаленных сервисов
> *Курс:* 4 курс 7 семестр

# Задание
Организовать проект с системой контроля версий и систему сборки на основе CI/CD. Система CI/CD должна собирать приложение запускать его передавая аргумент, который может динамически указать пользователь. Результат работы приложения должен быть возвращен из CI/CD в виде артефакта.

# Требования к репозиторию
1.	Создать публичный репозиторий на Gitlab
2.	Оформить структуру проекта на любом языке программирования и сделать первоначальную фиксацию пустого проекта
3.	Оформить ветки «master» и «dev»
4.	Зафиксировать в ветке «dev» промежуточные этапы разработки
5.	В ветку «master» зафиксировать версию 1.0. полностью готовое решение задачи
6.	Создать документацию:
    * В корне проекта: файл README.md с кратким описанием и интерфейсом программы в разметке markdown.
    * В корне проекта: файл DOC.md с описанием задачи в разметке markdown

# Функциональные требования:
1.	Решить задачи на любом языке программирования.
2.	Решения всех задач должны собираться, запускаться или разворачиваться системой CI/CD.
3.	Требуется ввод данных, организовать данный ввод динамически средствами CI/CD (env переменные), а не «жестко закодировать» в приложении.



### Вариант - 10

Создать приложение, которое принимает переменную char, если она оказывается цифрой, то возвращает ее значение типа integer.
