# -*- coding: utf-8 -*-
"""
"""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function

from main.core import models as m

modelsmap = {
    m.User: [
        'id',
        'username',
        'password',
        'first_name',
        'last_name',
        'email',
        'phone',
    ],
}
