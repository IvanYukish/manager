import ormar

from app.db.base import BaseMeta


class User(ormar.Model):
    id: int = ormar.Integer(primary_key=True, index=True)
    first_name: str = ormar.String(max_length=30)
    last_name: str = ormar.String(max_length=30)
    email: str = ormar.String(unique=True, index=True, nullable=False, max_length=100)
    hashed_password: str = ormar.String(nullable=False, max_length=100)
    is_active: bool = ormar.Boolean(default=True)
    is_superuser: bool = ormar.Boolean(default=False)

    class Meta(BaseMeta):
        pass
