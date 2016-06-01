import sys

try:
    import secrets
except ImportError as e:
    print('No "secrets.py" file exists. Put your API token in this file, please and thank you.')
    sys.exit(-1)

CONSUMER_KEY = secrets.CONSUMER_KEY
CONSUMER_SECRET = secrets.CONSUMER_SECRET

ACCESS_TOKEN = secrets.ACCESS_TOKEN
ACCESS_TOKEN_SECRET = secrets.ACCESS_TOKEN_SECRET
