from test import client, app
from controllers.utilities.capstone import query_capstone, CapstoneQuery

def test_query_capstone(client):
    capstones =query_capstone(2024, 'test_capstone')
    assert len(capstones)==1
    
    capstone =capstones[0]
    test_capstone =CapstoneQuery(('test_capstone_title', 'test_capstone_pic'))
    assert capstone.title == test_capstone.title and \
        capstone.person == test_capstone.person


def test_query_capstone_none(client):
    capstones =query_capstone(2024, 'none')
    assert len(capstones) == 0