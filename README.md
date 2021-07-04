# Pyxios

    Fusing Python's requests with Javascript's axios.

## Setup

Pyxios is a module that wraps `requests` methods in a single
instance, centralizing the settings of a given API. Let's use this 
https://nonrealapi.com as an example:

```python
from src.pyxios import Pyxios

non_real_api = Pyxios('https://nonrealapi.com/')

get_response = non_real_api.get()

post_response = non_real_api.post(json={'key': 'value'})
```

## Basic Usage

There's no need to provide the base url address and default values of 
headers, cookies, timeout and/or proxies. The Pyxios instance has on method 
for each HTTP operation, allowing clarity and agility in the integration 
with Restfull APIs.

```python
from src.pyxios import Pyxios

non_real_api = Pyxios(
    'https://nonrealapi.com/',
    headers={
        'x-api-key': '$PRIMARY_KEY',
    },
    timeout=10,
)

get_response = non_real_api.get('resource/1')

delete_response = non_real_api.delete('resource/1', )

# Is also possible to override/update values in each request
patch_response = non_real_api.patch(
    'resource/2',
    headers={
        'x-api-key': '$SECONDARY_KEY',
    },
    params={'key': 'value'},
)
```
