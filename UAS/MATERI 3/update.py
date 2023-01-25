import sqlite3

koneksikeDB = sqlite3.connect('cars.db')

k = koneksikeDB.cursor()

k.execute(
	"""
		UPDATE TBCars SET
			MODEL="C30"
		WHERE 
			ID="106"
		
	"""
	)

koneksikeDB.commit()
koneksikeDB.close()
print("update berhasil")