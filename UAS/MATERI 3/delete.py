import sqlite3

koneksikeDB = sqlite3.connect('cars.db')

k = koneksikeDB.cursor()

k.execute(
	"""
		DELETE FROM TBCars
		WHERE
			ID="101"
		
	"""
	)

koneksikeDB.commit()
koneksikeDB.close()
print("update berhasil")