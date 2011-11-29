import json

from django.conf import settings

import requests


class BasketException(Exception):
    pass


def subscribe(email, newsletters, **kwargs):
    kwargs.update(email=email, newsletters=newsletters)
    return _post('subscribe', kwargs)

def _url(path):
    return 'https://%s/news/%s/' % (settings.BASKET_URL, path)


def _post(path, data):
    return _parse_response(requests.post(_url(path), data=data))


def _get(path, data):
    return _parse_response(requests.get(_url(path), data=data))


def _parse_response(response):
    if response.error:
        raise BasketException('Error connecting to %s: %s. Ensure that '
                              'BASKET_URL is configured correctly in your '
                              'settings file.' % (response.url, response.error))

    response_json = json.loads(response.content)
    if response_json.get('desc', None):
        raise BasketException(response_json['desc'])

    return response_json
