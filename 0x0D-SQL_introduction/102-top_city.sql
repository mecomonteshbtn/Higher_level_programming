-- Display highest temperatures
-- DML query to list top 3 sorted temperatures during July and Agust
SELECT city,AVG(value) AS avg_temp
FROM temperatures
WHERE month=7 OR month=8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
