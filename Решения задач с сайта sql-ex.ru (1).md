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
3. Find the model number, RAM and screen size of the laptops with prices over $1000.
```sh
SELECT model, ram, screen
FROM laptop
WHERE price > 1000
```
4. Find all records from the Printer table containing data about color printers.
```sh
SELECT *
FROM printer
WHERE color = 'y'
```
5. Find the model number, speed and hard drive capacity of PCs cheaper than $600 having a 12x or a 24x CD drive.
```sh
SELECT model, speed, hd
FROM pc
WHERE cd IN ('12x', '24x')
AND price < 600
```
6. For each maker producing laptops with a hard drive capacity of 10 Gb or higher, find the speed of such laptops. Result set: maker, speed.
```sh
SELECT DISTINCT maker, speed
FROM product p
INNER JOIN laptop l
ON p.model = l.model
WHERE hd >= 10
AND type = 'Laptop'
```
7. Get the models and prices for all commercially available products (of any type) produced by maker B.
```sh
SELECT p.model, pc.price
FROM pc
INNER JOIN product p
ON pc.model = p.model
WHERE maker = 'B'
UNION
SELECT p.model, l.price
FROM Laptop l
INNER JOIN product p
ON l.model = p.model
WHERE maker = 'B'
UNION
SELECT p.model, pr.price
FROM Printer pr
INNER JOIN product p
ON pr.model = p.model
WHERE maker = 'B'
```
8. Find the makers producing PCs but not laptops.
```sh
SELECT DISTINCT maker 
FROM product
WHERE type = 'PC'
EXCEPT
SELECT DISTINCT maker 
FROM product
WHERE type = 'Laptop'
```
9. Find the makers of PCs with a processor speed of 450 MHz or more. Result set: maker.
```sh
SELECT DISTINCT maker
FROM product p
INNER JOIN pc
ON p.model = pc.model
WHERE speed >= 450
```
10. Find the printer models having the highest price. Result set: model, price.
```sh
SELECT model, price
FROM printer
WHERE price = (SELECT MAX(price) FROM printer)
```
11. Find out the average speed of PCs.
```sh
SELECT AVG(speed)
FROM pc
```
12. Find out the average speed of the laptops priced over $1000.
```sh
SELECT AVG(speed)
FROM laptop
WHERE price > 1000
```
13. Find out the average speed of the PCs produced by maker A.
```sh
SELECT AVG(speed)
FROM pc
INNER JOIN product p
ON pc.model = p.model
WHERE maker = 'A'
```
14. For the ships in the Ships table that have at least 10 guns, get the class, name, and country.
```sh
SELECT s.class
, name
, country
FROM ships s
INNER JOIN classes c
ON s.class = c.class
WHERE numguns >= 10
```
15. Get hard drive capacities that are identical for two or more PCs. Result set: hd.
```sh
SELECT hd
FROM pc
GROUP BY hd
HAVING COUNT(hd) >=2
```
16. Get pairs of PC models with identical speeds and the same RAM capacity. Each resulting pair should be displayed only once, i.e. (i, j) but not (j, i). Result set: model with the bigger number, model with the smaller number, speed, and RAM.
```sh
SELECT DISTINCT pc1.model
, pc2.model
, pc1.speed
, pc1.ram
FROM pc pc1 INNER JOIN pc pc2
ON pc1.speed = pc2.speed
AND pc1.ram = pc2.ram
AND pc1.model > pc2.model
```
17. Get the laptop models that have a speed smaller than the speed of any PC. Result set: type, model, speed.
```sh
SELECT DISTINCT type
, l.model
, speed
FROM laptop l
INNER JOIN product p
ON l.model = p.model
WHERE speed < (SELECT MIN(speed) FROM pc)
```
18. Find the makers of the cheapest color printers. Result set: maker, price.
```sh
SELECT DISTINCT maker, price
FROM product p
INNER JOIN
(SELECT model, price
FROM printer
WHERE color = 'y' AND price = 
(SELECT MIN(price)
FROM printer
WHERE color = 'y')) AS t
ON p.model = t.model
```
19. For each maker having models in the Laptop table, find out the average screen size of the laptops he produces. Result set: maker, average screen size.
```sh
SELECT maker, AVG(screen)
FROM laptop l
INNER JOIN product p
ON l.model = p.model
GROUP BY maker
```
20. Find the makers producing at least three distinct models of PCs. Result set: maker, number of PC models.
```sh
SELECT maker, COUNT(*) models_num
FROM product
WHERE type = 'pc'
GROUP BY maker
HAVING COUNT(*) > 2
```
Exercise 21:

Find out the maximum PC price for each maker having models in the PC table. Result set: maker, maximum price.

SELECT maker, MAX(price)
FROM product p
INNER JOIN pc
ON p.model = pc.model
GROUP BY maker

Exercise 22:

