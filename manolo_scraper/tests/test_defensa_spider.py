# -*- coding: utf-8 -*-
import os
import unittest

from manolo_scraper.spiders.defensa import DefensaSpider
from utils import fake_response_from_file


class TestMineduSpider(unittest.TestCase):

    def setUp(self):
        self.spider = DefensaSpider()

    def test_parse_item(self):
        filename = os.path.join('data/defensa', '19-08-2015.html')
        items = self.spider.parse(fake_response_from_file(filename, meta={'date': u'19/08/2015'}))

        item = next(items)
        self.assertEqual(item.get('full_name'), u'AURELIO COREDOR MIRANO')
        self.assertEqual(item.get('time_start'), u'08:38')
        self.assertEqual(item.get('institution'), u'defensa')
        self.assertEqual(item.get('id_document'), u'DNI')
        self.assertEqual(item.get('id_number'), u'43447287')
        self.assertEqual(item.get('entity'), None)
        self.assertEqual(item.get('reason'), u'REUNIÓN DE TRABAJO')
        self.assertEqual(item.get('host_name'), u'HUGO DAVID MEJIA HUAMAN')
        self.assertEqual(item.get('time_end'), None)
        self.assertEqual(item.get('date'), u'2015-08-19')

        number_of_items = 1 + sum(1 for _ in items)
        self.assertEqual(number_of_items, 14)
