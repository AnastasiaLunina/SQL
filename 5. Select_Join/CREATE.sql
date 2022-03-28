CREATE TABLE IF NOT EXISTS Singers (
	id_singer SERIAL PRIMARY KEY NOT NULL,
	nickname VARCHAR(40) UNIQUE NOT NULL,
);

CREATE TABLE IF NOT EXISTS Albums (
	id_album SERIAL PRIMARY KEY NOT NULL,
	name_album VARCHAR(100) NOT NULL,
	year_album INTEGER NOT NULL,
);

CREATE TABLE IF NOT EXISTS Tracks (
	id_tracks SERIAL PRIMARY KEY NOT NULL,
	name_tracks VARCHAR(100) NOT NULL,
	duration_tracks NUMERIC(3,2) NOT NULL,
	id_album INTEGER REFERENCES Albums(id_album) NOT NULL
);

CREATE TABLE IF NOT EXISTS Genre (
	id_genre SERIAL PRIMARY KEY NOT NULL,
	name_genre VARCHAR(40) NOT NULL,
);

CREATE TABLE IF NOT EXISTS Collection (
	id_collection SERIAL PRIMARY KEY NOT NULL,
	name_collection VARCHAR(100) NOT NULL,
	year_collection INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS Singers_Genre (
	id_singer INTEGER NOT NULL REFERENCES Singers(id_singer),
	id_genre INTEGER NOT NULL REFERENCES Genre(id_genre),
	PRIMARY KEY (id_singer, id_genre)	
);

CREATE TABLE IF NOT EXISTS Singers_Albums (
	id_album INTEGER NOT NULL REFERENCES Albums(id_album),
	id_singer INTEGER NOT NULL REFERENCES Singers(id_singer),
	PRIMARY KEY (id_album, id_singer)
);

CREATE TABLE Collection_tracks (
	id_collection INTEGER NOT NULL REFERENCES Collection(id_collection),
	id_tracks INTEGER NOT NULL REFERENCES Tracks(id_tracks),
	PRIMARY KEY (id_collection, id_tracks)
);