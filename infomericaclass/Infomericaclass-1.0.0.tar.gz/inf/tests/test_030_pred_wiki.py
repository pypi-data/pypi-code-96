#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tests for Wiki models

"""

import os
import shutil
import unittest
import pandas as pd
from ethnicolr.pred_wiki_ln import pred_wiki_ln
from ethnicolr.pred_wiki_name import pred_wiki_name
from . import capture


class TestPredWiki(unittest.TestCase):

    def setUp(self):
        names = [{'last': 'smith', 'first': 'john', 'true_race': 'GreaterEuropean,British'},
                 {'last': 'zhang', 'first': 'simon', 'true_race': 'Asian,GreaterEastAsian,EastAsian'}]
        self.df = pd.DataFrame(names)

    def tearDown(self):
        pass

    def test_pred_wiki_ln(self):
        odf = pred_wiki_ln(self.df, 'last')
        self.assertTrue(all(odf.sum(axis=1).round(1) == 1.0))
        self.assertTrue(all(odf.true_race == odf.race))

    def test_pred_wiki_name(self):
        odf = pred_wiki_name(self.df, 'last', 'first')
        self.assertTrue(all(odf.sum(axis=1).round(1) == 1.0))
        self.assertTrue(all(odf.true_race == odf.race))


if __name__ == '__main__':
    unittest.main()
