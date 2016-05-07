
#  Web-history-portable

Web-history-portable is an app that allows for portablility of your web surg=fing history online therefore you nolonger have to memmorise your surfing url content anymore. It is built with [Python][0] using the [Django Web Framework][1].

This project has the following basic apps:

* gethistoryfile ( Defines underlying OS platform and locates surfing history file)
* table ( Manages the jQuery and ajax display and actions on tabulised content)
* crispy_forms ( Renders great customised bootstrap3 form view)

## Installation

### Quick start

To set up a development environment quickly, first install Python 3. It
comes with virtualenv built-in. So create a virtual env by:

    1. `$ python3 -m venv my_proj`
    2. `$ . my_proj/bin/activate`

Install all dependencies:

    pip install -r requirements.txt

Run migrations:

    python manage.py migrate

### Detailed instructions

Take a look at the docs for more information.

[0]: https://www.alisoncodes.net/
[1]: https://www.cap10guts.com/
