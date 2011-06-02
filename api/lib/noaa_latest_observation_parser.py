import csv

class NoaaLatestObservationParser():

  document_fieldnames = ['station_id', 'latitude', 'longitude', 'year',
                         'month', 'day', 'hour', 'minute',
                         'wind_direction_degrees',
                         'wind_speed_meters_per_second',
                         'gust_meters_per_second',
                         'wave_height_meters',
                         'dominant_period_meters_per_second',
                         'average_period_meters_per_second',
                         'm_wind_compass_degrees',
                         'barometric_pressure', 'ptdy',
                         'air_temperature_celcius', 'water_temperature_celcius',
                         'dewpoint', 'visibility', 'tide_height_feet',
                         'unknown_1', 'unknown_2', 'uknown_3', 'unknown_4',
                         'unknown_5', 'unknown_6', 'unknown_7']
  null_value = 'MM'

  def process_row(self, row):
    result = {}
    for index, value in enumerate(row):
      key = self.document_fieldnames[index]
      if value == self.null_value:
        result[key] = None
      else:
        result[key] = self.process_value(value)
    return result

  def parse(self, input):
    input = input.split("\n")
    input.pop(0)
    input.pop(0)
    processed = []
    for row in input:
      processed.append(self.process_row(row.split()))

    return processed
