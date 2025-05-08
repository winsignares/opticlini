from app import create_app
import os
import mysql.connector

def execute_sql_file(path):
    with open(path, 'r') as file:
        sql = file.read()
    statements = [stmt.strip() for stmt in sql.split(';') if stmt.strip()]
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "")
    )
    cursor = conn.cursor()
    for statement in statements:
        try:
            cursor.execute(statement)
        except mysql.connector.Error as err:
            print(f"Error: {err}\nStatement: {statement}")
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    execute_sql_file('app/assets/db_creation.sql')
    app = create_app()
    app.run(host='0.0.0.0', port=4200, debug=True)