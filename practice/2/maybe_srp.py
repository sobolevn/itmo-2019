# -*- coding: utf-8 -*-

import logger


class CollectsStatisticsForOrders(object):
    """This class joins together the order id and number of sales."""

    def __init__(self, database, api) -> None:
        """We need a database access for orders and API access for counts."""
        self._database = database
        self._api = api

    def run(self):
        """Does the job."""
        orders = self._database.orders_to_find_prices()
        order_ids = [order.id for order in orders]
        logger.log('Searching prices for orders:', order_ids)
        return self._api.prices_for_order_ids(order_ids)
