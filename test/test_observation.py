import datetime
from test.stack_test_case import StackTestCase
from api.models.observation import Observation

class TestObservation(StackTestCase):

  def testCreateEmpty(self):
    instance = Observation().put()
    self.assertTrue(instance)

  def testCreateWithParam(self):
    instance = Observation(station_id = "abcd")
    self.assertEqual("abcd", instance.station_id)
