# test_database.py - Test database connection

from database import engine, create_tables, SessionLocal, User, Document, Analysis

# Test 1: Create tables
print("Test 1: Creating tables...")
create_tables()
print("✓ Tables created successfully")

# Test 2: Get session
print("\nTest 2: Getting database session...")
db = SessionLocal()
print("✓ Database session created")

# Test 3: Check if empty
print("\nTest 3: Checking database...")
user_count = db.query(User).count()
print(f"✓ Users in database: {user_count}")

# Test 4: Add test user
print("\nTest 4: Adding test user...")
test_user = User(
    username="testuser",
    email="test@example.com",
    hashed_password="fake_hash_123"
)
db.add(test_user)
db.commit()
print("✓ Test user added")

# Test 5: Query test user
print("\nTest 5: Querying test user...")
user = db.query(User).filter(User.username == "testuser").first()
print(f"✓ Found user: {user.username} ({user.email})")

# Test 6: Cleanup
print("\nTest 6: Cleaning up...")
db.delete(user)
db.commit()
print("✓ Test user deleted")

db.close()
print("\n✓✓✓ All database tests passed! ✓✓✓")
