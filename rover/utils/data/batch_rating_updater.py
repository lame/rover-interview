"""
With cassandra, it is inefficient to create
a 'count' or average that requires a read-write.
Because it is not program essential to have this
be an exact number all the time, it is a perfect
candidate for a batch update. This can be tuned to
update as frequently as desired.
"""
