# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 2018
Updated Feb 13,2018

The primary goal of this file is to demonstrate a simple python program to pull from GitHub API

@author: jbuonocore
"""

import requests
import json

r = requests.get('https://api.github.com/users/jbuonoco567/repos',auth=('jbuonoco567','Korae_67'))
print('User: jbuonoco')
print('Status Code: %d' % r.status_code)
print('The number of repositories is %d' % len(r.json()))

a = requests.get('https://api.github.com/repos/jbuonoco567/Triangle567/commits',auth=('jbuonoco567','Korae_67'))
print('Repository 1: Triangle567')
print('Status Code: %d' % a.status_code)
print('The number of commits is %d' % len(a.json()))

b = requests.get('https://api.github.com/repos/jbuonoco567/GitHubApi567/commits',auth=('jbuonoco567','Korae_67'))
print('Repository 2: GitHubApi567')
print('Status Code: %d' % b.status_code)
print('The number of commits is %d' % len(b.json()))