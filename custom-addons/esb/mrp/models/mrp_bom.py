# Copyright 2020 Ecosoft Co., Ltd (http://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

from odoo import models, fields


class MrpBom(models.Model):
    _inherit = "mrp.bom"

    remark = fields.Text(
        string="Remark",
        translate=True,
    )
