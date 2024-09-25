import psycopg2
from psycopg2 import sql

# Database connection details
host = "34.147.197.166"
port = "5432"
dbname = "nbrecords"
user = "postgres"
password = "jelszo"

# Connect to PostgreSQL server
conn = psycopg2.connect(
    host=host,
    port=port,
    dbname=dbname,
    user=user,
    password=password,
    sslmode='require'  # Ensure SSL is used
)

# Create a cursor object
cur = conn.cursor()

# SQL statements to create tables
create_table_statements = [
    """
    CREATE TABLE IF NOT EXISTS room_nr (
        id SERIAL PRIMARY KEY,
        number INTEGER
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS care_list (
        id SERIAL PRIMARY KEY,
        care TEXT
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS bowel_list (
        id SERIAL PRIMARY KEY,
        bowel_name TEXT,
        bowel_size TEXT,
        bowel_mode TEXT
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS staff (
        id SERIAL PRIMARY KEY,
        staff_name TEXT,
        staff_surname TEXT,
        staff_initials TEXT
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS fluid_list (
        id SERIAL PRIMARY KEY,
        fluid_name TEXT
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS service_list (
        id SERIAL PRIMARY KEY,
        service_name TEXT
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS units (
        id SERIAL PRIMARY KEY,
        unit_name TEXT
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS personal_care_list (
        id SERIAL PRIMARY KEY,
        personal_care_name TEXT
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS fluid_chart (
        id SERIAL PRIMARY KEY,
        resident_initials TEXT,
        timestamp TIMESTAMP,
        fluid_type TEXT,
        fluid_volume INTEGER,
        fluid_note TEXT,
        staff_initials TEXT
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS cardex_chart (
        id SERIAL PRIMARY KEY,
        resident_initials TEXT,
        timestamp TIMESTAMP,
        cardex_text TEXT,
        staff_initials TEXT
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS food_chart (
        id SERIAL PRIMARY KEY,
        resident_initials TEXT,
        timestamp TIMESTAMP,
        food_name TEXT,
        food_amount TEXT,
        food_note TEXT,
        staff_initials TEXT
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS personal_care_chart (
        id SERIAL PRIMARY KEY,
        resident_initials TEXT,
        timestamp TIMESTAMP,
        personal_care_type TEXT,
        personal_care_duration INTEGER,
        personal_care_note TEXT,
        staff_initials TEXT
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS care_frequency_chart (
        id SERIAL PRIMARY KEY,
        resident_initials TEXT,
        timestamp TIMESTAMP,
        mattress_appropriate TEXT,
        cushion_appropriate TEXT,
        functionality_check TEXT,
        pressure_areas_checked TEXT,
        redness_present TEXT,
        position TEXT,
        incontinence_urine TEXT,
        incontinence_bowels TEXT,
        diet_intake TEXT,
        fluid_intake TEXT,
        supplement_intake TEXT,
        staff_initials TEXT,
        notes TEXT
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS report_list (
        id SERIAL PRIMARY KEY,
        report_name TEXT
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS bowel_chart (
        id SERIAL PRIMARY KEY,
        resident_initials TEXT,
        timestamp TIMESTAMP,
        bowel_type TEXT,
        bowel_size TEXT,
        bowel_mode TEXT,
        bowel_note TEXT,
        staff_initials TEXT
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS residents_observations_list (
        id SERIAL PRIMARY KEY,
        observation_name TEXT
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS residents_observations_chart (
        id SERIAL PRIMARY KEY,
        resident_initials TEXT,
        unit_name TEXT,
        observation_name TEXT,
        start_date TIMESTAMP,
        end_date TIMESTAMP,
        observation_reason TEXT,
        observation_notes TEXT,
        staff_initials TEXT
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS residents (
        id SERIAL PRIMARY KEY,
        resident_name TEXT,
        resident_surname TEXT,
        unit_name TEXT,
        room_nr INTEGER,
        resident_initials TEXT,
        resident_unique_id TEXT
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS resident_identifiers (
        resident_unique_id TEXT PRIMARY KEY,
        resident_name TEXT,
        resident_surname TEXT
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS food_list (
        id SERIAL PRIMARY KEY,
        food_name TEXT
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS staff_log (
        id SERIAL PRIMARY KEY,
        timestamp TIMESTAMP,
        entry_category TEXT,
        description TEXT,
        suggested_completion_time TIMESTAMP,
        initiator TEXT,
        completer TEXT,
        task_completed BOOLEAN
    );
    """
]

# Execute each create table statement
for statement in create_table_statements:
    cur.execute(statement)

# Commit the changes
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()