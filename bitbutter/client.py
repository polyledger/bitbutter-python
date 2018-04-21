# coding: utf-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import json
import requests

from bitbutter.auth import HMACAuth
from bitbutter.compat import imap
from bitbutter.compat import quote
from bitbutter.compat import urljoin
from bitbutter.error import build_api_error


class Client(object):
    """ API Client for the Bitbutter API.

    Entry point for making requests to the Bitbutter API. Provides helper
    methods for API endpoints, as well as niceties around response
    verification and formatting.

    Any errors will be raised as exceptions. These exceptions will always
    be subclasses of `bitbutter.error.APIError`. HTTP-related errors will
    also be subclasses of `requests.HTTPError`.

    Ful API docs, including descriptions of each API and its parameters,
    are available here: https://docs.bitbutter.com.
    """

    def __init__(
        self,
        api_key,
        api_secret,
        base_uri,
        partnership_id=None,
        partner_id=None,
        user_id=None
    ):
        for key, value in locals().items():
            if not value and key != 'partner_id' and key != 'user_id' \
                    and key != 'partnership_id':
                    raise ValueError

        self.user_id = user_id
        self.partner_id = partner_id
        self.partnership_id = partnership_id
        self.BASE_API_URI = base_uri

        # Set up a requests session for interacting with the API.
        self.session = requests.session()
        self.session.auth = HMACAuth(api_key, api_secret)
        self.session.headers.update({
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'User-Agent': 'Bitbutter/python/1.0'
        })

        if self.user_id:
            self.session.headers.update({'BB-USER-ID': self.user_id})
        if self.partner_id:
            self.session.headers.update({'BB-PARTNER-ID': self.partner_id})

    def _request(self, method, *path, **kwargs):
        """Internal helper for creating HTTP requests to the Bitbutter API.

        Raises an APIError if the response is not 20X. Otherwise, returns the
        response object. Not intended for direct use by API consumers.
        """
        uri = urljoin(self.BASE_API_URI, '/'.join(imap(quote, path)))
        data = kwargs.get('data', None)
        if data and isinstance(data, dict):
            kwargs['data'] = json.dumps(data, separators=(',', ':'))
        response = getattr(self.session, method)(uri, **kwargs)
        return self._handle_response(response)

    def _handle_response(self, response):
        """Internal helper for handling API responses from the Bitbutter.

        Raises the appropriate exceptions when necessary; otherwise, returns
        the response.
        """
        if not str(response.status_code).startswith('2'):
            raise build_api_error(response)
        return response

    def _get(self, *args, **kwargs):
        return self._request('get', *args, **kwargs)

    def _post(self, *args, **kwargs):
        return self._request('post', *args, **kwargs)

    def _delete(self, *args, **kwargs):
        return self._request('delete', *args, **kwargs)

    """ Partner API """

    def create_user(self):
        path = ['v1', 'partnerships', self.partnership_id, 'users']
        response = self._post(*path)
        return response

    def delete_user(self, user_id):
        path = ['v1', 'users', user_id]
        response = self._delete(*path)
        return response

    def get_all_users(self):
        path = ['v1', 'partnerships', self.partnership_id, 'users']
        response = self._get(*path)
        return response

    """ User API """

    def get_user_balance(self):
        path = ['v1', 'users', self.user_id, 'balances']
        response = self._get(*path)
        return response

    def get_user_ledger(self):
        path = ['v1', 'users', self.user_id, 'ledger']
        response = self._get(*path)
        return response

    def connect_exchange(self, data):
        path = ['v1', 'connected-exchanges']
        response = self._post(*path, data=data)
        return response

    def get_all_exchanges(self):
        path = ['v1', 'exchanges']
        response = self._get(*path)
        return response

    def get_user_connected_exchanges(self):
        path = ['v1', 'users', self.user_id, 'connected-exchanges']
        response = self._get(*path)
        return response

    def get_connected_exchange_balances(self, connected_exchange_id):
        path = ['v1', 'connected-exchanges', connected_exchange_id, 'balances']
        response = self._get(*path)
        return response

    def get_connected_exchange_ledger(self, connected_exchange_id):
        path = ['v1', 'connected-exchanges', connected_exchange_id, 'ledger']
        response = self._get(*path)
        return response

    def get_connected_exchange_trades(self, connected_exchange_id):
        path = ['v1', 'connected-exchanges', connected_exchange_id, 'trades']
        response = self._get(*path)
        return response

    def get_connected_exchange_transfers(self, connected_exchange_id):
        path = ['v1', 'connected-exchanges', connected_exchange_id, 'transfers']
        response = self._get(*path)
        return response

    def sync_connected_exchange(self, connected_exchange_id):
        path = ['v1', 'connected-exchanges', connected_exchange_id, 'sync']
        response = self._get(*path)
        return response

    def disconnect_exchange(self, connected_exchange_id):
        path = ['v1', 'connected-exchanges', connected_exchange_id]
        response = self._delete(*path)
        return response

    def get_all_assets(self):
        path = ['v1', 'assets']
        response = self._get(*path)
        return response

    def connect_address(self, data):
        path = ['v1', 'connected-addresses']
        response = self._post(*path, data=data)
        return response

    def get_user_connected_addresses(self):
        path = ['v1', 'users', self.user_id, 'connected-addresses']
        response = self._get(*path)
        return response

    def get_connected_address_balances(self, connected_address_id):
        path = ['v1', 'connected-addresses', connected_address_id, 'balances']
        response = self._get(*path)
        return response

    def get_connected_address_ledger(self, connected_address_id):
        path = ['v1', 'connected-addresses', connected_address_id, 'ledger']
        response = self._get(*path)
        return response

    def sync_connected_address(self, connected_address_id):
        path = ['v1', 'connected-addresses', connected_address_id, 'sync']
        response = self._get(*path)
        return response

    def disconnect_address(self, connected_address_id):
        path = ['v1', 'connected-addresses', connected_address_id]
        response = self._delete(*path)
        return response
