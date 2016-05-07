from __future__ import absolute_import
from .models import UrlStore
from table import Table
from table.columns import Column

class UrlTable(Table):
    id = Column(field='id')
    url = Column(field='url')

    class Meta:
        model = UrlStore
        ajax = True
        ajax_source = 'table_data'
