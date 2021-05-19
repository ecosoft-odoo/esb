# Copyright 2020 Ecosoft Co., Ltd (http://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

from odoo import fields, models


class StockMove(models.Model):
    _inherit = "stock.move"

    analytic_account_id = fields.Many2one(
        comodel_name="account.analytic.account",
        string="Department",
    )


class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    analytic_account_id = fields.Many2one(
        comodel_name="account.analytic.account",
        string="Department",
    )
    # Patch to fix problem -> https://github.com/ecosoft-odoo/esb/issues/161
    # So, now the original compute function won't work, but user say they don't use it.
    secondary_uom_qty = fields.Float(compute=False)
