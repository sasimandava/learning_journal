"""SM: 02/12/2017 Pyramid Project homework#5."""
import datetime
from sqlalchemy import (
    Column,
    Integer,
    Unicode,
    UnicodeText,
    DateTime
)
from .meta import Base
from .models import includeme

class Entry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode(255), unique=True, nullable=False)
    body = Column(UnicodeText, default=u'')
    created = Column(DateTime, default=datetime.datetime.utcnow)
    edited = Column(DateTime, default=datetime.datetime.utcnow)

    @classmethod
    def all(cls, session=None):
        if session is None:
            # session = DBSession
            session = cls.dbsession
        return session.query(cls).order_by(Entry.created).all()


    @classmethod
    def by_id(cls, id, session=None):
        if session is None:
            # session = DBSession
            session = cls.dbsession
        return session.query(cls).get(id)
