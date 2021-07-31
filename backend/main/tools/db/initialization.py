# -*- coding: utf-8 -*-
"""
"""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function

from sqlalchemy import create_engine
from main.core import models as m
from main.core.models.base import Base
from main.core.roles import ROLES


def init_db(db_url, echo=False):
    engine = create_engine(db_url, echo=echo)
    Base.metadata.create_all(engine)


def create_roles(session):
    for name in ROLES:
        if not session.query(m.GlobalRole).filter(m.GlobalRole.name == name).first():
            role = m.GlobalRole(name=name)
            session.add(role)
            session.flush()
    session.commit()
