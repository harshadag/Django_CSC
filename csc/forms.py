#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-

# python/django imports
from django import forms

# project imports


class CSCForm(forms.Form):
    """ CSC- Country,State,City Form """

    country = forms.ChoiceField(label="Countries:", choices=[('in', 'India')],
                                widget=forms.Select(attrs={'class': 'common_dropdown'}))
    state = forms.ChoiceField(label="States:", choices=[('in', 'India')],
                              widget=forms.Select(attrs={'class': 'common_dropdown'}))
    city = forms.ChoiceField(label="Cities:", choices=[('in', 'India')],
                             widget=forms.Select(attrs={'class': 'common_dropdown'}))
