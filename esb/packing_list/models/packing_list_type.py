# Copyright 2020 Ecosoft Co., Ltd (http://ecosoft.co.th/)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import api, fields, models


class ESBPackingListType(models.Model):
    _name = "esb.packing.list.type"
    _description = "Type of Packing List"
    _order = "sequence"

    @api.model
    def _get_domain_sequence_id(self):
        return [("code", "=", "packing.list"), "|", ("company_id", "=", False), ("company_id", "=", self.env.company.id)]

    @api.model
    def _default_sequence_id(self):
        seq_type = self.env["ir.sequence"].search([("code", "=", "packing.list"), "|", ("company_id", "=", False), ("company_id", "=", self.env.company.id)], limit=1)
        return seq_type.id

    name = fields.Char(required=True)
    active = fields.Boolean(default=True)
    description = fields.Text(string="Description", translate=True)
    sequence_id = fields.Many2one(
        comodel_name="ir.sequence",
        string="Entry Sequence",
        copy=False,
        domain=_get_domain_sequence_id,
        default=_default_sequence_id,
        required=True,
    )
    incoterm_id = fields.Many2one(comodel_name="account.incoterms", string="Incoterm")
    sequence = fields.Integer(default=10)
    company_id = fields.Many2one(
        comodel_name="res.company",
        string="Company",
        default=lambda self: self.env.company,
    )
