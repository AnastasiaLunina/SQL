## Flowchart

![](diagram.png) 

## SQL commands

```sql
CREATE TABLE IF NOT EXISTS Singers (
	id_singer SERIAL PRIMARY KEY NOT NULL,
	nickname VARCHAR(40) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS Albums (
	id_album SERIAL PRIMARY KEY NOT NULL,
	name_album VARCHAR(100) NOT NULL,
	year_album VARCHAR(4) NOT NULL,
	id_singer INTEGER REFERENCES Singers(id_singer) NOT NULL
);

CREATE TABLE IF NOT EXISTS Tracks (
	id_tracks SERIAL PRIMARY KEY NOT NULL,
	name_tracks VARCHAR(100) NOT NULL,
	duration_tracks VARCHAR(10) NOT NULL,
	id_album INTEGER REFERENCES Albums(id_album) NOT NULL
);

CREATE TABLE IF NOT EXISTS Genre (
	id_genre SERIAL PRIMARY KEY NOT NULL,
	name_genre VARCHAR(40) NOT NULL,
	id_singer INTEGER REFERENCES Singers(id_singer) NOT NULL
);

ALTER TABLE Singers 
ADD id_genre INTEGER REFERENCES Genre(id_genre) NOT NULL;

ALTER TABLE Genre 
DROP COLUMN IF EXISTS id_singer;

ALTER TABLE Albums 
ALTER COLUMN year_album TYPE INTEGER USING year_album::integer;

ALTER TABLE Tracks 
ALTER COLUMN duration_tracks TYPE INTEGER USING duration_tracks::integer;
```