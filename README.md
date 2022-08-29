# pyurbandict

This is a python project, that fetches definitions of words from urban dictionary.

Future additions. PRs are always welcome :)
* Calculate ratio of `thumbs_up` and `thumbs_down` and decide the probability of a correct definition.

# Installation

*Python 3.10 or higher is required*

To install the library you can use the following command:

```
# Linux/MacOS
python3 -m pip install --upgrade pyurbandict

# Windows
py -3 -m pip install --upgrade pyurbandict
```

# Quick Example

You can create an instance of the `UrbanDict` class and pass a word to it. After that you can use the `search` method that will retrieve the definitions from UrbanDictionary.
If you want to you can also leave the word attribute empty, in which case a random word is selected by UrbanDictionary.

```python
from pyurbandict import UrbanDict

word = UrbanDict("python")
results = word.search()
print(results[0])

>>> Definition(word='python', definition='The best thing to happen to [Computer Science] students in a data and [file] structures or [algorithms] class.', example='Joe: "Man...I spent a week coding that [algorithm] in C."\r\nMoe: "I got it [done in one] evening with [Python]. It works great."\r\nJoe: "Say, what? Where can I download that?"', author='TheNextBillGates', thumbs_up=243, thumbs_down=71, sound_urls=['https://api.twilio.com/2008-08-01/Accounts/ACd09691b82112e4b26fce156d7c01d0ed/Recordings/RE7065a4ef810937cc16ae2b6e4b54b67d'], written_on='2010-03-24T05:24:18.000Z', permalink='http://python.urbanup.com/4826760', defid=4826760, current_vote='')
```

# Links
* [PyPi]()
