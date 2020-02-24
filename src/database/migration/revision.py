from src.database import migration

if __name__ == "__main__":
    migration.revision()

if __name__ == "__main__":
    migration.upgrade()