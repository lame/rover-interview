from cqlengine import columns, Model


class SitterByOwner(Model):
    __table_name__ = 'sitter_by_owner'

    owner_id = columns.Integer(primary_key=True)
    sitter_id = columns.Integer(primary_key=True)
    start_date = columns.DateTime()
    end_date = columns.DateTime()
    dogs_handled = columns.Set(columns.Text)
