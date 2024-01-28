from test import client, app
from controllers.utilities.capstone import create_capstone, get_capstone_by_title, delete_capstone_title, query_capstone


def test_delete_capstone_successfully(client):
    #Create capstone entry
    create_capstone('test_name_1', '1', '4', '2024', 'test_delete_title', 'test_company', 'test_contact', 'test_description')
    capstone = get_capstone_by_title('test_delete_title')
    #Check that capstone entry has successfully been created by checking if it exists by querying it 
    assert capstone.pic =='test_name_1'
    assert capstone.role ==1
    assert capstone.nstudents ==4
    assert capstone.year ==2024
    assert capstone.title =='test_delete_title'
    assert capstone.companyname =='test_company'
    assert capstone.poc =='test_contact'
    assert capstone.description =='test_description'
    #Delete
    delete_capstone_title('test_delete_title')
    capstones = query_capstone(2024, 'test_delete_title')
    #If entry is deleted, no entries is returned upon calling the query
    assert len(capstones) == 0


def test_delete_capstone_none(client):
    #Create capstone entry
    create_capstone('test_name_1', '1', '4', '2024', 'test_delete_title_1', 'test_company', 'test_contact', 'test_description')
    capstone = get_capstone_by_title('test_delete_title_1')
    #Check that capstone entry has successfully been created by checking if it exists by querying it 
    assert capstone.pic =='test_name_1'
    assert capstone.role ==1
    assert capstone.nstudents ==4
    assert capstone.year ==2024
    assert capstone.title =='test_delete_title_1'
    assert capstone.companyname =='test_company'
    assert capstone.poc =='test_contact'
    assert capstone.description =='test_description'
    #Delete
    delete_capstone_title('delete_none')
    capstones = query_capstone('2024', 'test_delete_title_1')
    #If entry is not deleted, it will be returned when calling the query
    assert len(capstones) > 0