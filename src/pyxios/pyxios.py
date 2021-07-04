from typing import *

import requests


class Pyxios:
    def __init__(
            self,
            base_url: str,
            params: Dict = None,
            data: Dict = None,
            json: Dict = None,
            headers: Dict = None,
            cookies: Dict = None,
            files: Dict = None,
            timeout: Union[float, Tuple] = None,
            allow_redirects: bool = True,
            proxies: Dict = None,
    ):
        self.base_url = base_url
        self.params = params or {}
        self.data = data or {}
        self.json = json or {}
        self.headers = headers or {}
        self.cookies = cookies or {}
        self.headers = headers or {}
        self.files = files or {}
        self.timeout = timeout
        self.allow_redirects = allow_redirects
        self.proxies = proxies or {}

    @property
    def _dict_attributes(self):
        return [
            'params',
            'data',
            'json',
            'headers',
            'cookies',
            'headers',
            'files',
            'proxies',
        ]

    def get(self, url: str = '', **kwargs) -> requests.Response:
        return self._make_request(url, 'GET', **kwargs)

    def post(self, url: str = '', **kwargs) -> requests.Response:
        return self._make_request(url, 'POST', **kwargs)

    def head(self, url: str = '', **kwargs) -> requests.Response:
        return self._make_request(url, 'HEAD', **kwargs)

    def put(self, url: str = '', **kwargs) -> requests.Response:
        return self._make_request(url, 'PUT', **kwargs)

    def patch(self, url: str = '', **kwargs) -> requests.Response:
        return self._make_request(url, 'PATCH', **kwargs)

    def options(self, url: str = '', **kwargs) -> requests.Response:
        return self._make_request(url, 'OPTIONS', **kwargs)

    def delete(self, url: str = '', **kwargs) -> requests.Response:
        return self._make_request(url, 'DELETE', **kwargs)

    def _make_request(
            self,
            url: str,
            method: str,
            **kwargs,
    ) -> requests.Response:
        url = self._make_url(url)
        kwargs = self._populate_default_kwargs(**kwargs)

        print(kwargs)

        return requests.request(url=url, method=method, **kwargs)

    def _make_url(self, url: str) -> str:
        return f'{self.base_url}{url}'

    def _populate_default_kwargs(self, **kwargs) -> Dict:

        for attr in self._dict_attributes:
            if kwargs.get(attr) is None:
                kwargs[attr] = getattr(self, attr)
                continue

            kwargs[attr].update(getattr(self, attr))

        if kwargs.get('timeout') is not None:
            kwargs['timeout'] = self.timeout

        if kwargs.get('allow_redirect') is not None:
            kwargs['allow_redirect'] = self.allow_redirects

        return kwargs
