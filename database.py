from sqlalchemy import create_engine, text
import os

# Use environment variables for sensitive information


# Construct the database URL
db_connector = f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}?charset=utf8mb4"

# Configure SSL parameters if necessary
ssl_args = {"ssl": {"ssl_ca": "/etc/ssl/cert.pem"}}

# Create the database engine
engine = create_engine(db_connector, connect_args=ssl_args)

def load_jobs_db():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT * FROM jobs"))

            # Fetch all rows as a list of dictionaries
            jobs = [dict(row) for row in result.fetchall()]
            return jobs

    except Exception as e:
        print(f"Error: {e}")
        return []

# Example usage
jobs_data = load_jobs_db()
print(jobs_data)
