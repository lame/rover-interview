from cqlengine import columns, Model


class OwnerNameByID(Model):
    __table_name__ = 'owner_name_by_id'

    owner_id = columns.Integer(primary_key=True)
    owner_name = columns.Text()
