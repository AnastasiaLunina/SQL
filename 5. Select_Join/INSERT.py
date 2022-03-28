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

connection.execute("""
INSERT INTO singers(id_singer, nickname)
VALUES(1, 'Adele'),
      (2, 'Metallica'),
      (3, 'Billie Eilish'),
      (4, 'Beyonce'),
      (5, 'Lady Gaga'),
      (6, 'Queen' ),
      (7, 'Backstreet boys'),
      (8, 'Eminem');
""")

connection.execute("""
INSERT INTO albums(id_album, name_album, year_album)
VALUES(1, 'Twenty five', 2019),
      (2, 'Reload', 1999),
      (3, 'Happier than ever', 2007),
      (4, 'BDay', 2017),
      (5, 'Born this way', 2018),
      (6, 'A day at the races', 1987),
      (7, 'Millennium', 2006),
      (8, 'The Marshall Mathers', 2012);
""")

connection.execute("""
INSERT INTO genre(id_genre, name_genre)
VALUES(1, 'Jazz'),
      (2, 'Rock'),
      (3, 'Pop'),
      (4, 'Hiphop'),
      (5, 'Rythm and blues'),
      (6, 'Dance');
""")

connection.execute("""
INSERT INTO tracks(id_tracks, name_tracks, duration_tracks, id_album)
VALUES(1, 'Skyfall', 3.06, 1),
      (2, 'Someone like you', 5.02, 2),
      (3, 'The Unforgiven', 5.17, 2),
      (4, 'Prince Charming', 2.45, 2),
      (5, 'No Time To Die', 4.12, 3),
      (6, 'My Strange Addiction', 3.12, 3),
      (7, 'Irreplaceable', 4.25, 4),
      (8, 'Run the World', 2.45, 4),
      (9, 'Dance in the dark', 3.55, 5),
      (10, 'Poker face', 5.03, 5),
      (11, 'Love of my life', 4.01, 6),
      (12, 'You take my breath away', 2.15, 6),
      (13, 'Everybody' , 3.05, 7),
      (14, 'Shape of My Heart', 2.55, 7),
      (15, 'Without Me', 3.11, 8),
      (16, 'Stan', 4.07, 8);
""")

connection.execute("""
INSERT INTO collection(id_collection, name_collection, year_collection)
VALUES(1, 'Pop music collection', 2019),
      (2, 'Rock music collection', 2006),
      (3, 'Back to ninties collection', 2000),
      (4, 'Dance collection', 2020),
      (5, 'New year collection', 2015),
      (6, 'Ladies collection', 2010),
      (7, 'Gentlemen collection', 2011),
      (8, 'Best collection', 2022);
""")

connection.execute("""
INSERT INTO singers_genre(id_singer, id_genre)
VALUES(1, 1),
      (1, 3),
      (2, 2),
      (3, 3),
      (3, 2),
      (4, 5),
      (4, 1),
      (4, 3),
      (5, 6),
      (5, 3),
      (5, 1),
      (6, 2),
      (7, 3),
      (7, 4),
      (8, 4),
      (8, 5);
""")

connection.execute("""
INSERT INTO singers_albums(id_singer, id_album)
VALUES(1, 1),
      (1, 3),
      (1, 5),
      (2, 2),
      (3, 3),
      (3, 5),
      (3, 8),
      (4, 1),
      (4, 4),
      (4, 3),
      (5, 1),
      (5, 5),
      (6, 6),
      (7, 7),
      (7, 8),
      (8, 8),
      (8, 1),
      (8, 5);
""")

connection.execute("""
INSERT INTO collection_tracks(id_collection, id_tracks)
VALUES(1, 1),
      (1, 2),
      (1, 4),
      (1, 8),
      (1, 11),
      (2, 3),
      (2, 4),
      (2, 11),
      (2, 12),
      (3, 13),
      (3, 14),
      (3, 15),
      (3, 16),
      (4, 6),
      (4, 8),
      (4, 9),
      (4, 10),
      (4, 11),
      (4, 13),
      (4, 14),
      (5, 1),
      (5, 2),
      (5, 8),
      (5, 12),
      (6, 1),
      (6, 2),
      (6, 5),
      (6, 6),
      (6, 7),
      (6, 8),
      (6, 9),
      (6, 10),
      (7, 3),
      (7, 4),
      (7, 11),
      (7, 12),
      (7, 13),
      (7, 14),
      (7, 15),
      (7, 16),
      (8, 1),
      (8, 3),
      (8, 5),
      (8, 7),
      (8, 9),
      (8, 11),
      (8, 13),
      (8, 15);
""")






