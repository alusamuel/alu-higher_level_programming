-- Step 1: Create the temperatures table
CREATE TABLE IF NOT EXISTS temperatures (
    id INT AUTO_INCREMENT PRIMARY KEY,
    city VARCHAR(255) NOT NULL,
    temperature DECIMAL(5, 2) NOT NULL,
    date DATE NOT NULL
);

-- Step 2: Query to display the average temperature by city in Fahrenheit
SELECT city, AVG(temperature) * 9 / 5 + 32 AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;

