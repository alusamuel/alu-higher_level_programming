SELECT city, AVG(temperature) AS avg_temp
FROM temperatures
WHERE MONTH(date) IN (7, 8)  -- July and August
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
