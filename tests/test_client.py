# coding: utf-8

"""
To run all tests:
```
$ make tests
```

For a single test:
```
$ nosetests tests.test_client:TestClient.create_user \
    --nocapture --nologcapture
```
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import six
import unittest2

import httpretty

from bitbutter.client import Client
from tests.helpers import mock_response


# Dummy base64 API key values for use in tests
partner_api_key = 'ZmFrZV9hcGlfa2V5'
partner_secret = 'ZmFrZV9hcGlfc2VjcmV0'
partnership_id = 'ZmFrZV9pZAas'
partner_id = 'ZmFrZV9pZAas'
user_id = 'dXNlcl9pZAas'
user_api_key = 'ZmFrZV9hcGlfa2V5'
user_secret = 'ZmFrZV9hcGlfc2VjcmV0'
exchange_id = 'dXNlcl9pZAas'
base_uri = 'https://api.bitbutter.com'

# Partner routes
create_user_route = '/v1/partnerships/' + partnership_id + '/users'
delete_user_route = '/v1/users/' + user_id
get_all_users_route = '/v1/partnerships/' + partnership_id + '/users'

# User routes
get_all_exchanges_route = '/v1/exchanges'
connect_exchange_route = '/v1/connected-exchanges'
get_user_balance_route = '/v1/users/' + user_id + '/balances'
get_user_connected_exchanges_route = ('/v1/users/' + user_id +
                                      '/connected-exchanges')

mock_item = {'key1': 'val1', 'key2': 'val2'}
mock_collection = [mock_item, mock_item]


class TestClient(unittest2.TestCase):
    def test_init(self):
        client = Client(partner_api_key, partner_secret, base_uri=base_uri)
        assert isinstance(client, Client)

    def test_key_and_secret_required(self):
        with self.assertRaises(ValueError):
            Client(None, partner_secret, base_uri, partner_id=partner_id)
        with self.assertRaises(ValueError):
            Client(partner_api_key, None, base_uri, partner_id=partner_id)

    @mock_response(httpretty.GET, 'test', {})
    def test_auth_succeeds_with_bytes_and_unicode(self):
        self.assertIsInstance(partner_api_key, six.text_type)  # Unicode
        self.assertIsInstance(partner_secret, six.text_type)  # Unicode

        client = Client(partner_api_key, partner_secret, base_uri,
                        partner_id=partner_id)
        self.assertEqual(client._get('test').status_code, 200)

        api_key_bytes = partner_api_key.encode('utf-8')
        api_secret_bytes = partner_secret.encode('utf-8')
        self.assertIsInstance(api_key_bytes, six.binary_type)  # Bytes
        self.assertIsInstance(api_secret_bytes, six.binary_type)  # Bytes

        client = Client(partner_api_key, partner_secret, base_uri,
                        partner_id=partner_id)
        self.assertEqual(client._get('test').status_code, 200)

    @httpretty.activate
    def test_request_includes_auth_headers(self):
        client = Client(partner_api_key, partner_secret, base_uri,
                        partner_id=partner_id, partnership_id=partnership_id,
                        user_id=user_id)

        def server_response(request, uri, response_headers):
            headers = ['BB-ACCESS-KEY', 'BB-ACCESS-SIGN', 'BB-TIMESTAMP',
                       'Accept', 'Content-Type', 'User-Agent']
            for header in headers:
                self.assertIn(header, request.headers)
                self.assertNotEqual(request.headers[header], '')

            if 'BB-PARTNER-ID' in request.headers:
                return 200, response_headers, '{}'

            if 'BB-USER-ID' in request.headers:
                return 200, response_headers, '{}'

            return 400, response_headers, '{}'

        # Test a partner route
        url = base_uri + get_all_users_route
        httpretty.register_uri(httpretty.GET, url, server_response)
        response = client.get_all_users()
        self.assertEqual(response.status_code, 200)

        # Test a user route
        url = base_uri + get_user_balance_route
        httpretty.register_uri(httpretty.GET, url, server_response)
        response = client.get_user_balance()
        self.assertEqual(response.status_code, 200)

    """ Partner routes """

    @mock_response(
        method=httpretty.POST,
        uri=create_user_route,
        data=mock_item)
    def test_create_user(self):
        client = Client(partner_api_key, partner_secret, base_uri,
                        partner_id=partner_id, partnership_id=partnership_id)
        response = client.create_user()
        self.assertEqual(response.json()['data'], mock_item)

    @mock_response(
        method=httpretty.DELETE,
        uri=delete_user_route,
        data=mock_item)
    def test_delete_user(self):
        client = Client(partner_api_key, partner_secret, base_uri,
                        partner_id=partner_id, partnership_id=partnership_id)
        response = client.delete_user(user_id)
        self.assertEqual(response.json()['data'], mock_item)

    @mock_response(
        method=httpretty.GET,
        uri=get_all_users_route,
        data=mock_collection)
    def test_get_all_users(self):
        client = Client(partner_api_key, partner_secret, base_uri,
                        partner_id=partner_id, partnership_id=partnership_id)
        response = client.get_all_users()
        self.assertEqual(response.json()['data'], mock_collection)

    """ User routes """

    @mock_response(
        method=httpretty.GET,
        uri=get_all_exchanges_route,
        data=mock_collection)
    def test_get_all_exchanges(self):
        client = Client(user_api_key, user_secret, base_uri, user_id=user_id)
        response = client.get_all_exchanges()
        self.assertEqual(response.json()['data'], mock_collection)

    @mock_response(
        method=httpretty.POST,
        uri=connect_exchange_route,
        data=mock_item)
    def test_connect_exchange(self):
        client = Client(user_api_key, user_secret, base_uri, user_id=user_id)
        body = {
            'credentials': {
                'api_key': user_api_key,
                'secret': user_secret
            },
            'exchange_id': exchange_id
        }
        response = client.connect_exchange(body)
        self.assertEqual(response.json()['data'], mock_item)

    @mock_response(
        method=httpretty.GET,
        uri=get_user_connected_exchanges_route,
        data=mock_collection)
    def test_get_user_connected_exchanges(self):
        client = Client(user_api_key, user_secret, base_uri, user_id=user_id)
        response = client.get_user_connected_exchanges()
        self.assertEqual(response.json()['data'], mock_collection)
