from dataclasses import dataclass
from typing import Optional

import requests


@dataclass
class Definition:
    word: str
    definition: str
    example: str
    author: str
    thumbs_up: int
    thumbs_down: int
    sound_urls: list[str]
    written_on: str
    permalink: str
    defid: int
    current_vote: str


class UrbanDict:
    def __init__(self, word: Optional[str] = None) -> None:
        self.url = (
            f"https://api.urbandictionary.com/v0/define?term={word}&definitions=1"
        )
        if not word:
            self.url = "https://api.urbandictionary.com/v0/random"

        self.searched = False
        self.definitions = None

    def search(self) -> dict:
        """Returns a dictionary with JSON data from urbandictionary."""

        data = requests.get(self.url).json()
        self.searched = True

        # Parse each listing and pass it
        # to the Definition dataclass.
        out = []
        for item in data["list"]:
            out.append(Definition(**item))

        return out
