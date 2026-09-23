from collections.abc import Iterator
from importlib import import_module

import pytest
from sqlalchemy import create_engine, inspect
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker


upgrade = import_module("app.db.migrations.001_init").upgrade


@pytest.fixture
def database_engine() -> Iterator[Engine]:
    """เตรียม schema SQLite ในหน่วยความจำสำหรับทดสอบ T-01."""

    test_engine = create_engine(
        "sqlite:///:memory:", connect_args={"check_same_thread": False}
    )
    upgrade(test_engine)
    try:
        yield test_engine
    finally:
        test_engine.dispose()


@pytest.fixture
def database_session(database_engine: Engine) -> Iterator[Session]:
    """เปิด session สำหรับตรวจ schema และงาน backend ที่ใช้ fixture นี้."""

    session_factory = sessionmaker(bind=database_engine)
    with session_factory() as session:
        yield session


def schema_tables(database_engine: Engine) -> set[str]:
    """คืนชื่อตารางที่ migration สร้างเพื่อให้ test ตรวจ schema ได้."""

    return set(inspect(database_engine).get_table_names())