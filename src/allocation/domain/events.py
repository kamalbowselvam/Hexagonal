# -*- coding: utf-8 -*-
# @Time    : 9/28/2021 11:55 AM
# @Author  : Kamal SELVAM
# @Email   : kamal.selvam@orange.com
# @File    : events.py.py


from dataclasses import dataclass

class Event:
    pass


@dataclass
class OutOfStock(Event):
    sku: str