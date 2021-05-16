# Copyright 2020 Ecosoft Co., Ltd (http://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

from odoo import fields, models


class StockInventory(models.Model):
    _inherit = "stock.inventory"

    remark = fields.Text(
        string="Remark",
        translate=True,
    )
