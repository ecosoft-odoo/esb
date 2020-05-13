# Copyright 2020 Ecosoft Co., Ltd (http://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

from odoo import api, fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    po_created = fields.Boolean(default=False)

    @api.model
    def create(self, vals):
        vals["po_created"] = True
        return super().create(vals)


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    mo_ref = fields.Char(string="MO Reference")
