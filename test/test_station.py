import datetime
from test.stack_test_case import StackTestCase
from api.models.station import Station
from api.models.observation import Observation

class TestStation(StackTestCase):

  def testCreateEmpty(self):
    instance = Station().put()
    self.assertTrue(instance)

  def testCreateWithParam(self):
    instance = Station(station_id = "abcdefg")
    self.assertEqual("abcdefg", instance.station_id)

  def testMostRecentObservation(self):
    instance = Station(station_id = "abcdefg")
    instance.put()

    observation = Observation(
        station_id = instance.station_id,
        wave_height_meters = 10,
    )
    observation.put()

    instance.most_recent_observation = observation
    instance.put()
