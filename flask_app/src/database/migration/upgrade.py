from flask_app.src.database import migration

if __name__ == "__main__":
    migration.upgrade()
