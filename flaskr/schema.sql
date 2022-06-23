DROP TABLE IF EXISTS tracks;

CREATE TABLE tracks
(
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    title   TEXT UNIQUE NOT NULL,
    artist  TEXT UNIQUE NOT NULL,
    genre   TEXT        NOT NULL,
    seconds INTEGER     NOT NULL
);

