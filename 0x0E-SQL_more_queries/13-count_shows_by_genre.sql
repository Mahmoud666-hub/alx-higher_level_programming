-- jnnunu
SELECT name AS genre, COUNT(genre_id) AS number_of_shows
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
HAVING COUNT(tv_show_genres.genre_id) IS NOT NULL
ORDER BY number_of_shows DESC;