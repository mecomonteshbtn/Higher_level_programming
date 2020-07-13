-- Display contents sorted using ORDER BY 
-- DML query to display results sorted by score >= 10
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
