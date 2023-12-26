from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker


engine = create_engine("sqlite:///dns_db.sqlite")
Session = sessionmaker(bind=engine)
Base = declarative_base()


class DNSRecord(Base):
    __tablename__ = 'dns_db'

    id = Column(Integer, primary_key=True, autoincrement=True)
    domain = Column(String(255), nullable=False)
    host = Column(String(255), nullable=False)
    user_id = Column(String(255), nullable=False)
