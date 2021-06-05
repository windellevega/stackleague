import math
import itertools
import re
import operator
import collections

def lyricist(songbank, lyric):
    for i in songbank:
        for song in songbank[i]:
            if lyric.lower() in songbank[i][song].lower():
                return i + ' - ' + song

    return 'Not found'

def lyric_search(artist, songs, lyric):
    for i in songs:
        if lyric.lower() in songs[i].lower():
            return [artist, i, songs[i]]

    return None

######################### END OF SOLUTION #########################





import unittest

class MyTestCase(unittest.TestCase):

    def test___AL___lyric_search(self):
        bank = {
            "Sam Smith": {
                "Too Good At Goodbyes":
                    "You must think that I'm stupid, you must think that I'm a fool",
            },
            "Justin Bieber": {
                "Heartbreaker": "Don't tell me you're my heartbreaker",
                "One Less Lonely Girl":
                    "How many I told you's and start overs and shoulders have you cried on before?",
            },
        }

        lyric = "I'm stupid"

        self.assertListEqual(lyric_search("Sam Smith", bank["Sam Smith"], lyric), [
            "Sam Smith",
            "Too Good At Goodbyes",
            "You must think that I'm stupid, you must think that I'm a fool",
        ])

    def test___AL___lyric_search_2(self):
        bank = {
            "Sam Smith": {
                "Too Good At Goodbyes":
                    "You must think that I'm stupid, you must think that I'm a fool",
            },
            "Justin Bieber": {
                "Heartbreaker": "Don't tell me you're my heartbreaker",
                "One Less Lonely Girl":
                    "How many I told you's and start overs and shoulders have you cried on before?",
            },
        }

        lyric = "Thinking about forever"

        self.assertEqual(lyric_search(
            "Sam Smith", bank["Sam Smith"], lyric), None)

    def test___SE___lyricist(self):
        bank = {
            "Sam Smith": {
                "Too Good At Goodbyes":
                    "You must think that I'm stupid, you must think that I'm a fool",
            },
            "Justin Bieber": {
                "Heartbreaker": "Don't tell me you're my heartbreaker",
                "One Less Lonely Girl":
                    "How many I told you's and start overs and shoulders have you cried on before?",
            },
        }

        lyric = "Thinking about forever"

        self.assertEqual(lyricist(bank, lyric), "Not found")


if __name__ == '__main__':
    unittest.main()