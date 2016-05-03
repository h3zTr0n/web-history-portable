from __future__ import absolute_import
from __future__ import unicode_literals

from django.shortcuts import render
from gethistoryfile.models import UrlStore

# Create your views here.

class FixtureData(object):
    """docstring for FixtureData"""
    def __init__(self, data):
        super(FixtureData, self).__init__()

        class Meta:
            model = UrlStore
        self.data =

[
    {
        "fields": {
            "date_joined": "2010-09-05 13:52:36",
            "email": "invalid@example.com",
            "first_name": "",
            "groups": [],
            "is_active": true,
            "is_staff": true,
            "is_superuser": true,
            "last_login": "2010-09-05 13:52:36",
            "last_name": "",
            "password": "sha1$c4e7f$383259f017f100f2ee8b4d233e4232501a896f36",
            "user_permissions": [],
            "username": "admin"
        },
        "model": "auth.user",
        "pk": 1
    },
    {
        "fields": {
            "name": "Fred Flintstone"
        },
        "model": "sports.person",
        "pk": 1
    },
    {
        "fields": {
            "name": "Barney Rubble"
        },
        "model": "sports.person",
        "pk": 2
    },
    {
        "fields": {
            "name": "Bam-Bam"
        },
        "model": "sports.person",
        "pk": 3
    },
    {
        "fields": {
            "name": "Pebbles"
        },
        "model": "sports.person",
        "pk": 4
    },
    {
        "fields": {
            "name": "Dino"
        },
        "model": "sports.person",
        "pk": 5
    },
    {
        "fields": {
            "name": "Bedrock Bumblebees"
        },
        "model": "sports.team",
        "pk": 1
    },
    {
        "fields": {
            "name": "Whackity-sacks"
        },
        "model": "sports.team",
        "pk": 2
    },
    {
        "fields": {
            "name": "Premier"
        },
        "model": "sports.league",
        "pk": 1
    },
    {
        "fields": {
            "name": "Old-timers"
        },
        "model": "sports.league",
        "pk": 2
    },
    {
        "fields": {
            "departed": "2002-06-30",
            "joined": "2000-04-12",
            "league": 2,
            "team": 2
        },
        "model": "sports.leagueteam",
        "pk": 1
    },
    {
        "fields": {
            "departed": null,
            "joined": "2002-07-01",
            "league": 1,
            "team": 2
        },
        "model": "sports.leagueteam",
        "pk": 2
    },
    {
        "fields": {
            "departed": null,
            "joined": "2002-07-01",
            "league": 1,
            "team": 1
        },
        "model": "sports.leagueteam",
        "pk": 3
    },
    {
        "fields": {
            "departed": "2002-06-30",
            "joined": "2000-04-12",
            "league": 2,
            "umpire": 5
        },
        "model": "sports.leagueumpire",
        "pk": 1
    },
    {
        "fields": {
            "departed": null,
            "joined": "2002-07-01",
            "league": 1,
            "umpire": 5
        },
        "model": "sports.leagueumpire",
        "pk": 2
    },
    {
        "fields": {
            "departed": null,
            "joined": "2002-07-01",
            "person": 1,
            "role": "P",
            "team": 2
        },
        "model": "sports.teammember",
        "pk": 1
    },
    {
        "fields": {
            "departed": null,
            "joined": "2002-07-01",
            "person": 2,
            "role": "P",
            "team": 2
        },
        "model": "sports.teammember",
        "pk": 2
    },
    {
        "fields": {
            "departed": null,
            "joined": "2002-07-01",
            "person": 4,
            "role": "C",
            "team": 2
        },
        "model": "sports.teammember",
        "pk": 3
    },
    {
        "fields": {
            "date": "1937-11-01",
            "precision": 0
        },
        "model": "dates.date",
        "pk": 1
    },
    {
        "fields": {
            "date": "1891-08-01",
            "precision": 1
        },
        "model": "dates.date",
        "pk": 2
    },
    {
        "fields": {
            "date": "1975-11-11",
            "precision": 2
        },
        "model": "dates.date",
        "pk": 3
    },
    {
        "fields": {
            "date": "1940-04-05",
            "precision": 3
        },
        "model": "dates.date",
        "pk": 4
    },
    {
        "fields": {
            "date": "1000-01-01",
            "precision": 4
        },
        "model": "dates.date",
        "pk": 5
    },
    {
        "fields": {
            "date": "0101-01-01",
            "precision": 4
        },
        "model": "dates.date",
        "pk": 6
    },
    {
        "fields": {
            "date": "0400-01-01",
            "precision": 4
        },
        "model": "dates.date",
        "pk": 7
    },
    {
        "fields": {
            "date": "1201-02-02",
            "precision": 4
        },
        "model": "dates.date",
        "pk": 8
    },
    {
        "fields": {
            "date": "1752-06-30",
            "precision": 3
        },
        "model": "dates.date",
        "pk": 9
    },
    {
        "fields": {
            "date": "1905-01-01",
            "precision": 3
        },
        "model": "dates.date",
        "pk": 10
    },
    {
        "fields": {
            "date": "2010-09-08",
            "precision": 0
        },
        "model": "dates.date",
        "pk": 11
    },
    {
        "fields": {
            "date": "1201-02-02",
            "precision": 4
        },
        "model": "dates.date",
        "pk": 12
    },
    {
        "fields": {
            "date": "1905-01-01",
            "precision": 3
        },
        "model": "dates.date",
        "pk": 13
    },
    {
        "fields": {
            "end": 7,
            "start": 6
        },
        "model": "dates.daterange",
        "pk": 1
    },
    {
        "fields": {
            "end": 9,
            "start": 8
        },
        "model": "dates.daterange",
        "pk": 2
    },
    {
        "fields": {
            "end": 11,
            "start": 10
        },
        "model": "dates.daterange",
        "pk": 3
    },
    {
        "fields": {
            "end": null,
            "start": 12
        },
        "model": "dates.daterange",
        "pk": 4
    },
    {
        "fields": {
            "end": null,
            "start": 13
        },
        "model": "dates.daterange",
        "pk": 5
    }
]
