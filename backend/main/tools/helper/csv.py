# -*- coding: utf-8 -*-
"""
field_verification verifies the contents in each of the fields input in the csv
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
from io import StringIO
from itertools import islice
import functools
import codecs

from .validation import *


def parse_csv(data, dialect=csv.excel, **kwargs):
    """@todo: Docstring for parse_csv.

    :data: string with csv data
    :returns: iterator returning lists

    """
    assert isinstance(data, str)
    for line in newline.split(data):
        try:
            reader = csv.reader(StringIO(line), dialect=dialect, **kwargs)
            for row in reader:
                row = [cell.strip() for cell in row]
                yield [cell.decode('latin-1').encode("utf-8") for cell in row]
        except UnicodeDecodeError:
            pass


def read_csv(data, dialect=csv.excel, **kwargs):
    """@todo: Docstring for read_csv.

    :data: string with csv data
    :returns: list of lists the CSV data

    """
    rows = parse_csv(data, dialect, **kwargs)
    rows = islice(rows, 50000)
    # remove empty rows
    rows = [r for r in rows if r]
    return rows


def process_base_row(node_properties):
    """
    :param node_properties:
    :return:
    """
    row_errors = []
    qr, qr_err = verify_batch_qr(node_properties['qr'])
    printed, printed_err = verify_batch_printed(node_properties['printed'])
    nfc, nfc_err = verify_batch_nfc(node_properties['nfc'])
    uhf, uhf_err = verify_batch_uhf(node_properties['uhf'])

    no_node_error = len(qr_err + printed_err + nfc_err + uhf_err) == 0
    if no_node_error is False:
        node_pairs = [
            ('qr', qr_err),
            ('printed', printed_err),
            ('nfc', nfc_err),
            ('uhf', uhf_err),
        ]
        node_errors = get_errors(node_pairs, node_properties, ['qr', 'printed', 'nfc', 'uhf'],
                                 ['QR', 'Printed', 'NFC', 'UHF'])
        row_errors += node_errors
    else:
        node_properties[qr] = qr
        node_properties[printed] = printed
        node_properties[nfc] = nfc
        node_properties[uhf] = uhf

    return node_properties, row_errors


def process_row(bot_row, csv_header):
    """
    :param bot_row:
    :param csv_header:
    :return:
    """
    # Initialize return variables
    node_data = dict()
    row_errors = []

    (node_properties, row_err_msg) = verify_row(bot_row, csv_header)
    if len(row_err_msg) == 0:
        (node_data, row_errors) = process_base_row(node_properties)
    else:
        row_errors += [FieldError('row formatting', None, row_err_msg)]
    return node_data, row_errors


def parse_csv_data(csv_data, csv_header):
    """
    :param csv_data:
    :param csv_header:
    :return:
    """
    file_header = csv_data[0]

    csv_data = csv_data[1:]
    file_header[0] = ''.join([x for x in file_header[0] if ord(x) < 128])
    (header_valid, wrong_headers) = verify_header(file_header, csv_header)
    if header_valid:
        data_and_errors = map(functools.partial(process_row, csv_header=csv_header), csv_data)
        node_list = [_item[0] for _item in data_and_errors]
        error_messages = [RowError(_idx + 2, _errs[1]) for (_idx, _errs) in enumerate(data_and_errors)]
    else:
        node_list = []
        csv_header_err = 'CSV file header does not match template. Please verify your ' \
                         'template is accurate and up to date. \n\nExpected header is {}. \n\nThe following headers ' \
                         'are wrong: {}\n'.format(csv_header, wrong_headers)
        error_messages = \
            [RowError(None, [FieldError('csv itself', None,
                                        csv_header_err.format(", ".join(csv_header),
                                                              ", ".join(wrong_headers)))])]
    return node_list, error_messages


def get_errors(field_pairs_arr, node_properties, props, csv_header):
    """get_errors returns an array of pairs of field labels and the errors encountered
    when processing them"""

    fc = dict((props[j], csv_header[j]) for j in range(len(props)))
    return [FieldError(fc[field_label], node_properties[field_label], field_error)
            for (field_label, field_error) in
            field_pairs_arr if len(field_error) > 0]
