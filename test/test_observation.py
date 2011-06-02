import datetime
from test.stack_test_case import StackTestCase
from api.models.observation import Observation
from api.models.station import Station

class TestObservation(StackTestCase):

  def testCreateEmptyish(self):
    instance = Observation(station_id = "abcd").put()
    self.assertTrue(instance)

  def testCreateWithParam(self):
    instance = Observation(station_id = "abcd1234")
    self.assertEqual("abcd1234", instance.station_id)
