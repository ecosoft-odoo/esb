# Copyright 2020 Ecosoft Co., Ltd (http://ecosoft.co.th/).
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class MrpProduction(models.Model):
    _inherit = "mrp.production"

    def _default_order_type(self):
        return self.env["manufacturing.order.type"].search(
            ["|", ("company_id", "=", False), ("company_id", "=", self.company_id.id)],
            limit=1,
        )

    order_type = fields.Many2one(
        comodel_name="manufacturing.order.type",
        string="Type",
        ondelete="restrict",
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",
        default=_default_order_type,
    )

    @api.onchange("product_id")
    def onchange_product_id(self):
        super().onchange_product_id()
        mo_type = self.product_id.mo_type or self.product_id.categ_id.mo_type
        if mo_type:
            self.order_type = mo_type

    @api.onchange("order_type")
    def onchange_order_type(self):
        for order in self:
            if order.order_type.picking_type_id:
                order.picking_type_id = order.order_type.picking_type_id

    @api.model
    def create(self, vals):
        if vals.get("name", "/") == "/" and vals.get("order_type"):
            mo_type = self.env["manufacturing.order.type"].browse(vals["order_type"])
            if mo_type.sequence_id:
                vals["name"] = mo_type.sequence_id.next_by_id()
        return super().create(vals)
