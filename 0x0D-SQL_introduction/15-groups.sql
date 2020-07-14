-- Display same score using COUNT, ORDER BY, GROUP BY
-- DML query to display number of records with same score
SELECT score,COUNT(*) AS 'number' FROM second_table
GROUP BY score
ORDER BY score DESC;
