# Решения задач с сайта sql-ex.ru
Схемы таблиц с данными доступны по [ссылке](https://www.sql-ex.ru/help/select13.php).
Задачи и решения:
1. Find the model number, speed and hard drive capacity for all the PCs with prices below $500. Result set: model, speed, hd.
```sh
SELECT model, speed, hd
FROM pc
WHERE price < 500
```
2. List all printer makers. Result set: maker.
```sh
SELECT DISTINCT maker
FROM product
WHERE type = 'Printer'
```
##### Exercise 3:
Find the model number, RAM and screen size of the laptops with prices over $1000.
```sh
SELECT model, ram, screen
FROM laptop
WHERE price > 1000
```
###### Exercise 4:
Find all records from the Printer table containing data about color printers.
```sh
SELECT *
FROM printer
WHERE color = 'y'
```