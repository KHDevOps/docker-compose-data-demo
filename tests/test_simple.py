import subprocess
import time
import psycopg2

def test_docker_compose_works():
    """Simple test to verify docker-compose services work"""

    # Start services
    print("Starting docker-compose services...")
    subprocess.run(["docker","compose", "up", "-d"], cwd="..")

    # Wait for services to be ready
    print("Waiting for services to start...")
    time.sleep(5)

    try:
        # Test database connection
        print("Testing database connection...")
        conn = psycopg2.connect(
            host="localhost",
            port=5432,
            database="postgres",
            user="postgres",
            password="password123"
        )

        # Check if table exists and has data
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM random_users")
        count = cur.fetchone()[0]

        print(f"Found {count} users in database")

        # Close connection
        cur.close()
        conn.close()

        # Assert we have data
        assert count > 0, "No data found in random_users table"

    finally:
        # Always cleanup
        print("Stopping docker-compose services...")
        subprocess.run(["docker", "compose", "down"], cwd="..")