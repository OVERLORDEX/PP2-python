import psycopg2

conn = psycopg2.connect(
    host="ep-divine-fog-a55emvje-pooler.us-east-2.aws.neon.tech",
    database="neondb",
    user="neondb_owner",
    password="npg_Um02TyoiHXhw",
    port="5432"
)

cur = conn.cursor()

cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")

tables = cur.fetchall()
print("Tables in the database:")
for table in tables:
    print(table[0])

cur.close()
conn.close()