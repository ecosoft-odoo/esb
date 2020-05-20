# Copyright 2020 Ecosoft Co., Ltd (http://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    so_created = fields.Boolean(default=False)

    @api.model
    def create(self, vals):
        vals["so_created"] = True
        return super().create(vals)

    def copy_data(self, default=None):
        if default is None:
            default = {}
        default["type_id"] = self.type_id.id
        return super().copy_data(default)
