import javaproperties
import io
from robot.api.deco import keyword

# Create an html documentation of this file:
# python -m robot.libdoc ./JavaPropertiesLibrary.py ./docs/JavaPropertiesLibrary.html


class JavaPropertiesLibrary:
    """
    Library for interaction with *.properties files, which is a common format
    to store parameters in Java
    ([https://en.wikipedia.org/wiki/.properties|see here]).

    = Usage =
    The library contains keywords for either getting resetting a parameter
    value. Moreover, the complete content of a properties file can be into a
    string variable using the keyword ``Get properties file content``.
    """
    ROBOT_LIBRARY_TEST_DOC_FORMAT = 'ROBOT'
    __version__ = '0.1'

    def __init__(self):
        pass

    @keyword
    def get_properties_file_content(self, prop_file_path):
        """
        Reads the complete content of a properties file located at
        ``prop_file_path`` and returns its content as a dictionary
        """

        try:
            prop_file = open(prop_file_path, "r")
            properties = javaproperties.load(prop_file)
            prop_file.close()

            return properties

        except OSError as err:
            print("File cannot be opened: " + err)

    @keyword
    def get_properties_value(self, prop_file_path, key):
        """
        Returns the value of a parameter name ``key`` within a read-in properties
        using the ``get_properties_file`` method and returns its value as a String
        ``properties_file`` as a String
        """
        all_content = self.get_properties_file_content(prop_file_path)

        return all_content[key]

    @keyword
    def change_properties_value(self, prop_file_path, prop_key, value):
        """
        Changes the value of the parameter ``prop_key`` inside the properties file
        located at ``prop_file_path`` to the given ``value``
        """

        prop_file = io.open(prop_file_path, "r", encoding="utf-8")
        properties = javaproperties.load(prop_file)
        properties[prop_key] = str(value)

        with io.open(prop_file_path, "w", encoding="utf-8") as fp:
            javaproperties.dump(properties, fp, sort_keys=True)

