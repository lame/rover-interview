from cqlengine import columns, Model


class OwnerProfile(Model):
    __table_name__ = 'owner_profile'

    id = columns.Integer(primary_key=True)
    name = columns.Text()
    image = columns.Text()
    owner_review_text = columns.Text()
    dogs = columns.Set(columns.Text)
