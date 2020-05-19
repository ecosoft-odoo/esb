# Copyright 2020 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

import logging

from odoo import models

_logger = logging.getLogger(__name__)

try:
    from num2words import num2words
except ImportError:
    _logger.warning(
        "The num2words python library is not installed,"
        "amount-to-text features won't be fully available."
    )
    num2words = None


class Currency(models.Model):
    _inherit = "res.currency"

    def amount_to_text(self, amount):
        amount_words = super().amount_to_text(amount)
        if self.name == "THB":
            try:
                amount_words = num2words(amount, to="currency", lang="th")
            except NotImplementedError:
                amount_words = num2words(amount, to="currency", lang="en")
        return amount_words
