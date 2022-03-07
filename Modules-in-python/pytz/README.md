# pytz Module

Pytz brings the Olson tz database into Python and thus supports almost all time zones | Not buit-in module

**Installation**

---

Python pytz module can be installed in the given way

Using command line : 

`pip install pytz`

Using tarball, run the following command as an administrative user :

`python setup.py install`

Using setuptools, the latest version will be downloaded for you from the Python package index :

`easy_install --upgrade pytz`

**Fetching time of a given time-zone :**

---

The pytz.timezone() returns the timezone object by the name. And, the datetime.datetime.now() returns the date-time of that particular time-zone
```py
import datetime
import pytz

utc = pytz.timezone('US/Pacific')

print(datetime.datetime.now(utc))
```