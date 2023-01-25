import sqlite3

koneksikeDB = sqlite3.connect('cars.db')

k = koneksikeDB.cursor()

k.execute(
	"""
		SELECT * FROM TBCars
	"""
	)

print(k.fetchall())
koneksikeDB.commit()
koneksikeDB.close()
print("update berhasil")