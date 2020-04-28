# Copyright 2020 Ecosoft Co., Ltd (http://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

from odoo import models, fields


class StockScrap(models.Model):
    _inherit = "stock.scrap"

    department_id = fields.Many2one(
        comodel_name="hr.department",
        string="Department",
        related="production_id.department_id",
        readonly=True,
    )
