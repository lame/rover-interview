from cqlengine import columns, Model


class SitterNameByID(Model):
    __table_name__ = 'sitter_name_by_id'

    sitter_id = columns.Integer(primary_key=True)
    sitter_name = columns.Text()
