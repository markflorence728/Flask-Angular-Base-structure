# -*- coding: utf-8 -*-
"""
"""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function

import unicodedata

from datetime import datetime, timedelta

from sqlalchemy.exc import IntegrityError
from .corebase import CoreBase
from main.core import models as m


def is_password_complex_enough(password):
    if len(password) < 6:
        return False
    return True


class Auth(CoreBase):
    """Docstring for Auth. """

    def facebook_login(self, facebook_id, email, first_name, last_name, photo_url):
        user = self.session.query(m.User).filter(m.User.facebook_id == facebook_id).first()
        if not user:
            user = m.User(
                facebook_id=facebook_id,
                email=email,
                email_verified=True,
                first_name=first_name,
                last_name=last_name,
                photo_url=photo_url,
            )
            self.session.add(user)
            self.session.flush()
        return user

    def email_login(self, email):
        user = self.session.query(m.User).filter(m.User.email == email).first()
        if not user:
            user = m.User(
                email=email,
                email_verified=True,
            )
            self.session.add(user)
            self.session.flush()
        return user

    def signup_email(self, email, password=None):
        user = m.User(email=email)
        if password:
            if not is_password_complex_enough(password):
                return None
            user.set_password(password)
        self.session.add(user)
        try:
            self.session.flush()
        except IntegrityError:
            self.session.rollback()
            return None
        return user

    def make_auth_token(self, user):
        """TODO: Docstring for make_auth_token.

        :user: TODO
        :returns: TODO

        """
        token = self.session.query(m.AuthToken).filter(m.AuthToken.user_id == user.id).first()
        if not token:
            token = m.AuthToken(
                expire_time=datetime.utcnow() + timedelta(seconds=self.conf.AUTH_TOKEN_EXPIRE_TIME),
                user_id=user.id
            )
            self.session.add(token)
            self.session.flush()
        else:
            token.expire_time = datetime.utcnow() + timedelta(seconds=self.conf.AUTH_TOKEN_EXPIRE_TIME)

        return token

    @staticmethod
    def set_password(user, password):
        if not is_password_complex_enough(password):
            return None
        user.set_password(password)
        return user
