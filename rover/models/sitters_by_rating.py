from cqlengine import columns, Model

"""
Could be used at scale if sitters need to be sorted
by their ranking, however this table currently wont
function correctly as a sitter can have many ratings.

This calculation will be done on the fly by python
from the sitter_profile rating with a sort by until
this can be addressed
"""


class SittersByRating(Model):
    __table_name__ = 'sitters_by_rating'

    overall_rank = columns.Integer(primary_key=True)
    rating = columns.Float(double_precision=True)
    sitter_id = columns.Integer()
