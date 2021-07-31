# -*- coding: utf-8 -*-
"""
"""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function

from .corebase import CoreBase
from main.core import models as m


class Logs(CoreBase):
    """Docstring for Logs. """

    def add_multi_logs(self, logs_data):
        logs = []
        for log_data in logs_data:
            log = self.session.query(m.Log).get(log_data['id'])
            if not log:
                log = m.Log(
                    id=log_data['id'],
                    checkpoint_id=log_data['checkpoint_id'],
                    code_type=log_data['code_type'],
                    code=log_data['code'],
                    create_time=log_data['create_time'],
                )
            props = ['code_type', 'code', 'create_time']
            for prop in props:
                setattr(log, prop, log_data[prop])
            # setattr(log, 'checkpoint_id', checkpoint.id)
            logs.append(log)

        self.session.add_all(logs)
        self.session.flush()

        return logs
