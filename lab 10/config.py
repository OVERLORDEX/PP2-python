import psycopg2

def connect():
    return psycopg2.connect(
        host="ep-divine-fog-a55emvje-pooler.us-east-2.aws.neon.tech",
        dbname="neondb",
        user="neondb_owner",
        password="npg_Um02TyoiHXhw"  
    )