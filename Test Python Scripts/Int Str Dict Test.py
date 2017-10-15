#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 15:47:39 2017

@author: maxjnorman
"""

def period_transform(period):
        period_dict = {
            'DAILY': 0,
            'WEEKLY': 1,
            'MONTHLY': 2,
            'YEARLY': 3,
            '0': 'Daily',
            '1': 'Weekly',
            '2': 'Monthly',
            '3': 'Daily',
        }
        if str(period).upper() in period_dict.keys():
            return period_dict[str(period).upper()]
        else:
            return 2

print(period_transform('f'))