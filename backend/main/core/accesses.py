# -*- coding: utf-8 -*-
"""
"""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function

from datetime import datetime
from main.core import models as m
from .corebase import CoreBase


class Accesses(CoreBase):
    """Docstring for Accesses. """

    def new_access(self, user_id, place_id, access_type, is_active):
        access = m.Access()
        access.user_id = user_id
        access.place_id = place_id
        access.access_type = access_type
        access.is_active = is_active
        self.session.add(access)
        self.session.flush()
        return access

    def add_multicode(self, user_id, place_id, access_type, is_active, codes_data):
        access = self.new_access(user_id, place_id, access_type, is_active)
        for code_data in codes_data:
            self.create_new_code(code_data['code'], code_data['code_type'], access.id)
        access.user.update_time = datetime.utcnow()
        return access

    def create_new_code(self, code, code_type, access_id):
        access_code = m.AccessCode(
            code=code,
            code_type=code_type,
            access_id=access_id
        )
        self.session.add(access_code)
        self.session.flush()
        return access_code

    def affiliate_access(self, user_id, place_id, access_type, batch_card):
        access = self.new_access(user_id, place_id, access_type, True)

        if batch_card.qr:
            self.create_new_code(batch_card.qr, m.AccessCode.QR_CARD, access.id)
        if batch_card.printed:
            self.create_new_code(batch_card.printed, m.AccessCode.PRINTED_CARD, access.id)
        if batch_card.uhf:
            self.create_new_code(batch_card.uhf, m.AccessCode.UHF_CARD, access.id)
        if batch_card.nfc:
            self.create_new_code(batch_card.nfc, m.AccessCode.NFC_CARD, access.id)

        return access
