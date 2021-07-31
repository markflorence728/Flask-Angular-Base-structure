from flask import g
from flask_api import errors
from random import SystemRandom
from werkzeug._compat import range_type

_sys_rng = SystemRandom()
GEN_NUMBERS = '0123456789'


def update_if_set(item, fields, ignore_fields=[]):
    for name in fields:
        if name in g.api.json and name not in ignore_fields:
            setattr(item, name, g.api.json[name])
    return item


def get_or_not_found(Model, model_id):
    item = g.s.query(Model).get(model_id)
    if not item:
        raise errors.not_found_error
    return item


def get_or_bad(Model, model_id):
    item = g.s.query(Model).get(model_id)
    if not item:
        raise errors.bad_request_error
    return item


def generate_verification(length):
    if length <= 0:
        raise ValueError('verification length must be positive')
    return ''.join(_sys_rng.choice(GEN_NUMBERS) for _ in range_type(length))
