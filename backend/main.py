# -*- coding: utf-8 -*-
"""
"""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function

import os
from main.api.app import init_app
import main.api.endpoints.v1
from main.core.coreconf import CoreConf

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@127.0.0.1/pa?charset=utf8mb4'
core_conf = CoreConf()

app = init_app({
    'SECRET_KEY': b'I.\x05\xe6i\xd7\x10\x07\x02\xe7i\x89\xac\xd2nJ\x19\xdd\xbd\xb0',
    'SQLALCHEMY_DATABASE_URI': SQLALCHEMY_DATABASE_URI,
    'CORE_CONF': core_conf
})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
