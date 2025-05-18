import json
import psycopg2



with open('logins.json', 'r') as file:
    LOGINS = json.load(file)

try:
    CONN = psycopg2.connect(
        database=LOGINS["DB_NAME"],
        user=LOGINS["DB_USER"],
        password=LOGINS["DB_PASSWORD"],
        host=LOGINS["DB_ADDRESS"],
        port=LOGINS["DB_PORT"]
    )
except Exception as e:
    print(f"Erreur avec la BDD : {e}")

