from unittest import TestCase, mock

from pyurbandict import UrbanDict
from pyurbandict.parse import Definition


class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data


def mock_request(*args, **kwargs):
    data = {
        "list": [
            {
                "word": "python",
                "definition": (
                    "The best thing to happen to [Computer Science] "
                    "students in a data and [file] structures or [algorithms] class."
                ),
                "example": (
                    'Joe: "Man...I spent a week coding that [algorithm] in C."\r\n'
                    'Moe: "I got it [done in one] evening with [Python]. '
                    'It works great."\r\nJoe: "Say, what? Where can I download that?"'
                ),
                "author": "TheNextBillGates",
                "thumbs_up": 243,
                "thumbs_down": 71,
                "sound_urls": [
                    "https://api.twilio.com/2008-08-01/Accounts/"
                    "ACd09691b82112e4b26fce156d7c01d0ed/Recordings"
                    "/RE7065a4ef810937cc16ae2b6e4b54b67d"
                ],
                "written_on": "2010-03-24T05:24:18.000Z",
                "permalink": "http://python.urbanup.com/4826760",
                "defid": 4826760,
                "current_vote": "",
            }
        ]
    }
    return MockResponse(data, 200)


class ParseTest(TestCase):
    def setUp(self) -> None:
        self.mock_definition = Definition(
            word="python",
            definition=(
                "The best thing to happen to [Computer Science] "
                "students in a data and [file] structures or [algorithms] class."
            ),
            example=(
                'Joe: "Man...I spent a week coding that [algorithm] in C."\r\n'
                'Moe: "I got it [done in one] evening with [Python]. It works great."'
                '\r\nJoe: "Say, what? Where can I download that?"'
            ),
            author="TheNextBillGates",
            thumbs_up=243,
            thumbs_down=71,
            sound_urls=[
                "https://api.twilio.com/2008-08-01/Accounts/"
                "ACd09691b82112e4b26fce156d7c01d0ed/Recordings"
                "/RE7065a4ef810937cc16ae2b6e4b54b67d"
            ],
            written_on="2010-03-24T05:24:18.000Z",
            permalink="http://python.urbanup.com/4826760",
            defid=4826760,
            current_vote="",
        )

        return super().setUp()

    @mock.patch("requests.get", side_effect=mock_request)
    def test_search(self, mock_get) -> None:
        """Test the search method."""

        # Use mocks instead of actual requests.
        word = UrbanDict("python")
        data = word.search()
        self.assertTrue(word.searched)
        self.assertEqual(data[0], self.mock_definition)

    @mock.patch("requests.get", side_effect=mock_request)
    def test_search_random(self, mock_get) -> None:
        """Test the search method with a random word"""

        # Use mocks instead of actual requests.
        word = UrbanDict()
        data = word.search()
        self.assertTrue(word.searched)
        self.assertEqual(data[0], self.mock_definition)
