import ormar

from app.db.db import database, metadata


class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database
