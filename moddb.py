import sqlite3

def drop_tables_from_etfs_db():
	db_path = 'etfs_data.db'
	tables = ['category_weights', 'historical_data', 'sqlite_sequence']
	conn = sqlite3.connect(db_path)
	cursor = conn.cursor()
	for table in tables:
		try:
			cursor.execute(f"DROP TABLE IF EXISTS {table}")
			print(f"Dropped table: {table}")
		except Exception as e:
			print(f"Error dropping table {table}: {e}")
	conn.commit()
	conn.close()

if __name__ == "__main__":
	drop_tables_from_etfs_db()
