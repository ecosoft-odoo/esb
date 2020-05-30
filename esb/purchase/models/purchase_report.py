# Copyright 2020 Ecosoft Co., Ltd (http://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

from odoo import fields, models


class PurchaseReport(models.Model):
    _inherit = "purchase.report"

    account_analytic_id = fields.Many2one(
        comodel_name="account.analytic.account",
        string="Department",
        readonly=True,
    )

    date_planned = fields.Datetime(string="Scheduled Date", readonly=True)

    def _select(self):
        res = super()._select()
        res += ", l.date_planned AS date_planned"
        return res

    def _group_by(self):
        res = super()._group_by()
        res += ", l.date_planned"
        return res
