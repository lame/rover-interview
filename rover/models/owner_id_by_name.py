from cqlengine import columns, Model


class OwnerIDByName(Model):
    __table_name__ = 'owner_id_by_name'

    owner_name = columns.Text(primary_key=True)
    owner_id = columns.Integer(primary_key=True)
