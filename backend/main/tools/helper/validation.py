# -*- coding: utf-8 -*-
""""""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import re
from collections import namedtuple

newline = re.compile('\n|\r|\r\n', flags=re.MULTILINE)

RowError = namedtuple('bot_schema', ['row_num', 'err_msgs'])
FieldError = namedtuple('field_error', ['field_name', 'field_entry', 'error_description'])


def verify_header(file_header, csv_header):
    """
    Ensure that the input header has the same columns as the
    template header.

    Returns:
    (bool, list)     a tuple of (valid, wrong_headers). If valid
                     is True, wrong_headers is an empty list.
    """
    wrong_headers = []
    is_valid = True

    if len(file_header) != len(csv_header):
        return False, file_header

    for index in range(len(csv_header)):
        if file_header[index].lower() != csv_header[index]:
            wrong_headers.append(file_header[index])
            is_valid = False

    return is_valid, wrong_headers


def verify_row(bot_row, header_title):
    """
    :param bot_row:
    :param header_title:
    :return:
    """
    err_msg = str()
    if len(header_title) != len(bot_row):
        node_properties = dict()
        err_msg = 'Row of csv is improperly formatted; namely the template expects ' \
                  'more fields ("columns") than were submitted.'
    else:
        node_properties = dict(zip(header_title, bot_row))
    return node_properties, err_msg


def verify_batch_qr(qr):
    """
    :param qr:
    :return:
    """
    err_msg = str()
    qr = qr.replace('-', '')
    if len(qr) != 20 and len(qr) != 10:
        err_msg = "The length of qr is {}, the length of qr must be 10, 20.".format(len(qr))
    return qr, err_msg


def verify_batch_printed(printed):
    """
    :param printed:
    :return:
    """
    err_msg = str()
    printed = printed.replace('-', '')
    if len(printed) != 6 and len(printed) != 8 and len(printed) != 9:
        err_msg = "The length of printed is {}, the length of printed must be 6, 8, 9.".format(len(printed))
    return printed, err_msg


def verify_batch_nfc(nfc):
    """
    :param nfc:
    :return:
    """
    err_msg = str()
    nfc = nfc.replace('-', '')
    if len(nfc) != 14:
        err_msg = "The length of nfc is {}, the length of nfc must be 14.".format(len(nfc))
    return nfc, err_msg


def verify_batch_uhf(uhf):
    """
    :param uhf:
    :return:
    """
    err_msg = str()
    uhf = uhf.replace('-', '')
    if len(uhf) != 24:
        err_msg = "The length of uhf is {}, the length of uhf must be 24.".format(len(uhf))
    return uhf, err_msg
