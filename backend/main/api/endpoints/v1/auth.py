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


@api.post('/auth/signup', schema={
    'username': {
        'type': 'string',
        'empty': False,
        'required': True,
    },
    'password': {
        'type': 'string',
        'empty': False,
        'required': True,
    },
    'first_name': {
        'type': 'string',
        'empty': False,
        'required': True,
    },
    'last_name': {
        'type': 'string',
        'empty': False,
        'required': True,
    },
    'email': {
        'type': 'string',
        'empty': False,
        'required': True,
    },
    'phone': {
        'type': 'string',
        'empty': False,
        'required': True,
    },
})
@api.doc(""" User SignUp """)
def post_signup():
    return


@api.post('/auth/login', schema={
    'username': {
        'type': 'string',
        'empty': False,
        'required': True,
    },
    'password': {
        'type': 'string',
        'empty': False,
        'required': True,
    }
})
@api.doc(""" User Login """)
def post_login():
    return


@api.delete('/auth/logout')
@api.doc(""" Logout current user """)
@auth.required
def delete_auth_login():
    token = g.s.query(m.AuthToken).get(g.current_token_id)
    g.s.delete(token)
    return
