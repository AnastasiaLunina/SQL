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

# 1. Name and year of albums released in 2018
select_year = connection.execute("""
    SELECT name_album, year_album
    FROM albums
    WHERE year_album = 2018;
""").fetchall()
pprint(select_year)

# 2. Name and duration of the longest track
select_duration = connection.execute("""
    SELECT name_tracks, duration_tracks
    FROM tracks
    WHERE duration_tracks = (SELECT MAX(duration_tracks) FROM tracks);
""").fetchone()
pprint(select_duration)

# OR

select_duration_1 = connection.execute("""
    SELECT name_tracks, duration_tracks
    FROM tracks
    ORDER BY duration_tracks DESC
    LIMIT 1
""").fetchall()
pprint(select_duration_1)

# 3. Name of the tracks with duration not less than 3.05
select_3_05 = connection.execute("""
    SELECT name_tracks, duration_tracks
    FROM tracks
    WHERE duration_tracks >= 03.05
""").fetchall()
pprint(select_3_05)

# 4. Name f cllections released between 2018 and 2020
select_2018_2020 = connection.execute("""
    SELECT name_collection
    FROM collection
    WHERE year_collection BETWEEN 2018 AND 2020;
""").fetchall()
pprint(select_2018_2020)

# 5. Nickname of singers with one word name
select_nickname = connection.execute("""
    SELECT nickname FROM singers
    WHERE nickname NOT LIKE '%% %%';
""").fetchall()
pprint(select_nickname)

# 6. Name of the tracks with word "my"
select_track = connection.execute("""
    SELECT name_tracks FROM tracks
    WHERE name_tracks LIKE '%%my%%';
""").fetchall()
pprint(select_track)
