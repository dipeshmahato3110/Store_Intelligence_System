from sqlalchemy import create_engine

DATABASE_URL = (
    "postgresql://admin:admin@localhost:5432/storedb"
)

engine = create_engine(DATABASE_URL)

connection = engine.connect()

print("Database Connected Successfully")