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
21. Find out the maximum PC price for each maker having models in the PC table. Result set: maker, maximum price.
```sh
SELECT maker, MAX(price)
FROM product p
INNER JOIN pc
ON p.model = pc.model
GROUP BY maker
```
22. For each value of PC speed that exceeds 600 MHz, find out the average price of PCs with identical speeds. Result set: speed, average price.
```sh
SELECT speed, AVG(price)
FROM pc
WHERE speed > 600
GROUP BY speed
```
23. Get the makers producing both PCs having a speed of 750 MHz or higher and laptops with a speed of 750 MHz or higher. Result set: maker
```sh
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
```
24. List the models of any type having the highest price of all products present in the database.
```sh
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
```
25. Find the printer makers also producing PCs with the lowest RAM capacity and the highest processor speed of all PCs having the lowest RAM capacity. Result set: maker.
```sh
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
```
26. Find out the average price of PCs and laptops produced by maker A. Result set: one overall average price for all items.
```sh
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
```
27. Find out the average hard disk drive capacity of PCs produced by makers who also manufacture printers. Result set: maker, average HDD capacity.
```sh
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
```
28. Using Product table, find out the number of makers who produce only one model.
```sh
SELECT COUNT(maker)
FROM 
(SELECT maker
FROM product
GROUP BY maker
HAVING COUNT(model) = 1) AS a
```
29. Under the assumption that receipts of money (inc) and payouts (out) are registered not more than once a day for each collection point [i.e. the primary key consists of (point, date)], write a query displaying cash flow data (point, date, income, expense). Use Income_o and Outcome_o tables.
```sh
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
```
30. Under the assumption that receipts of money (inc) and payouts (out) can be registered any number of times a day for each collection point [i.e. the code column is the primary key], display a table with one corresponding row for each operating date of each collection point. Result set: point, date, total payout per day (out), total money intake per day (inc). Missing values are considered to be NULL.
```sh
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
```
31. For ship classes with a gun caliber of 16 in. or more, display the class and the country.
```sh
SELECT class, country
FROM classes
WHERE bore >= 16
```
32. One of the characteristics of a ship is one-half the cube of the calibre of its main guns (mw). Determine the average ship mw with an accuracy of two decimal places for each country having ships in the database.
```sh
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
```
33. Get the ships sunk in the North Atlantic battle. Result set: ship.
```sh
SELECT ship
FROM outcomes
WHERE battle = 'North Atlantic'
AND result = 'sunk'
```
34. In accordance with the Washington Naval Treaty concluded in the beginning of 1922, it was prohibited to build battle ships with a displacement of more than 35 thousand tons. Get the ships violating this treaty (only consider ships for which the year of launch is known). List the names of the ships.
```sh
SELECT name 
FROM classes c
INNER JOIN ships s
ON c.class = s.class
WHERE displacement > 35000
AND launched >= 1922
AND type = 'bb'
```
35. Find models in the Product table consisting either of digits only or Latin letters (A-Z, case insensitive) only. Result set: model, type.
```sh
SELECT model, type 
FROM Product 
WHERE model NOT LIKE '%[^A-Z]%' 
OR model NOT LIKE '%[^0-9]%'
```
36. List the names of lead ships in the database (including the Outcomes table).
```sh
SELECT class
FROM classes
WHERE class IN
(SELECT name
FROM ships
UNION
SELECT ship 
FROM outcomes)
```
37. Find classes for which only one ship exists in the database (including the Outcomes table).
```sh
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
```
38. Find countries that ever had classes of both battleships (‘bb’) and cruisers (‘bc’).
```sh
SELECT country
FROM classes
WHERE type = 'bb' OR type = 'bc'
GROUP BY country
HAVING COUNT(DISTINCT type) > 1
```
39. Find the ships that survived for future battles; that is, after being damaged in a battle, they participated in another one, which occurred later.
```sh
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
```
40. Get the makers who produce only one product type and more than one model. Output: maker, type.
```sh
SELECT DISTINCT maker, MAX(type)
FROM product
GROUP BY maker
HAVING COUNT(model) > 1
AND COUNT(DISTINCT type) = 1
```
41. For each maker who has models at least in one of the tables PC, Laptop, or Printer, determine the maximum price for his products. Output: maker; if there are NULL values among the prices for the products of a given maker, display NULL for this maker, otherwise, the maximum price.
```sh
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
```
42. Find the names of ships sunk at battles, along with the names of the corresponding battles.
```sh
SELECT ship, battle
FROM outcomes
WHERE result = 'sunk'
```
43. Get the battles that occurred in years when no ships were launched into water.
```sh
SELECT name
FROM battles
WHERE YEAR(date) NOT IN 
(SELECT launched
FROM ships
WHERE launched IS NOT NULL)
```
44. Find all ship names beginning with the letter R.
```sh
SELECT ship
FROM outcomes
WHERE ship LIKE 'R%'
UNION
SELECT name
FROM ships
WHERE name LIKE 'R%'
```
45. Find all ship names consisting of three or more words (e.g., King George V). Consider the words in ship names to be separated by single spaces, and the ship names to have no leading or trailing spaces.
```sh
SELECT name
FROM ships
WHERE name LIKE '% % %'
UNION
SELECT ship
FROM outcomes
WHERE ship LIKE '% % %'
```
46. For each ship that participated in the Battle of Guadalcanal, get its name, displacement, and the number of guns.
```sh
SELECT DISTINCT ship, displacement, numGuns
FROM classes c
LEFT JOIN ships s
ON c.class = s.class
RIGHT JOIN outcomes o 
ON c.class = o.ship
OR s.name = o.ship
WHERE battle = 'Guadalcanal'
```
47. Find the countries that have lost all their ships in battles.
```sh
WITH temp AS (
SELECT s.name, c.country
FROM classes c JOIN ships s
ON c.class = s.class 
UNION
SELECT o.ship name, c.country
FROM classes c JOIN outcomes o
ON o.ship = c.class
)
, temp2 AS (
SELECT country, COUNT(*) AS count
FROM temp
GROUP BY country
)
, temp3 AS (
SELECT country, COUNT(*) AS sunk_count
FROM temp JOIN outcomes o
ON o.ship = temp.name
WHERE result ='sunk'
GROUP BY country
)
SELECT temp3.country
FROM temp3 JOIN temp2
ON temp2.country = temp3.country
AND temp2.count = temp3.sunk_count
```
48. Find the ship classes having at least one ship sunk in battles.
```sh
SELECT class 
FROM Outcomes o
LEFT JOIN ships s
ON o.ship = s.name
WHERE result = 'sunk' AND class IS NOT NULL
UNION 
SELECT class 
FROM Outcomes o
LEFT JOIN classes c
ON o.ship = c.class
WHERE result = 'sunk' AND class IS NOT NULL
```
49. Find the names of the ships having a gun caliber of 16 inches (including ships in the Outcomes table).
```sh
SELECT name 
FROM ships
WHERE class IN
(SELECT class FROM classes WHERE bore = 16)
UNION
SELECT ship FROM outcomes WHERE ship IN
(SELECT class FROM classes WHERE bore = 16)
```
50. Find the battles in which Kongo-class ships from the Ships table were engaged.
```sh
SELECT DISTINCT battle
FROM ships s
INNER JOIN outcomes o
ON s.name = o.ship
WHERE s.class = 'Kongo'
```
51. Find the names of the ships with the largest number of guns among all ships having the same displacement (including ships in the Outcomes table).
```sh
WITH a AS 
(SELECT name AS ship, numGuns, displacement
FROM classes c
INNER JOIN ships s
ON s.class = c.class
UNION
SELECT ship, numGuns, displacement
FROM outcomes o
INNER JOIN classes c
ON o.ship = c.class)
SELECT ship
FROM a
INNER JOIN 
(SELECT displacement, MAX(numGuns) AS MaxNum
FROM a
GROUP BY displacement) AS b
ON a.displacement = b.displacement
AND a.numGuns = b.MaxNum
```
52. Determine the names of all ships in the Ships table that can be a Japanese battleship having at least nine main guns with a caliber of less than 19 inches and a displacement of not more than 65 000 tons.
```sh
SELECT name
FROM ships s
INNER JOIN 
classes c
ON s.class = c.class
WHERE (numGuns >= 9 OR numGuns IS NULL)
AND (bore < 19 OR bore IS NULL)
AND (displacement <= 65000 OR displacement IS NULL)
AND (country = 'Japan' OR country IS NULL)
AND (type = 'bb' OR type IS NULL)
```
53. With a precision of two decimal places, determine the average number of guns for the battleship classes.
```sh
SELECT CAST(AVG(numGuns*1.0) AS NUMERIC(4,2))
FROM classes
WHERE type = 'bb'
```
54. With a precision of two decimal places, determine the average number of guns for all battleships (including the ones in the Outcomes table).
```sh
SELECT CAST(AVG(numGuns * 1.0) AS NUMERIC(6,2)) Avg_numG
FROM
(SELECT s.name, c.numGuns
FROM classes c JOIN ships s
ON c.class = s.class
WHERE type = 'bb'
union
SELECT o.ship, c.numGuns
FROM classes c JOIN outcomes o
ON c.class = o.ship
WHERE type = 'bb') a
```
55. For each class, determine the year the first ship of this class was launched.
If the lead ship’s year of launch is not known, get the minimum year of launch for the ships of this class.
Result set: class, year.
```sh
SELECT c.class, MIN(launched)
FROM classes c
LEFT JOIN ships s
ON c.class = s.class
GROUP BY c.class
```
56. For each class, find out the number of ships of this class that were sunk in battles.
Result set: class, number of ships sunk.
```sh
WITH temp AS
(SELECT class, COUNT(*) cnt
FROM
(SELECT s.class, o.ship, result
FROM outcomes o 
JOIN ships s
ON s.name = o.ship
UNION
SELECT c.class, o.ship, result
FROM outcomes o 
JOIN classes c
ON c.class = o.ship) a
WHERE result = 'sunk'
GROUP BY class)
SELECT c.class, CASE WHEN cnt IS NULL THEN 0 ELSE cnt END sunk
FROM classes c
LEFT JOIN temp
ON c.class = temp.class
```
57. For classes having irreparable combat losses and at least three ships in the database, display the name of the class and the number of ships sunk.
```sh
WITH temp AS
(SELECT class, name 
FROM ships
UNION
SELECT ship AS class, ship AS name
FROM outcomes
WHERE ship IN (SELECT class FROM classes))
, temp2 AS
(SELECT class 
FROM temp
GROUP BY class
HAVING COUNT(name) >= 3)
SELECT temp.class, COUNT(*)
FROM temp
JOIN outcomes o
ON temp.name = o.ship
WHERE result = 'sunk' 
AND temp.class IN (SELECT class FROM temp2)
GROUP BY class
```
58. For each product type and maker in the Product table, find out, with a precision of two decimal places, the percentage ratio of the number of models of the actual type produced by the actual maker to the total number of models by this maker.
Result set: maker, product type, the percentage ratio mentioned above.
```sh
WITH temp AS (
SELECT maker, type, COUNT(DISTINCT p.model) models
FROM product p LEFT JOIN pc
ON p.model = pc.model 
WHERE p.type = 'PC'
GROUP BY maker, type
UNION
SELECT maker, type, COUNT(DISTINCT p.model) models
FROM product p left join laptop l
ON p.model = l.model 
WHERE p.type = 'Laptop'
GROUP BY maker, type
UNION
SELECT maker, p.type, COUNT(DISTINCT p.model) models
FROM product p left join printer pr
ON p.model = pr.model 
WHERE p.type = 'Printer'
GROUP BY maker, p.type
)
, temp2 AS(
SELECT maker, type
, CAST(models * 100.0 / SUM(models) OVER(PARTITION BY maker ORDER BY type ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS
NUMERIC(6,2)) AS prc
FROM temp
)
, temp3 AS(
SELECT maker, type, 0 AS prc
FROM (SELECT DISTINCT maker FROM product) m
CROSS JOIN (SELECT DISTINCT type FROM product) p)
SELECT temp3.maker, temp3.type, CASE WHEN temp2.prc IS NULL THEN temp3.prc ELSE temp2.prc END
FROM temp2 RIGHT JOIN temp3 ON temp2.maker = temp3.maker
AND temp2.type = temp3.type
```
59. Calculate the cash balance of each buy-back center for the database with money transactions being recorded not more than once a day.
Result set: point, balance.
```sh
WITH temp AS (
SELECT CASE WHEN i.point IS NULL THEN o.point ELSE i.point END AS point
, CASE WHEN i.date IS NULL THEN o.date ELSE i.date END AS date
, CASE WHEN inc IS NULL THEN 0 ELSE inc END - CASE WHEN out IS NULL THEN 0 ELSE out END AS remain
FROM income_o i
FULL JOIN outcome_o o
ON i.point = o.point
AND i.date = o.date
)
SELECT point, SUM(remain) remain
FROM temp
GROUP BY point
```
60. For the database with money transactions being recorded not more than once a day, calculate the cash balance of each buy-back center at the beginning of 4/15/2001.
Note: exclude centers not having any records before the specified date.
Result set: point, balance
```sh
WITH temp AS (
SELECT CASE WHEN i.point IS NULL THEN o.point ELSE i.point END AS point
, CASE WHEN i.date IS NULL THEN o.date ELSE i.date END AS date
, CASE WHEN inc IS NULL THEN 0 ELSE inc END - CASE WHEN out IS NULL THEN 0 ELSE out END AS remain
FROM income_o i
FULL JOIN outcome_o o
ON i.point = o.point
AND i.date = o.date)
SELECT point, SUM(remain) 
FROM temp
WHERE date < '2001-04-15'
GROUP BY point
```

