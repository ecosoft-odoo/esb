# Copyright 2020 Ecosoft Co., Ltd (http://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

from odoo import api, models, fields


class MrpProduction(models.Model):
    _inherit = "mrp.production"

    machine_number = fields.Char(string="Machine Number", size=30)
    operator = fields.Char(string="Operator", size=30)
    shift = fields.Selection(
        selection=[("day", "Day"), ("night", "Night")],
        string="Shift",
        default="day",
    )
    assembly_line = fields.Selection(
        selection=[("auto", "Auto"), ("manual", "Manual"), ("line3", "Line 3")],
        string="Assembly Line",
        default="auto",
    )
    delay = fields.Boolean(string="Delay")
    remark = fields.Text(string="Remark", translate=True)
    net_weight = fields.Float(string="Net Weight(kg/pcs)", default=0.00)
    gross_weight = fields.Float(string="Net Weight + Inner Box(kg/pcs)", default=0.00)

    analytic_account_id = fields.Many2one(
        comodel_name="account.analytic.account",
        string="Department",
    )

    mo_created = fields.Boolean(default=False)
    planned_quantity = fields.Float(
        string="Planned Quantity",
        readonly=False,
    )

    @api.model
    def create(self, vals):
        vals["mo_created"] = True
        return super().create(vals)
