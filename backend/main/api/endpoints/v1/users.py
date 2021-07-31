from __future__ import division
from __future__ import absolute_import
from __future__ import print_function

from flask import g, current_app
from datetime import datetime

from flask_api import errors

from main.api import tools
from main.api.app import api, auth
from main.api.encoder import encode
from main.core import models as m


@api.put('/users/<user_id>', schema={
    'first_name': {
        'type': 'string',
        'nullable': True
    },
    'last_name': {
        'type': 'string',
        'nullable': True
    },
    'email': {
        'type': 'string',
        'nullable': True,
    },
    'phone': {
        'type': 'string',
        'nullable': True
    },
    'gender': {
        'type': 'string',
        'nullable': True
    },
    'birthday': {
        'type': 'string',
        'nullable': True
    },
    'zipcode': {
        'type': 'string',
        'nullable': True
    },
    'city': {
        'type': 'string',
        'nullable': True
    },
})
@api.doc(""" User Update Request """)
@auth.required
def put_user_update(user_id):
    user = tools.get_or_not_found(m.User, user_id)
    user = tools.update_if_set(user, g.api.schema.keys())
    return user
