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
        self.assertEqual(b'{ "imie":"Kasia", "mgs":Hello World!"}', rv.data)

    def test_msg_with_output_xml(self):
        rv = self.app.get('/?output=xml')
        correct_output = ('<greeting>\n\t<name>'
                          + 'Kasia'
                          + '</name>\n\t<msg>'
                          + 'Hello World!'
                          + '</msg>\n</greetings>\n')
        self.assertEqual(correct_output.encode(), rv.data)
