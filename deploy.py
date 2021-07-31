#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function

import os
import sys
import logging
import shutil
from argparse import ArgumentParser
from subprocess import check_call, CalledProcessError


_readme = """
"""
_readme = _readme.strip()
root = os.path.dirname(os.path.abspath(__file__))

logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
log = logging.getLogger('deploy')


def get_pip_path():
    path = sys.executable
    path = os.path.dirname(path)
    path = os.path.join(path, 'pip')
    return path


def get_conf():
    parser = ArgumentParser(description='', usage=_readme)
    parser.add_argument('--npm-install', action='store_true', help='Run "npm install" before deploying')
    parser.add_argument('--pip-install', action='store_true', help='Run "npm install" before deploying')
    parser.add_argument('--key', type=os.path.abspath, help='Path to service account key for authentication')
    parser.add_argument('--project', help='Project ID')
    return parser.parse_args()


def full_path(path):
    return os.path.join(root, path)


def main():
    conf = get_conf()
    log.info('Project root: %s', root)
    log.info('Build web frontend client')
    os.chdir(full_path('frontend'))

    if conf.npm_install:
        log.info('Installing npm modules')
        try:
            # at first run npm can return nonzero status code even if it
            # finished successfully, to avoid incorrect exception `npm install`
            # should be run two times
            check_call([
                'npm',
                'install'
            ])
        except CalledProcessError:
            pass
        check_call([
            'npm',
            'install'
        ])

    check_call([
        'ng',
        'build',
        '--prod',
        '--deploy-url',
        'static/'
    ])
    shutil.rmtree(full_path('backend/static'), ignore_errors=True)
    shutil.copytree(full_path('frontend/dist/browser'), full_path('backend/static'))

    if conf.pip_install:
        log.info('Installing pip packages')
        os.chdir(full_path('backend'))
        check_call([
            get_pip_path(),
            'install',
            '-r',
            'requirements.txt'
        ])

    log.info('Updating version information')
    os.chdir(root)
    with open(full_path('backend/version'), 'w') as f:
        check_call([
            'git',
            'rev-parse',
            'HEAD'
        ], stdout=f)

    log.info('Deploying app')
    if conf.key:
        log.info('Using key for authentication: %s', conf.key)
        check_call([
            'gcloud',
            'auth',
            'activate-service-account',
            '--key-file',
            conf.key
        ])
    if conf.project:
        log.info('Project ID: %s', conf.project)
        check_call([
            'gcloud',
            'config',
            'set',
            'project',
            conf.project
        ])
    os.chdir(full_path('backend'))

    check_call([
        'gcloud',
        'app',
        'deploy',
        'app.yaml',
        '-q',
        '--version',
        '1'
    ])
    log.info('Done :-)')


if __name__ == '__main__':
    main()
