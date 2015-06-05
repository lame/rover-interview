from cqlengine import columns, Model


class SitterProfile(Model):
    __table_name__ = 'sitter_profile'

    id = columns.Integer(primary_key=True)
    image = columns.Text()
    owner_review_text = columns.Text()
    score = columns.Float(double_precision=True)
    rating = columns.Decimal()
