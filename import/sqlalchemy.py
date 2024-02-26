# @tags: import, init, sqlalchemy

from sqlalchemy import create_engine, inspect, text

engine = create_engine("sqlite:///:memory:"); display(engine)
conn = engine.connect()
inspector = inspect(conn)
