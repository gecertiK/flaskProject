CREATE TABLE IF NOT EXISTS tracks (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT UNIQUE NOT NULL,
  artist TEXT UNIQUE NOT NULL,
  genre TEXT NOT NULL,
  seconds INTEGER NOT NULL
);

