# -*- coding: utf-8 -*-
# @Time    : 9/28/2021 11:56 AM
# @Author  : Kamal SELVAM
# @Email   : kamal.selvam@orange.com
# @File    : messagebus.py.py


from typing import List, Dict, Callable, Type
from src.allocation.adapters import email
from src.allocation.domain import events



def handle(event: events.Event):
    for handler in HANDLERS[type(event)]:
        handler(event)

def send_out_of_stock_notification(event: events.OutOfStock):
    email.send_mail(
        "stock@made.com",
        f"Out of stock for {event.sku}"
    )

HANDLERS = {
    events.OutOfStock : [send_out_of_stock_notification]
}