For each value of PC speed that exceeds 600 MHz, find out the average price of PCs with identical speeds. Result set: speed, average price.

SELECT speed, AVG(price)
FROM pc
WHERE speed > 600
GROUP BY speed

Exercise 23:

Get the makers producing both PCs having a speed of 750 MHz or higher and laptops with a speed of 750 MHz or higher. Result set: maker

SELECT DISTINCT maker
FROM product p
WHERE maker IN 
(SELECT maker
FROM product p
INNER JOIN pc
ON p.model = pc.model
AND pc.speed >= 750)
AND maker in
(SELECT maker
FROM product p
INNER JOIN laptop l
ON p.model = l.model
AND l.speed >= 750)

Exercise 24:

List the models of any type having the highest price of all products present in the database.

WITH temp AS 
(
SELECT model, price
FROM pc
WHERE price = (SELECT MAX(price) FROM pc)
UNION
SELECT model, price
FROM laptop
WHERE price = (SELECT MAX(price) FROM laptop)
UNION
SELECT model, price
FROM printer
WHERE price = (SELECT MAX(price) FROM printer)
)
SELECT model
FROM temp
WHERE price = (SELECT MAX(price) FROM temp)

Exercise 25:

Find the printer makers also producing PCs with the lowest RAM capacity and the highest processor speed of all PCs having the lowest RAM capacity. Result set: maker.

WITH min_ram AS
(SELECT min(ram) ram FROM pc)
, max_speed AS
(SELECT max(speed) speed FROM pc
WHERE ram = (SELECT ram FROM min_ram))
, maker AS
(SELECT maker
FROM pc
INNER JOIN product p
ON ram = (SELECT ram FROM min_ram)
AND speed = (SELECT speed FROM max_speed)
AND pc.model = p.model)
SELECT DISTINCT m.maker
FROM product p
INNER JOIN maker m
ON m.maker = p.maker
AND type = 'printer'

Exercise 26:

Find out the average price of PCs and laptops produced by maker A. Result set: one overall average price for all items.

WITH temp AS
(SELECT maker, p.model, price
FROM product p
INNER JOIN pc
ON pc.model = p.model
AND p.maker = 'A'
AND p.type = 'PC'
UNION ALL
SELECT maker, p.model, price
FROM product p
INNER JOIN laptop l
ON l.model = p.model
AND p.maker = 'A'
AND p.type = 'Laptop')
SELECT AVG(price)
FROM temp

Exercise 27:

Find out the average hard disk drive capacity of PCs produced by makers who also manufacture printers. Result set: maker, average HDD capacity.

SELECT p.maker, AVG(hd)
FROM pc
INNER JOIN product p
ON p.model = pc.model
AND p.maker IN 
(
SELECT distinct maker
FROM product
WHERE type = 'Printer'
)
GROUP BY p.maker

Exercise 28:

Using Product table, find out the number of makers who produce only one model.

SELECT COUNT(maker)
FROM 
(SELECT maker
FROM product
GROUP BY maker
HAVING COUNT(model) = 1) AS a

Exercise 29:

Under the assumption that receipts of money (inc) and payouts (out) are registered not more than once a day for each collection point [i.e. the primary key consists of (point, date)], write a query displaying cash flow data (point, date, income, expense). Use Income_o and Outcome_o tables.

SELECT CASE WHEN i.point IS NULL THEN o.point
WHEN o.point IS NULL THEN i.point
ELSE i.point END AS point
, CASE WHEN i.date IS NULL THEN o.date
WHEN o.date IS NULL THEN i.date
ELSE i.date END AS date
, SUM(inc) AS inc
, SUM(out) AS out
FROM outcome_o o
FULL JOIN income_o i
ON o.point = i.point
AND o.date = i.date
GROUP BY CASE WHEN i.point IS NULL THEN o.point
WHEN o.point IS NULL THEN i.point
ELSE i.point END
, CASE WHEN i.date IS NULL THEN o.date
WHEN o.date IS NULL THEN i.date
ELSE i.date END

Exercise 30:

Under the assumption that receipts of money (inc) and payouts (out) can be registered any number of times a day for each collection point [i.e. the code column is the primary key], display a table with one corresponding row for each operating date of each collection point. Result set: point, date, total payout per day (out), total money intake per day (inc). Missing values are considered to be NULL.

WITH inc_gr AS
(SELECT point, date, SUM(inc) inc
FROM income
GROUP BY point, date)
, out_gr as
(SELECT point, date, SUM(out) out
FROM outcome
GROUP BY point, date)
SELECT i.point, i.date, out, inc
FROM inc_gr i LEFT JOIN out_gr o
ON i.point = o.point AND i.date = o.date
UNION
SELECT o.point, o.date, out, inc
FROM inc_gr i RIGHT JOIN out_gr o
ON i.point = o.point AND i.date = o.date

