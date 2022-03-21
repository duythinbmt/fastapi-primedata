from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgres://qijrkmmgpaowpt:40ab622c3de0488460bd815a6cd6ee34e0a5a77a43ce13a10f4e462e2b0aad24@ec2-44-194-167-63.compute-1.amazonaws.com:5432/dcpvpm0pu13lia"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
