from cqlengine import columns, Model
from uuid import uuid4


class RatingBySitter(Model):
    __table_name__ = 'rating_by_sitter'

    sitter_id = columns.Integer(primary_key=True)
    rating = columns.Float(primary_key=True, double_precision=True)
    id = columns.UUID(default=uuid4)
