import sqlalchemy
import psycopg2
from credentials import postgresql as credentials
from pprint import pprint


def get_engine(user, password, host, port, db):
    url = f"postgresql://{user}:{password}@{host}:{port}/{db}"
    engine = sqlalchemy.create_engine(url)
    return engine


engine = get_engine(credentials["pguser"],
                    credentials["pgpassword"],
                    credentials["pghost"],
                    credentials["pgport"],
                    credentials["pgdb"])

connection = engine.connect()


# 1. Number of singers in each genre
select_singers = connection.execute("""
    SELECT G.name_genre, COUNT(SG.id_singer)
    FROM genre G
    JOIN singers_genre SG on G.id_genre = SG.id_genre
    GROUP BY G.name_genre;
""").fetchall()
pprint(f"#1 Number of singers in each genre: {select_singers}")

# 2. Number of tracks in albums dated 2019-2020
select_tracks = connection.execute("""
    SELECT A.year_album, COUNT(T.id_tracks)
    FROM albums A
    JOIN tracks T ON T.id_album = A.id_album
    WHERE A.year_album BETWEEN 2019 AND 2020
    GROUP BY A.year_album;
""").fetchall()
print()
pprint(f"#2 Number of tracks in albums dated 2019-2020: {select_tracks}")

# 3. Average track duration on each album
select_track_duration = connection.execute("""
    SELECT A.name_album, ROUND(AVG(T.duration_tracks),2)
    FROM albums A
    JOIN tracks T ON T.id_album = A.id_album
    group BY A.name_album;
""").fetchall()
print()
pprint(f"#3 Average track duration on each album: {select_track_duration}")

# 4. All singers who did not release albums in 2020
select_release = connection.execute("""
    SELECT DISTINCT s.nickname FROM singers s
    WHERE s.nickname NOT IN (
        SELECT DISTINCT s.nickname FROM singers s
        LEFT JOIN singers_albums sa ON s.id_singer = sa.id_singer
        LEFT JOIN albums a ON a.id_album = sa.id_album
        WHERE a.year_album = 2020
        )
    ORDER BY s.nickname;
""").fetchall()
print()
pprint(f"#4 All singers who did not release albums in 2020: {select_release}")

# 5. Name of collections where singer = "Eminem"
select_singer = connection.execute("""
    SELECT DISTINCT C.name_collection
    FROM collection C
    JOIN collection_tracks CT ON C.id_collection = CT.id_collection
    JOIN tracks T ON T.id_tracks = CT.id_tracks
    JOIN albums A ON T.id_album = A.id_album
    JOIN singers_albums SA ON SA.id_album = A.id_album
    JOIN singers S ON SA.id_singer = S.id_singer
    WHERE S.nickname = 'Eminem';
""").fetchall()
print()
pprint(f"#5 Name of collections where singer = 'Eminem': {select_singer}")

# 6. Name of albums where the singers of more the one genre present.
select_singer_genre = connection.execute("""
    SELECT A.name_album, COUNT(SG.id_genre)
    FROM albums A
    JOIN singers_albums SA ON SA.id_album = A.id_album
    JOIN singers S ON SA.id_singer = S.id_singer
    JOIN singers_genre SG ON S.id_singer = SG.id_singer
    JOIN genre G ON SG.id_genre = G.id_genre
    GROUP BY A.name_album
    HAVING COUNT(SG.id_genre) > 1;
""").fetchall()
print()
pprint(f"#6 Name of albums where the singers of more the one genre present: {select_singer_genre}")

# 7. Name of tracks which are not included in any collection.
select_not_included = connection.execute("""
    SELECT T.name_tracks, C.name_collection
    FROM tracks T
    JOIN collection_tracks CT ON CT.id_tracks = T.id_tracks 
    JOIN collection C ON CT.id_collection = C.id_collection
    WHERE CT.id_tracks IS NULL;
""").fetchall()
print()
pprint(f"#7 Name of tracks which are not included in any collection: {select_not_included}")

# 8. Singer with the shortest track.
select_shortest = connection.execute("""
    SELECT S.nickname, T.duration_tracks
    FROM singers S
    JOIN singers_albums SA ON S.id_singer = SA.id_singer 
    JOIN albums A ON SA.id_album = A.id_album
    JOIN tracks T ON A.id_album = T.id_album
    WHERE T.duration_tracks 
    IN (SELECT MIN(duration_tracks) FROM tracks);
""").fetchall()
print()
pprint(f"#8 Singer with the shortest track: {select_shortest}")

# 9. Name of album(s) with the least amount of tracks.
select_least_songs = connection.execute("""
    SELECT DISTINCT A.name_album
    FROM albums AS A
    LEFT JOIN tracks as T ON T.id_album = A.id_album
    WHERE T.id_album IN
        (
        SELECT T.id_album 
        FROM tracks T
        GROUP BY T.id_album 
        HAVING COUNT(T.id_tracks) = 
            (
            SELECT COUNT(T.id_tracks)
            FROM tracks T
            GROUP BY T.id_album 
            ORDER BY COUNT
            LIMIT 1
            )
    )
    ORDER BY A.name_album;
""").fetchall()
print()
pprint(f"#9 Name of album(s) with the least amount of songs: {select_least_songs}")
