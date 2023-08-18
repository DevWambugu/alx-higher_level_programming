-- lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
-- You can use a maximum of two SELECT statement
SELECT title
FROM tv_shows
WHERE id NOT IN (
	    SELECT DISTINCT ts.id
	    FROM tv_shows AS ts
	    JOIN tv_show_genres AS tsg ON ts.id = tsg.show_id
	    JOIN tv_genres AS tg ON tsg.genre_id = tg.id
	    WHERE tg.name = 'Comedy'
)
ORDER BY title ASC;

