-- lists all cities contained in the database hbtn_0d_usa.
-- Each record should display: cities.id - cities.name - states.name
-- Results must be sorted in ascending order by cities.id
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT c.id, c.name, s.name
FROM hbtn_0d_usa.cities AS c
JOIN hbtn_0d_usa.states AS s ON c.state_id = s.id
ORDER BY c.id ASC;