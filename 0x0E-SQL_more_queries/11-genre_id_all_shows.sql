-- nnml
SELECT tv_shows.title, COALESCE(tv_show_genres.genre_id, NULL) AS genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title, tv_show_genres.genre_id;