from __future__ import division
from __future__ import absolute_import
from __future__ import print_function

from flask import g
from main.api.app import api, auth


@api.get('/me')
@api.doc("""
Information about current user
""")
@auth.required
def get_me():
    """TODO: Docstring for get_me.
    :returns: TODO

    """
    return g.current_user
