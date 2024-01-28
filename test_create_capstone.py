from test import client, app
from controllers.utilities.capstone import create_capstone, query_capstone


def test_create_capstone_successfully(client):
    create_capstone('test_name_1', 'student', '4', '2024', 'test_title', 'test_company', 'test_contact', 'test_description')
    capstones = query_capstone('2024', 'test_title')
    capstone =capstones[0]
    assert capstone.pic =='test_name_1'
    assert capstone.role =='student'
    assert capstone.nstudents =='4'
    assert capstone.year =='2024'
    assert capstone.title =='test_title'
    assert capstone.companyname =='test_company'
    assert capstone.poc =='test_contact'
    assert capstone.description =='test_description'


def test_create_capstone_none(client):
    create_capstone('test_name_1', 'student', '4', '2024', 'test_title', 'test_company', 'test_contact', 'test_description')
    capstones = query_capstone('2024', 'test_title')
    assert len(capstones) == 0