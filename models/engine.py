from sqlalchemy import create_engine
from .base import Base

engine = create_engine('sqlite:////Users/ahmadel-bobou/Documents/github/menu-generator/db/sqlite.db')
Base.metadata.create_all(engine)