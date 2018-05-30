import os
import sys
import hmac
import time
import base64
import hashlib

timestamp = sys.argv[1]
method = sys.argv[2]
route = sys.argv[3]

api_secret = os.environ['BITBUTTER_API_SECRET']
partnership_id = os.environ['BITBUTTER_PARTNERSHIP_ID']

message = str(timestamp) + method + route
message = message.encode('ascii')

hmac_key = base64.b64decode(api_secret)
signature = hmac.new(hmac_key, message, hashlib.sha256)
signature_b64 = base64.b64encode(signature.digest()).decode('utf-8')

print(signature_b64)
