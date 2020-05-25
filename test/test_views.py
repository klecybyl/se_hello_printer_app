'''
import unittest
from hello_world import app
from hello_world.formater import SUPPORTED


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_outputs(self):
        rv = self.app.get('/outputs')
        s = str(rv.data)
        ','.join(SUPPORTED) in s

    def test_msg_with_output_json(self):
        rv = self.app.get('/?output=json')
        self.assertEqual(b'{ "imie":"Kasia", "mgs":Hello World!"}', rv.data) # noqa

    def test_msg_with_output_xml(self):
        rv = self.app.get('/?output=xml')
        correct_output = ('<greeting>\n\t<name>'
                          + 'Kasia'
                          + '</name>\n\t<msg>'
                          + 'Hello World!'
                          + '</msg>\n</greetings>\n')
        self.assertEqual(correct_output.encode(), rv.data)

    def test_name(self):
        rv = self.app.get('/?name=Kasia')
        self.assertEqual(b'Kasia Hello World!"}', rv.data) # noqa
'''

import unittest
from ddt import ddt, data
from hello_world import app
from hello_world.formater import SUPPORTED


@ddt
class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_outputs(self):
        rv = self.app.get('/outputs')
        s = str(rv.data)
        ','.join(SUPPORTED) in s

    @data('Ania', 'Ola', 'Konrad')
    def test_msg_with_output_1(self, name):
        query = 'name=' + name + '&output=json'
        rv = self.app.get('/?' + query)
        correct_res = b'{ "imie":"'\
                      + bytes(name.encode('utf-8'))\
                      + b'", "mgs":"Hello World!"}'
        self.assertEqual(correct_res, rv.data)  # noqa

    @data('Basia', 'Wojtek', 'Tester')
    def test_msg_with_output_2(self, name):
        query = 'name=' + name + '&output=xml'
        rv = self.app.get('/?' + query)
        correct_output = ('<greetings>\n\t<name>'
                          + name
                          + '</name>\n\t<msg>'
                          + 'Hello World!'
                          + '</msg>\n</greetings>\n')
        self.assertEqual(correct_output.encode(), rv.data)
