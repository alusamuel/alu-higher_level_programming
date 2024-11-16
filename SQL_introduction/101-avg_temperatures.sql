-- Display the average temperature by city ordered by temperature (in Fahrenheit) in descending order

SELECT city, AVG(temperature) * 9 / 5 + 32 AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
