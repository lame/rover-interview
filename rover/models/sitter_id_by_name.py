from cqlengine import columns, Model


class SitterIDByName(Model):
    __table_name__ = 'sitter_id_by_name'

    sitter_name = columns.Text(primary_key=True)
    sitter_id = columns.Integer(primary_key=True)
