import sqlite3

conn = sqlite3.connect('music.sqlite') #creates a file if it doesn't exist
cur = conn.cursor() #like file handle

cur.execute('DROP TABLE IF EXISTS Tracks')
cur.execute('CREATE TABLE Tracks(title TEXT, plays INTEGER)')

cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', ('Thunderstruck', '20')) #values passed as tuples
cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', ('My Way', '15'))
conn.commit()

print('Tracks: ')
cur.execute('SELECT title, plays from Tracks')
for row in cur:
    print(row)

cur.execute('DELETE FROM Tracks WHERE plays < 100')
conn.commit()
cur.close()

