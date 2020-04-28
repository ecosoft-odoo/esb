# Copyright 2020 Ecosoft Co., Ltd (http://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

from odoo import models, fields


class MrpProduction(models.Model):
    _inherit = "mrp.production"

    department_id = fields.Many2one(
        comodel_name="hr.department",
        string="Department",
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",
        required=True,
    )
