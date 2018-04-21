# Welcome to Chainbridge

For source code visit the [repository](https://github.com/polyledger/chainbridge) on GitHub.

## Usage

### Partner Routes

First create a partner client

```python
import os
from bitbutter.client import Client

partner_api_key = os.environ['BITBUTTER_API_KEY']
partner_secret = os.environ['BITBUTTER_API_SECRET']
base_uri = os.environ['BITBUTTER_BASE_URI']
partner_id = os.environ['BITBUTTER_PARTNER_ID']
partnership_id = os.environ['BITBUTTER_PARTNERSHIP_ID']

partner_client = Client(partner_api_key, partner_secret, base_uri, partner_id=partner_id, partnership_id=partnership_id)
```

#### Create user

```python
partner_client.create_user()
```

#### Delete user

```python
partner_client.delete_user(user_id)
```

#### Get all users

```python
partner_client.get_all_users()
```

### User Routes

First create a user client

```python
import os
from bitbutter.client import Client

partner_api_key = os.environ['BITBUTTER_API_KEY']
partner_secret = os.environ['BITBUTTER_API_SECRET']
base_uri = os.environ['BITBUTTER_BASE_URI']
partner_id = os.environ['BITBUTTER_PARTNER_ID']
partnership_id = os.environ['BITBUTTER_PARTNERSHIP_ID']

user_id = 'some user id'

user_client = Client(partner_api_key, partner_secret, base_uri, partner_id=partner_id, partnership_id=partnership_id, user_id=user_id)
```

#### Get user balance

#### Get user ledger

#### Connect exchange

```python
params = {
    'credentials': {
        'api_key': user_api_key,
        'secret': user_secret
    },
    'exchange_id': exchange_id
}

user_client.connect_exchange(params=params)
```

#### Get all exchanges

```python
user_client.get_all_exchanges()
```

#### Get user connected exchanges

#### Get connected exchange balances

#### Get connected exchange ledger

#### Get connected exchange trades

#### Get connected exchange transfers

#### Sync connected exchange

#### Disconnect exchange

#### Get all assets

#### Connect address

#### Get user connected addresses

#### Get connected address balances

#### Get connected address ledger

#### Sync connected address

#### Disconnect address
