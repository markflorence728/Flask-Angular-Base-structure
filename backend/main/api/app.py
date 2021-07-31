# -*- coding: utf-8 -*-
"""
"""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function

from flask import Flask, g

from flask_api import Api, errors
from flask_auth import Auth
from flask_sa import SA

from main.core import Core, models as m
from main.api.encoder import encode

app = Flask('main.api')
api = Api(app, version='v1.0', encode=encode)
auth = Auth()
sa = SA()

app.config['MAX_PAGE_SIZE'] = 50
app.config['CORE_CONF'] = None
app.config[SA.SQLALCHEMY_DATABASE_URI] = 'mysql+pymysql://root:password@127.0.0.1/pa?charset=utf8mb4'


def init_app(config):
    app.config.update(config)
    auth.init_app(app)
    sa.init_app(app)
    return app


@app.before_request
def before_request():
    g.core = Core(sa.get_session(), app.config['CORE_CONF'])


@auth.set_user_getter
def get_user(token):
    """TODO: Docstring for get_user.

    :token: TODO
    :returns: TODO

    """
    if not g.s.query(m.AuthToken).get(token['tid']):
        raise errors.unauthorized_error
    user = g.s.query(m.User).get(token['sub'])
    if not user:
        raise errors.unauthorized_error
    # if not user.is_active:
    #     raise errors.unauthorized_error
    return user

# @auth.set_roles_getter
# def get_roles(user):
#     """TODO: Docstring for get_roles.
#
#     :user: TODO
#     :returns: TODO
#
#     """
#     return [r.name for r in user.roles]
