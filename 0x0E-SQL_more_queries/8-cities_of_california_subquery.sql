-- List California's cities
-- DML query to get all cities in Californi (state_id = 1)
SELECT id,name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY cities.id ASC;
