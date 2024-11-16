-- Script to list all records of second_table, ensuring rows have a name, ordered by score (highest first)
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
