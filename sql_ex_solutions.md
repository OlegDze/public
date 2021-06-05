# Решения задач с сайта sql-ex.ru

Все задачи и описание таблиц с данными взяты с сайта https://www.sql-ex.ru/ от 6 июня 2021 года. На этот момент времени на сайте 155 задач, для которых представлены решения.

## Структуры таблиц с данными

All exercises are performed on the databases described below.

### 1. Computer firm
The database scheme consists of four tables:
- Product(maker, model, type)
- PC(code, model, speed, ram, hd, cd, price)
- Laptop(code, model, speed, ram, hd, screen, price)
- Printer(code, model, color, type, price)

The Product table contains data on the maker, model number, and type of product ('PC', 'Laptop', or 'Printer'). It is assumed that model numbers in the Product table are unique for all makers and product types. Each personal computer in the PC table is unambiguously identified by a unique code, and is additionally characterized by its model (foreign key referring to the Product table), processor speed (in MHz) – speed field, RAM capacity (in Mb) - ram, hard disk drive capacity (in Gb) – hd, CD-ROM speed (e.g, '4x') - cd, and its price. The Laptop table is similar to the PC table, except that instead of the CD-ROM speed, it contains the screen size (in inches) – screen. For each printer model in the Printer table, its output type (‘y’ for color and ‘n’ for monochrome) – color field, printing technology ('Laser', 'Jet', or 'Matrix') – type, and price are specified.
![](https://www.sql-ex.ru/images/computers.gif)

### 2. Recycling firm
The firm owns several buy-back centers for collection of recyclable materials. Each of them receives funds to be paid to the recyclables suppliers. Data on funds received is recorded in the table Income_o(point, date, inc). The primary key is (point, date), where point holds the identifier of the buy-back center, and date corresponds to the calendar date the funds were received. The date column doesn’t include the time part, thus, money (inc) arrives no more than once a day for each center. 

Information on payments to the recyclables suppliers is held in the table Outcome_o(point, date, out). In this table, the primary key (point, date) ensures each buy-back center reports about payments (out) no more than once a day, too.

For the case income and expenditure may occur more than once a day, another database schema with tables having a primary key consisting of the single column code is used:
- Income(code, point, date, inc);
- Outcome(code, point, date, out).
Here, the date column doesn’t include the time part, either.
![](https://www.sql-ex.ru/images/income.gif)

### 3. Ships
The database of naval ships that took part in World War II is under consideration. The database consists of the following relations:
- Classes(class, type, country, numGuns, bore, displacement)
- Ships(name, class, launched)
- Battles(name, date)
- Outcomes(ship, battle, result)

Ships in classes all have the same general design. A class is normally assigned either the name of the first ship built according to the corresponding design, or a name that is different from any ship name in the database. The ship whose name is assigned to a class is called a lead ship.
The Classes relation includes the name of the class, type (can be either bb for a battle ship, or bc for a battle cruiser), country the ship was built in, the number of main guns, gun caliber (bore diameter in inches), and displacement (weight in tons). The Ships relation holds information about the ship name, the name of its corresponding class, and the year the ship was launched. The Battles relation contains names and dates of battles the ships participated in, and the Outcomes relation - the battle result for a given ship (may be sunk, damaged, or OK, the last value meaning the ship survived the battle unharmed).

Notes: 
1) The Outcomes relation may contain ships not present in the Ships relation. 
2) A ship sunk can’t participate in later battles. 
3) For historical reasons, lead ships are referred to as head ships in many exercises.
4) A ship found in the Outcomes table but not in the Ships table is still considered in the database. This is true even if it is sunk.
![](https://www.sql-ex.ru/images/income.gif)

### 4. Airport
The database schema consists of 4 tables:
- Company(ID_comp, name)
- Trip(trip_no, id_comp, plane, town_from, town_to, time_out, time_in)
- Passenger(ID_psg, name)
- Pass_in_trip(trip_no, date, ID_psg, place)

The Company table contains IDs and names of the airlines transporting passengers. The Trip table contains information on the schedule of flights: trip (flight) number, company (airline) ID, plane type, departure city, destination city, departure time, and arrival time. The Passenger table holds IDs and names of the passengers. The Pass_in_trip table contains data on flight bookings: trip number, departure date (day), passenger ID and her seat (place) designation during the flight. It should be noted that:
- scheduled flights are operated daily; the duration of any flight is less than 24 hours; town_from <> town_to;
- all time and date values are assumed to belong to the same time zone;
- departure and arrival times are specified with one minute precision;
- there can be several passengers bearing the same first name and surname (for example, Bruce Willis);
- the seat (place) designation consists of a number followed by a letter; the number stands for the row, while the letter (a – d) defines the seat position in the grid (from left to right, in alphabetical order;
- connections and constraints are shown in the database schema below.
![](https://www.sql-ex.ru/images/aero.gif)

### 5. Painting
The database schema consists of 3 tables:
- utQ (Q_ID int, Q_NAME varchar(35)), 
- utV (V_ID int, V_NAME varchar(35), V_COLOR char(1)), 
- utB (B_DATETIME datetime, B_Q_ID int, B_V_ID int, B_VOL tinyint).

The utQ table contains the identifiers and names of squares, the initial color of which is black. (Note: black is not a color and is considered unpainted. Only Red, Green and Blue are colors.)
The utV table contains the identifiers and names of spray cans and the color of paint they are filled with.
The utB table holds information on squares being spray-painted, and contains the time of the painting event, the square and spray can identifiers, the quantity of paint being applied.

It should be noted that:
- a spray can may contain paint of one of three colors: red (V_COLOR='R'), green (V_COLOR='G'), or blue (V_COLOR='B');
- any spray can initially contains 255 units of paint;
- the square color is defined in accordance with the RGB model, i.e. R=0, G=0, B=0 is black, whereas R=255, G=255, B=255 is white;
- any record in the utB table decreases the paint quantity in the corresponding spray can by B_VOL and accordingly increases the amount of paint applied to the square by the same value;
- B_VOL must be greater than 0 and less or equal to 255;
- the paint quantity of a single color applied to one square can’t exceed 255, and there can’t be a less than zero amount of paint in a spray can;
- the time of the painting event (B_DATETIME) is specified with one second precision, i.e. it does not contain milliseconds;
- for historical reasons, the spray cans are referred to as “balloons” by many of the exercises, and the utV table contains spray can names (V_NAME column) such as “Balloon # 01”, etc.
![](https://www.sql-ex.ru/images/painting.gif)

## Задачи

1. Find the model number, speed and hard drive capacity for all the PCs with prices below $500. Result set: model, speed, hd.
SELECT model, speed, hd
FROM pc
WHERE price < 500
2. List all printer makers. Result set: maker.
SELECT DISTINCT maker
FROM product
WHERE type = 'Printer'
3. Find the model number, RAM and screen size of the laptops with prices over $1000.
SELECT model, ram, screen
FROM laptop
WHERE price > 1000
4. Find all records from the Printer table containing data about color printers.
SELECT *
FROM printer
WHERE color = 'y'
5. Find the model number, speed and hard drive capacity of PCs cheaper than $600 having a 12x or a 24x CD drive.
SELECT model, speed, hd
FROM pc
WHERE cd IN ('12x', '24x')
AND price < 600
6. For each maker producing laptops with a hard drive capacity of 10 Gb or higher, find the speed of such laptops. Result set: maker, speed.
SELECT DISTINCT maker, speed
FROM product p
INNER JOIN laptop l
ON p.model = l.model
WHERE hd >= 10
AND type = 'Laptop'
7. Get the models and prices for all commercially available products (of any type) produced by maker B.
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
8. Find the makers producing PCs but not laptops.
SELECT DISTINCT maker 
FROM product
WHERE type = 'PC'
EXCEPT
SELECT DISTINCT maker 
FROM product
WHERE type = 'Laptop'
9. Find the makers of PCs with a processor speed of 450 MHz or more. Result set: maker.
SELECT DISTINCT maker
FROM product p
INNER JOIN pc
ON p.model = pc.model
WHERE speed >= 450
10. Find the printer models having the highest price. Result set: model, price.
SELECT model, price
FROM printer
WHERE price = (SELECT MAX(price) FROM printer)
11. Find out the average speed of PCs.
SELECT AVG(speed)
FROM pc
12. Find out the average speed of the laptops priced over $1000.
SELECT AVG(speed)
FROM laptop
WHERE price > 1000
13. Find out the average speed of the PCs produced by maker A.
SELECT AVG(speed)
FROM pc
INNER JOIN product p
ON pc.model = p.model
WHERE maker = 'A'
14. For the ships in the Ships table that have at least 10 guns, get the class, name, and country.
SELECT s.class
, name
, country
FROM ships s
INNER JOIN classes c
ON s.class = c.class
WHERE numguns >= 10

```python

```


```python

```


```python

```


```python

```
