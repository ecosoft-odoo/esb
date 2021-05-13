# Copyright 2020 Ecosoft Co., Ltd (http://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    # change Weight to Net Weight
    weight = fields.Float(string="Net Weight", digits="Stock Weight")
