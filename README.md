Amazon-SQS-Tool
===============

Python tool for manipulation queues on Amazon SQS using JSON format messages.

Requirements
------------

- Python 2.7.x
- simplejson
- boto

Issue the following command to install all of requirements:
```
pip install -r amazonsqs.reqs
```

Instructions
------------

- Copy ``config.ini.bkp`` to ``config.ini``.
- Set values on ``queue``, ``access_key_id`` and ``secret_access_key`` options on ``config.ini``.
- Run ``python main.py``.
