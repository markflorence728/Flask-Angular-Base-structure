# -*- coding: utf-8 -*-
"""
"""
import StringIO
import codecs
import csv
import os
from random import SystemRandom

choice = SystemRandom().choice

from xlsxwriter import Workbook


def get_request_ip():
    """Return IP of client request"""
    return os.environ.get("REMOTE_ADDR")


def get_user_agent(request):
    """Return the browser info"""
    return request.headers.get('User-Agent')


def gen_code(symbols, size):
    """Function for generating protection code

        :symbols: @todo
        :size: @todo
        :returns: @todo

        """
    code = ''
    for _ in xrange(size):
        code += choice(symbols)
    return code


def stringify(value):
    if isinstance(value, unicode):
        return value
    elif value is None:
        return u''
    else:
        return unicode(value)


def gen_csv(data):
    """Create csv data representing csv file in memory

    :data: list of lists
    :returns: string with csv data

    """
    buf = StringIO.StringIO()
    buf.write(codecs.BOM_UTF8)
    writer = csv.writer(buf)
    for row in data:
        row = (stringify(v) for v in row)
        writer.writerow([s.encode('utf-8') for s in row])
    return buf.getvalue()


def gen_xlsx(data):
    buf = StringIO.StringIO()
    workbook = Workbook(buf, {'in_memory': True})
    sheet = workbook.add_worksheet()
    for i, row in enumerate(data):
        row = (stringify(v) for v in row)
        for j, val in enumerate(row):
            sheet.write(i, j, val)
    workbook.close()
    return buf.getvalue()
