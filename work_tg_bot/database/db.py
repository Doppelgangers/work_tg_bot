from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_NAME = "sqlite:///dns_db.sqlite"

engine = create_engine(DATABASE_NAME)
Session = sessionmaker(bind=engine)

Base = declarative_base()


class DNSRecord(Base):
    __tablename__ = 'dns_db'

    id = Column(Integer, primary_key=True, autoincrement=True)
    domain = Column(String(64), nullable=False)
    host = Column(String(64), nullable=False)
    user_id = Column(String(64), nullable=False)
    status = Column(String(64), nullable=True, default="pending")

    def __str__(self):
        return f"Domain: {self.domain}, Host: {self.host}"
