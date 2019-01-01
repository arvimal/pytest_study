#!/usr/bin/env python3

"""
Test the Task data type
"""

from collections import namedtuple

Task = namedtuple("Task", ["Summary", "Owner", "Done", "ID"])
Task.__new__.__defaults__ = (None, None, False, None)

def test_defaults():
    """
    Using parameters should invoke defaults
    """

    t1 = Task()
    t2 = Task(None, None, False, None)

    assert t1 == t2


def test_member_access():
    t = Task("Buy Milk", "Brian")
    assert t.Summary == "Buy Milk"
    assert t.Owner == "Brian"
    assert (t.Done, t.ID) == (False, None)



