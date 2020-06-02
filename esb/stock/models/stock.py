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


class StockPicking(models.Model):
    _inherit = "stock.picking"

    name = fields.Char(readonly=False)
