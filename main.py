import psycopg
from faker import Faker

fake = Faker()

conn = psycopg.connect(
    host="localhost",
    port=5432,
    dbname="testdb",
    user="postgres",
    password="postgres"
)

with conn:
    with conn.cursor() as cur:
        # Create table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                created_at TIMESTAMP DEFAULT now()
            );
        """)

        # Insert 10 random users
        for _ in range(10):
            name = fake.name()
            email = fake.unique.email()

            cur.execute(
                "INSERT INTO users (name, email) VALUES (%s, %s)",
                (name, email)
            )

        # Query users
        cur.execute("SELECT * FROM users;")
        rows = cur.fetchall()

        print("\nUsers in database:")
        for row in rows:
            print(row)
