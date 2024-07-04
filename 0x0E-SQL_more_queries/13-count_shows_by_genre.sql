-- jnnunu
SELECT name AS genre, IFNULL(COUNT(genre_id), NULL) AS number_of_shows
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY COUNT(genre_id)
WHERE number_of_shows IS NOT NULL
ORDER BY number_of_shows DESC;