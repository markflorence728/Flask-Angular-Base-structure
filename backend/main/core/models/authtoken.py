# -*- coding: utf-8 -*-
"""
"""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function

from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class AuthToken(Base):
    """Docstring for AuthToken. """

    __tablename__ = 'auth_tokens'

    id = Column(Integer, primary_key=True, autoincrement=True)
    expire_time = Column(DateTime, nullable=False)
    update_time = Column(DateTime, nullable=False, onupdate=datetime.utcnow, default=datetime.utcnow)
    create_time = Column(DateTime, nullable=False, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
