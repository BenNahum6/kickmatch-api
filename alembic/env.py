import sys
import os

# הוסף את השורש של הפרויקט ל־sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context

import os
from dotenv import load_dotenv

# --- ייבוא של Base ---
from app.db.database_sqlalchemy import Base

# Imports all models (this is how Alembic will recognize them)
from app.db.models import user, playerGame


# זה מה שמאפשר לאוטוגנרייט לעבוד
target_metadata = Base.metadata

# --- Alembic config ---
config = context.config

# Logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Load the .env file
load_dotenv()

# Get the database URL from .env
database_url = os.getenv('SUPABASE_CONNECTION_STR')

if not database_url:
    raise ValueError("DATABASE_URL לא מוגדר בקובץ .env שלך")

# Update Alembic to work with this URL instead of what's in the ini
config.set_main_option('sqlalchemy.url', database_url)


def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
