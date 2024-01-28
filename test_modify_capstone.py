from test import client, app
from controllers.utilities.capstone import create_capstone, get_capstone_by_title, update_capstone


def test_modify_capstone_successfully(client):
    #Create capstone entry
    create_capstone('test_name_1', '1', '4', '2024', 'test_title', 'test_company', 'test_contact', 'test_description')
    allcapstones = get_capstone_by_title('test_title')
    capstone = allcapstones[0]
    #Check that capstone entry has successfully been created by checking if it exists by querying it 
    assert capstone.pic =='test_name_1'
    assert capstone.role_id =='1'
    assert capstone.nstudent =='4'
    assert capstone.year =='2024'
    assert capstone.title =='test_title'
    assert capstone.companyname =='test_company'
    assert capstone.poc =='test_contact'
    assert capstone.description =='test_description'
    #Update the newly created entry
    updatedCapstone = update_capstone('test-title', 'new_name', '1', '5', '2024', 'new_title', 'new_company', 'new_contact', 'new_description')
    #Search for entry with newly updated title
    newCapstones = query_capstone('2024', 'new_title')
    #Check that an entry with the title exists
    assert len(newCapstones) > 0
    retrievedCapstone = newCapstones[0]
    #Check if the returned entry from search matches the newly updated information
    assert retrievedCapstone.pic =='new_name'
    assert retrievedCapstone.role_id =='1'
    assert retrievedCapstone.nstudent =='5'
    assert retrievedCapstone.year =='2024'
    assert retrievedCapstone.title =='new_title'
    assert retrievedCapstone.companyname =='new_company'
    assert retrievedCapstone.poc =='new_contact'
    assert retrievedCapstone.description =='new_description'


def test_modify_capstone_none(client):
    #Create capstone entry
    create_capstone('test_name_1', '1', '4', '2024', 'test_title', 'test_company', 'test_contact', 'test_description')
    allcapstones = get_capstone_by_title('test_title')
    capstone = allcapstones[0]
    #Check that capstone entry has successfully been created by checking if it exists by querying it 
    assert capstone.pic =='test_name_1'
    assert capstone.role_id =='1'
    assert capstone.nstudent =='4'
    assert capstone.year =='2024'
    assert capstone.title =='test_title'
    assert capstone.companyname =='test_company'
    assert capstone.poc =='test_contact'
    assert capstone.description =='test_description'
    #Update the newly created entry
    updatedCapstone = update_capstone('test-title', 'new_name', '1', '5', '2024', 'new_title', 'new_company', 'new_contact', 'new_description')
    #Search for entry with newly updated title
    newCapstones = query_capstone('2024', 'new_title')
    #If no entries with the updated title exists, it means that no entries were updated successfully
    assert len(newCapstones) == 0