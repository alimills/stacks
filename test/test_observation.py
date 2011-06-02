import datetime
from test.stack_test_case import StackTestCase
from api.models.observation import Observation
from api.models.station import Station

class TestObservation(StackTestCase):

  def testCreateEmpty(self):
    instance = Observation().put()
    self.assertTrue(instance)

  def testCreateWithParam(self):
    station = Station(station_id = "abcd1234")
    station.put()
    instance = Observation(station = station)
    self.assertEqual("abcd1234", instance.station.station_id)
