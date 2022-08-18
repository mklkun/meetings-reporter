import pandas as pd
from datetime import datetime

from meetings_reporter import Meeting
from meetings_reporter import __version__
from meetings_reporter import parse_meetings
from meetings_reporter import generate_meetings_conflicts


t815 = datetime.strptime('8:15am', '%I:%M%p')
t830 = datetime.strptime('8:30am', '%I:%M%p')
t900 = datetime.strptime('9:00am', '%I:%M%p')
t1000 = datetime.strptime('10:00am', '%I:%M%p')


def test_version():
    assert __version__ == '0.1.0'


def test_parse_meetings():
    # Preparing input and output
    data_frame = pd.DataFrame({'start': {0: '8:15am', 1: '9:00am'}, 'end': {0: '8:30am', 1: '10:00am'}})
    result_list = [Meeting(t815, t830), Meeting(t900, t1000)]
    # Test
    assert parse_meetings(data_frame) == result_list


def test_generate_meetings_without_conflicts():
    # Preparing input and output
    meetings_list = [Meeting(t815, t830), Meeting(t900, t1000)]
    conflicts_result = []
    # Test
    assert generate_meetings_conflicts(meetings_list) == conflicts_result


def test_generate_meetings_with_conflicts():
    # Preparing input and output
    meetings_list = [Meeting(t815, t900), Meeting(t830, t1000)]
    conflicts_result = [(Meeting(t815, t900), Meeting(t830, t1000))]
    # Test
    assert generate_meetings_conflicts(meetings_list) == conflicts_result
