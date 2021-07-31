# -*- coding: utf-8 -*-
"""
"""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function

from datetime import datetime
from sqlalchemy import Column, Integer, String, Unicode, DateTime, Boolean, ForeignKey, Enum
from sqlalchemy.orm import relationship

from .base import Base


class User(Base):
    """Docstring for User. """

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(Unicode(45), unique=True, nullable=True, index=True)
    first_name = Column(Unicode(45), nullable=True)
    last_name = Column(Unicode(45), nullable=True)
    email = Column(Unicode(45), unique=True, nullable=True, index=True)
    phone = Column(Unicode(45), unique=True, nullable=True, index=True)
    update_time = Column(DateTime, nullable=False, onupdate=datetime.utcnow, default=datetime.utcnow)
    create_time = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return 'User({})'.format(self.id)
