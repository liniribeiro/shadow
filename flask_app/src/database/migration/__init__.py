from alembic import command

from flask_app.src.database.migration.config import alembic_cfg


def upgrade():
    print("Start Migration")
    command.upgrade(alembic_cfg, "head")

    print("End Migration")


def revision():
    command.revision(alembic_cfg, autogenerate=True)


__all__ = ("upgrade", "revision")


if __name__ == '__main__':
    upgrade()
