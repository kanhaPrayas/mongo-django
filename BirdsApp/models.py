from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Birds(object):
    def __init__(self, id, name, family, continents):
        self.id = id
        self.name = name
        self.family = family
        self.continents = continents