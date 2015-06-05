from cqlengine import columns, Model
from uuid import uuid4


class CSVImport(Model):
    __table_name__ = 'csv_import'

    id = columns.UUID(primary_key=True, default=uuid4)
    sitter_id = columns.Integer()
    rating = columns.Integer()
    sitter_image = columns.Text()
    start_date = columns.DateTime()
    end_date = columns.DateTime()
    profile_text = columns.Text()
    owner_image = columns.Text()
    dogs = columns.Set(columns.Text)
    sitter = columns.Text()
    owner = columns.Text()
    owner_id = columns.Integer()
