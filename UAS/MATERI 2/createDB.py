import sqlite3
konekDB = sqlite3.connect('cars28.db')
k = konekDB.cursor()

k.execute(
    """
    CREATE TABLE cars28 (
	    ID	char(5),
	    BRAND	char(20),
	    MODEL	char(20),
	    PRICE	INTEGER,
	    PRIMARY KEY("ID")
        )
    """    
        )
konekDB.commit()
konekDB.close()
