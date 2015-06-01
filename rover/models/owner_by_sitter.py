from cqlengine import columns, Model


class OwnerBySitter(Model):
    __table_name__ = 'owner_by_sitter'

    sitter_id = columns.Integer(primary_key=True)
    owner_id = columns.Integer(primary_key=True)
    start_date = columns.DateTime()
    end_date = columns.DateTime()