Exercise 31:

For ship classes with a gun caliber of 16 in. or more, display the class and the country.

SELECT class, country
FROM classes
WHERE bore >= 16

vExercise 32:

One of the characteristics of a ship is one-half the cube of the calibre of its main guns (mw). Determine the average ship mw with an accuracy of two decimal places for each country having ships in the database.

SELECT country, CAST(AVG(POWER(bore, 3)/2) AS NUMERIC(10, 2)) 
FROM
(SELECT country, bore, name 
FROM classes c
INNER JOIN ships s
ON s.class = c.class
UNION
SELECT country, bore, ship 
FROM classes c
INNER JOIN outcomes o
ON o.ship = c.class 
AND o.ship NOT IN(SELECT DISTINCT name FROM ships)) AS n
GROUP BY country

Exercise 33:

Get the ships sunk in the North Atlantic battle. Result set: ship.

SELECT ship
FROM outcomes
WHERE battle = 'North Atlantic'
AND result = 'sunk'

Exercise 34:

In accordance with the Washington Naval Treaty concluded in the beginning of 1922, it was prohibited to build battle ships with a displacement of more than 35 thousand tons. Get the ships violating this treaty (only consider ships for which the year of launch is known). List the names of the ships.

SELECT name 
FROM classes c
INNER JOIN ships s
ON c.class = s.class
WHERE displacement > 35000
AND launched >= 1922
AND type = 'bb'

Exercise 35:

Find models in the Product table consisting either of digits only or Latin letters (A-Z, case insensitive) only. Result set: model, type.

SELECT model, type 
FROM Product 
WHERE model NOT LIKE '%[^A-Z]%' 
OR model NOT LIKE '%[^0-9]%'

Exercise 36:

List the names of lead ships in the database (including the Outcomes table).

SELECT class
FROM classes
WHERE class IN
(SELECT name
FROM ships
UNION
SELECT ship 
FROM outcomes)

Exercise 37:

Find classes for which only one ship exists in the database (including the Outcomes table).

SELECT c.class
FROM classes c 
INNER JOIN
(SELECT name AS name, class AS class
FROM ships
UNION
SELECT ship AS name, ship AS class
FROM outcomes) u
ON u.class = c.class OR u.name = c.class
GROUP BY c.class
HAVING COUNT(*) = 1

Exercise 38:

Find countries that ever had classes of both battleships (‘bb’) and cruisers (‘bc’).

SELECT country
FROM classes
WHERE type = 'bb' OR type = 'bc'
GROUP BY country
HAVING COUNT(DISTINCT type) > 1

Exercise 39:

Find the ships that survived for future battles; that is, after being damaged in a battle, they participated in another one, which occurred later.

SELECT DISTINCT b.ship
FROM
(SELECT *
, LAG(result) OVER(PARTITION BY ship ORDER BY date) lag
FROM outcomes o
INNER JOIN battles b
ON o.battle = b.name
AND ship IN (
SELECT ship
FROM outcomes
WHERE result = 'damaged')) AS b
WHERE b.lag = 'damaged'

Exercise 40:

Get the makers who produce only one product type and more than one model. Output: maker, type.

SELECT DISTINCT maker, MAX(type)
FROM product
GROUP BY maker
HAVING COUNT(model) > 1
AND COUNT(DISTINCT type) = 1

Exercise 41:

For each maker who has models at least in one of the tables PC, Laptop, or Printer, determine the maximum price for his products. Output: maker; if there are NULL values among the prices for the products of a given maker, display NULL for this maker, otherwise, the maximum price.

WITH temp AS 
(SELECT model, price FROM PC
UNION
SELECT model, price FROM Laptop
UNION
SELECT model, price FROM Printer)
SELECT p.maker
, CASE WHEN COUNT(*) = COUNT(price) THEN MAX(price) END
FROM Product p
INNER JOIN temp
ON p.model = temp.model
GROUP BY p.maker

Exercise 42:

Find the names of ships sunk at battles, along with the names of the corresponding battles.

SELECT ship, battle
FROM outcomes
WHERE result = 'sunk'

Exercise 43:

Get the battles that occurred in years when no ships were launched into water.

SELECT name
FROM battles
WHERE YEAR(date) NOT IN 
(SELECT launched
FROM ships
WHERE launched IS NOT NULL)

Exercise 44:

Find all ship names beginning with the letter R.

SELECT ship
FROM outcomes
WHERE ship LIKE 'R%'
UNION
SELECT name
FROM ships
WHERE name LIKE 'R%'

Exercise 45:

Find all ship names consisting of three or more words (e.g., King George V). Consider the words in ship names to be separated by single spaces, and the ship names to have no leading or trailing spaces.

SELECT name
FROM ships
WHERE name LIKE '% % %'
UNION
SELECT ship
FROM outcomes
WHERE ship LIKE '% % %'