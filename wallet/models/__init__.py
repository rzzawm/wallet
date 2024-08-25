from pathlib import Path
from peewee import SqliteDatabase

_db_path = Path.home() / "wallet-data" / "database.db"

if not _db_path.parent.exists():
    _db_path.parent.mkdir()
    print(f"database created at {_db_path}")

db = SqliteDatabase(_db_path)
