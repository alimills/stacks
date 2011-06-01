from noaa_latest_observation_parser import NoaaLatestObservationParser
from test.stack_test_case import StackTestCase

class TestNoaaLatestObservationParser(StackTestCase):

  def setUp(self):
    super(TestNoaaLatestObservationParser, self).setUp()
    valid_file = "test/fixtures/noaa_latest_observations.txt"
    self.valid_source = open(valid_file).readlines()

  def testParseWithValidSource(self):
    parser = NoaaLatestObservationParser()
    parsed = parser.parse(self.valid_source)
    self.assertTrue(parsed is not None)
    self.assertEqual(647, len(parsed))
