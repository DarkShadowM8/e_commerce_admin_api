from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

databaseUrl = 'mysql+mysqlconnector://root:root@localhost:3306/case1'
engine = create_engine( databaseUrl, echo=True)
@contextmanager
def session_scope():

    session = Session(engine)
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()