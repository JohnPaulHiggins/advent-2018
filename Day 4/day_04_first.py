#!/usr/bin/python
import re

def parse_entry(entry):
    m = re.compile(r'\[(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})\]'\
                   '\D*(\d*)\D* (up|asleep)*')
    return re.match(m, entry).groups()


print(parse_entry('[1518-07-03 23:58]'\
                   'Guard #2437 begins shift'))
assert parse_entry('[1518-07-03 23:58]'\
                   'Guard #2437 begins shift') == ('1518',
                                                   '07',
                                                   '03',
                                                   '23',
                                                   '58',
                                                   '2437',
                                                   None)

assert parse_entry('[1518-09-23 00:54] falls asleep') == ('1518',
                                                          '09',
                                                          '23',
                                                          '00',
                                                          '54',
                                                          'asleep')

assert parse_entry('[1518-07-27 00:59] wakes up') == ('1518',
                                                      '07',
                                                      '27',
                                                      '00',
                                                      '59',
                                                      'up')

assert sorted(['[1518-07-03 23:58] Guard #2437 begins shift',
               '[1518-09-23 00:54] falls asleep',
               '[1518-07-27 00:59] wakes up'],
               key = lambda x: parse_entry(x)[:5]) == \
                       ['[1518-07-03 23:58] Guard #2437 begins shift',
                        '[1518-07-27 00:59] wakes up',
                        '[1518-09-23 00:54] falls asleep']

