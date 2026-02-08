import psycopg2
from psycopg2 import sql

#Define connection parameters
connection_parameters = {
    'dbname': 'photon',
    'user': 'student',
    'password': 'student',
    'host': 'localhost',
    'port': '5432'
}

'''try:
    conn = psycopg2.connect(**connection_parameters)
    cursor = conn.cursor()

    # Execute a query
    cursor.execute("SELECT version();")

    # Fetch and display the result
    version = cursor.fetchone()
    print(f"Connected to - {version}")

    cursor.execute("INSERT INTO players (id, codename) VALUES ('2', 'trash can');")
    # Fetch and display data from the table
    cursor.execute("SELECT * FROM players;")
    conn.commit()
    rows = cursor.fetchall()
    for row in rows:
        print(row)

except Exception as error:
    print(f"Error connecting to PostgreSQL database: {error}")

finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if conn:
        conn.close()'''

def add_player(id, name):
    with psycopg2.connect(**connection_parameters) as conn:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO players (id, codename) VALUES (%s, %s);", (id, name))

def show_all_players(id, name):
    with psycopg2.connect(**connection_parameters) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM players;")
            rows = cursor.fetchall()
            for row in rows:
                print(row)

