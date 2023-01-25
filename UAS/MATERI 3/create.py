import sqlite3

koneksikeDB = sqlite3.connect('cars.db')

k = koneksikeDB.cursor()

k.execute(
	"""
		CREATE TABLE TBCars (
		ID,
		BRAND,
		MODEL,
		PRICE
		)
	"""
	)

koneksikeDB.commit()
koneksikeDB.close()
print("update berhasil")