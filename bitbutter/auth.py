# coding: utf-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import hmac
import time
import base64
import hashlib

from requests.auth import AuthBase
from requests.utils import to_native_string


class HMACAuth(AuthBase):
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret

    def __call__(self, request):
        timestamp = int(time.time() * 1000)
        message = str(timestamp) + request.method + request.path_url + \
            (request.body or '')
        message = message.encode('ascii')

        hmac_key = base64.b64decode(self.api_secret)
        signature = hmac.new(hmac_key, message, hashlib.sha256)
        signature_b64 = base64.b64encode(signature.digest()).decode('utf-8')
        request.headers.update({
            to_native_string('BB-ACCESS-KEY'): self.api_key,
            to_native_string('BB-ACCESS-SIGN'): signature_b64,
            to_native_string('BB-TIMESTAMP'): timestamp,
        })
        return request
