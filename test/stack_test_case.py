import unittest
from google.appengine.ext import db
from google.appengine.ext import testbed

class StackTestCase(unittest.TestCase):

  def setUp(self):
    self.testbed = testbed.Testbed()
    self.testbed.setup_env(app_id = "12345")
    self.testbed.activate()
    self.testbed.init_datastore_v3_stub()

  def tearDown(self):
    self.testbed.deactivate()
