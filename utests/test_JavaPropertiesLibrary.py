import os
from JavaPropertiesLibrary.keywords import JavaPropertiesLibrary as jp

def test_something():
    my_jp = jp()
    my_jp.get_properties_file_content('./utests/test.properties')
    assert 1 == 1


def test_get_properties_file_content():
    my_jp = jp()
    prop_path = os.path.abspath('./utests/test.properties')
    my_jp_content = my_jp.get_properties_file_content(prop_path)

    assert 'AcquireModule.system.traverse.TraverseType' in my_jp_content
    assert 'I am not here' not in my_jp_content


def test_get_properties_value():
    my_jp = jp()
    prop_path = os.path.abspath('./utests/test.properties')
    my_key = 'AcquireModule.system.Identifier'
    my_value = my_jp.get_properties_value(prop_path, my_key)

    assert my_value != ''
    assert my_value == 'System_SN12345'


def test_change_properties_value():
    my_jp = jp()
    prop_path = os.path.abspath('./utests/test.properties')
    my_key = 'AcquireModule.system.Identifier'
    my_new_value = 'mynewvalue'
    my_jp.change_properties_value(prop_path, my_key, my_new_value)
    new_value = my_jp.get_properties_value(prop_path, my_key)

    assert new_value == my_new_value

    my_jp.change_properties_value(prop_path, my_key, 'System_SN12345')
    default_value = my_jp.get_properties_value(prop_path, my_key)

    assert default_value == 'System_SN12345'

