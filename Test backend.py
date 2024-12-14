from backend import *
import unittest

def test_add_tasks():
    tasks.clear()
    add_tasks("object")
    assert "object" in get_tasks()

def test_get_tasks():
    tasks.clear()
    add_tasks("object")
    assert get_tasks() == ["object"]


test_add_tasks()
test_get_tasks()