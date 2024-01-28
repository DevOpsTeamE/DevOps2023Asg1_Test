from test import client, app
from controllers.utilities.capstone import create_capstone, get_capstone_by_title, update_capstone, query_capstone


def test_modify_capstone_successfully(client):
    #Create capstone entry
    create_capstone('test_name_1', '1', '4', '2024', 'test_modify_title', 'test_company', 'test_contact', 'test_description')
    capstone = get_capstone_by_title('test_title')
    #Check that capstone entry has successfully been created by checking if it exists by querying it 
    assert capstone.pic =='test_name_1'
    assert capstone.role ==1
    assert capstone.nstudents ==4
    assert capstone.year ==2024
    assert capstone.title =='test_modify_title'
    assert capstone.companyname =='test_company'
    assert capstone.poc =='test_contact'
    assert capstone.description =='test_description'
    #Update the newly created entry
    updatedCapstone = update_capstone('test_modify_title', 'new_name', '1', '5', '2024', 'new_title_modified', 'new_company', 'new_contact', 'new_description')
    #Search for entry with newly updated title
    retrievedCapstone = get_capstone_by_title('new_title_modified')
    #Check if the returned entry from search matches the newly updated information
    assert retrievedCapstone.pic =='new_name'
    assert retrievedCapstone.role ==1
    assert retrievedCapstone.nstudents ==5
    assert retrievedCapstone.year ==2024
    assert retrievedCapstone.title =='new_title'
    assert retrievedCapstone.companyname =='new_company'
    assert retrievedCapstone.poc =='new_contact'
    assert retrievedCapstone.description =='new_description'


def test_modify_capstone_none(client):
    #Create capstone entry
    create_capstone('test_name_1', '1', '4', '2024', 'test_modify_title_1', 'test_company', 'test_contact', 'test_description')
    capstone = get_capstone_by_title('test_title')
    #Check that capstone entry has successfully been created by checking if it exists by querying it 
    assert capstone.pic =='test_name_1'
    assert capstone.role ==1
    assert capstone.nstudents ==4
    assert capstone.year ==2024
    assert capstone.title =='test_modify_title_1'
    assert capstone.companyname =='test_company'
    assert capstone.poc =='test_contact'
    assert capstone.description =='test_description'
    #Update the newly created entry
    updatedCapstone = update_capstone('test-title', 'new_name', '1', '5', '2024', 'new_title_modified_1', 'new_company', 'new_contact', 'new_description')
    #Search for entry with newly updated title
    newCapstones = query_capstone('2024', 'new_title_modified_1')
    #If no entries with the updated title exists, it means that no entries were updated successfully
    assert len(newCapstones) == 0