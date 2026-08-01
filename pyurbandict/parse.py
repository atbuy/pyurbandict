from dataclasses import dataclass, field, fields
from typing import Any, Optional

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
    udimg_url: Optional[str] = ""
    play_sound_url: Optional[str] = ""
    
    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Definition":
        """Filters out all unknown keyword arguments."""
        
        class_fields = {f.name for f in fields(cls)}
        filtered_data = {k: v for k, v in data.items() if k in class_fields}
        return cls(**filtered_data)


class UrbanDict:
    def __init__(self, word: Optional[str] = None) -> None:
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
        # fix: using the correct method
        definitions = [Definition.from_dict(item) for item in data["list"]]
        self.definitions = definitions
        return definitions
