import sqlalchemy
import databases
import ormar

from app.settings.config import settings


metadata = sqlalchemy.MetaData()
database = databases.Database(settings.ORMAR_DATABASE_URL)
engine = sqlalchemy.create_engine(settings.ORMAR_DATABASE_URL)


def model_register():
    pass

