"""
Vehicle Rental System — Interactive Query Runner
Allows running the project immediately on macOS without installing MySQL server!
"""
import sqlite3
import re
import os
import sys

DB_FILE = os.path.join(os.path.dirname(__file__), "vehicle_rental.db")
SQL_FILE = os.path.join(os.path.dirname(__file__), "vehicle_rental.sql")

def initialize_database():
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)
    print("⏳ Initializing database from vehicle_rental.sql...")
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()

    cur.execute('''
    CREATE TABLE customers (
      customer_id INTEGER PRIMARY KEY,
      customer_name TEXT,
      email TEXT,
      phone TEXT,
      city TEXT,
      driver_license_no TEXT,
      signup_date TEXT
    );''')

    cur.execute('''
    CREATE TABLE vehicles (
      vehicle_id INTEGER PRIMARY KEY,
      model_name TEXT,
      brand TEXT,
      category TEXT,
      fuel_type TEXT,
      seating_capacity INTEGER,
      daily_rate REAL,
      mileage_km INTEGER,
      vehicle_status TEXT
    );''')

    cur.execute('''
    CREATE TABLE rental_locations (
      location_id INTEGER PRIMARY KEY,
      location_name TEXT,
      city TEXT,
      address TEXT,
      contact_number TEXT,
      parking_capacity INTEGER
    );''')

    cur.execute('''
    CREATE TABLE rentals (
      rental_id INTEGER PRIMARY KEY,
      customer_id INTEGER,
      vehicle_id INTEGER,
      pickup_location_id INTEGER,
      return_location_id INTEGER,
      rental_start_date TEXT,
      rental_end_date TEXT,
      rental_duration_days INTEGER,
      total_amount REAL,
      rental_status TEXT,
      payment_method TEXT,
      FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
      FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id),
      FOREIGN KEY (pickup_location_id) REFERENCES rental_locations(location_id),
      FOREIGN KEY (return_location_id) REFERENCES rental_locations(location_id)
    );''')

    with open(SQL_FILE, "r", encoding="utf-8") as f:
        sql_content = f.read()

    for tbl in ["customers", "vehicles", "rental_locations", "rentals"]:
        matches = re.findall(r'INSERT INTO \`' + tbl + r'\` VALUES (.*?);', sql_content)
        for m in matches:
            cur.execute(f"INSERT INTO {tbl} VALUES " + m)

    conn.commit()
    conn.close()
    print("✅ Database successfully initialized (30,600 records loaded)!\n")

def run_suite(suite_filename):
    filepath = os.path.join(os.path.dirname(__file__), suite_filename)
    if not os.path.exists(filepath):
        print(f"File not found: {suite_filename}")
        return

    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Split by questions
    sections = re.split(r'-- (Q\d+\..*)', content)
    print(f"\n========================================================")
    print(f"  RUNNING: {suite_filename}")
    print(f"========================================================")

    for i in range(1, len(sections), 2):
        title = sections[i].strip()
        body = sections[i+1]
        # extract query
        clean_lines = [l for l in body.splitlines() if not l.strip().startswith("--") and not l.strip().startswith("#") and not l.strip().startswith("USE ")]
        sql = " ".join(clean_lines).strip()
        if not sql:
            continue
        if sql.endswith(";"):
            sql = sql[:-1]

        # SQLite compatibility for date functions
        test_sql = re.sub(r'YEAR\(([^)]+)\)', r"strftime('%Y', \1)", sql)
        test_sql = re.sub(r'MONTH\(([^)]+)\)', r"cast(strftime('%m', \1) as integer)", test_sql)

        print(f"\n▶ {title}")
        print(f"SQL: {sql[:100]}..." if len(sql) > 100 else f"SQL: {sql}")
        try:
            cur.execute(test_sql)
            rows = cur.fetchall()
            col_names = [d[0] for d in cur.description] if cur.description else []
            print(f"Returned {len(rows)} row(s):")
            # print header
            print(" | ".join(col_names[:6]))
            print("-" * 50)
            for r in rows[:5]:
                print(" | ".join(str(val) for val in r[:6]))
            if len(rows) > 5:
                print(f"... and {len(rows) - 5} more rows.")
        except Exception as e:
            print(f"Error executing query: {e}")

    conn.close()

if __name__ == "__main__":
    if not os.path.exists(DB_FILE):
        initialize_database()

    print("Choose an option:")
    print("1. Run Simple Queries (20 queries)")
    print("2. Run Medium Queries (20 queries)")
    print("3. Run Hard Queries (20 queries)")
    print("4. Run ALL 60 Queries")
    print("5. Reset / Rebuild Database")
    
    choice = sys.argv[1] if len(sys.argv) > 1 else "1"
    if choice == "1":
        run_suite("Simple_queries.txt")
    elif choice == "2":
        run_suite("Medium_queries.txt")
    elif choice == "3":
        run_suite("Hard_queries.txt")
    elif choice == "4":
        run_suite("Simple_queries.txt")
        run_suite("Medium_queries.txt")
        run_suite("Hard_queries.txt")
    elif choice == "5":
        initialize_database()
