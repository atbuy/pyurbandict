from dataclasses import dataclass, field

import requests


@dataclass
class Definition:
    word: str | None = ""
    definition: str | None = ""
    example: str | None = ""
    author: str | None = ""
    thumbs_up: int | None = None
    thumbs_down: int | None = None
    sound_urls: list[str] | None = field(default_factory=list)
    written_on: str | None = ""
    permalink: str | None = ""
    defid: int | None = None
    current_vote: str = ""


class UrbanDict:
    def __init__(self, word: str | None = None) -> None:
        self.url = f"https://api.urbandictionary.com/v0/define?term={word}"
        if not word:
            self.url = "https://api.urbandictionary.com/v0/random"

        self.searched = False
        self.definitions = None

    def search(self) -> list[Definition]:
        """Returns a dictionary with JSON data from urbandictionary."""

        data = requests.get(self.url).json()
        self.searched = True

        # Parse each listing and pass it to the Definition dataclass.
        definitions = [Definition(**item) for item in data["list"]]
        self.definitions = definitions
        return definitions
