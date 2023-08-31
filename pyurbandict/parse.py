from dataclasses import dataclass, field
from typing import Optional

import requests


@dataclass
class Definition:
    word: Optional[str] = ""
    definition: Optional[str] = ""
    example: Optional[str] = ""
    author: Optional[str] = ""
    thumbs_up: Optional[int] = None
    thumbs_down: Optional[int] = None
    sound_urls: Optional[list[str]] = field(default_factory=list)
    written_on: Optional[str] = ""
    permalink: Optional[str] = ""
    defid: Optional[int] = None
    current_vote: str = ""


class UrbanDict:
    def __init__(self, word: Optional[str] = None) -> None:
        self.url = f"https://api.urbandictionary.com/v0/define?term={word}"
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
        definitions = [Definition(**item) for item in data["list"]]
        self.definitions = definitions
        return definitions
