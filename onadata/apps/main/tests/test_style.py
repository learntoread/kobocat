# coding: utf-8
from __future__ import unicode_literals, print_function, division, absolute_import
from subprocess import call
import unittest

from django.test import TestCase


class TestStyle(TestCase):

    @unittest.skip('Fails under Django 1.6')
    def test_flake8(self):
        result = call(['flake8', '--exclude', 'migrations,src', '.'])
        self.assertEqual(result, 0, "Code is not flake8.")
