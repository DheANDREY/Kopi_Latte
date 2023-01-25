import sqlite3

koneksikeDB = sqlite3.connect('cars.db')

k = koneksikeDB.cursor()

k.execute(
	"""
		INSERT INTO TBCars (
		ID,
		BRAND,
		MODEL,
		PRICE
		)
		VALUES (
		"101",
		"Honda",
		"Accord",
		"150"
		)
		
	"""
	)


koneksikeDB.commit()
koneksikeDB.close()
print("update berhasil")