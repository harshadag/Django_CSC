#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-

# python/django imports
from django.db import models

# project imports


class Country(models.Model):
    """ Country model """
    name = models.CharField("Country Name", max_length=100)
    code = models.CharField("Country Code", max_length=5)

    def __unicode__(self):
        """ unicode for country """
        return self.name


class State(models.Model):
    """ State model """
    country = models.ForeignKey(Country)
    name = models.CharField("State Name", max_length=100)
    code = models.CharField("State Code", max_length=5)

    def __unicode__(self):
        """ unicode for state """
        return self.name


class City(models.Model):
    """ City model """
    state = models.ForeignKey(State)
    name = models.CharField("City Name", max_length=100)
    code = models.CharField("City Code", max_length=5)

    def __unicode__(self):
        """ unicode for city """
        return self.name
