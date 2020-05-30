# Copyright 2020 Ecosoft Co., Ltd (http://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

from odoo import api, fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    po_created = fields.Boolean(default=False)

    discount_last = fields.Float(
        string="Discount (%)",
        digits="Discount",
        default=0.0,
    )

    _sql_constraints = [
        (
            "discount_last_limit",
            "CHECK (discount_last <= 100.0)",
            "Discount must be lower than 100%.",
        ),
    ]

    @api.onchange("discount_last")
    def _onchange_discount_last(self):
        # Change discount_last to discount3
        for record in self:
            for line in record.order_line:
                line.discount3 = record.discount_last

    @api.model
    def create(self, vals):
        vals["po_created"] = True
        return super().create(vals)

    def action_view_invoice(self):
        result = super().action_view_invoice()
        result['context']['default_discount_last'] = self.discount_last
        return result


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    mo_ref = fields.Char(string="MO Reference")

    account_analytic_id = fields.Many2one(
        comodel_name="account.analytic.account",
        string="Department",
        required=True,
    )

    subtotal_no_disc = fields.Monetary(
        string="Subtotal",
        store=True,
        compute="_compute_subtotal_no_disc",
        currency_field="currency_id",
        help="Subtotal not including discount",
    )

    @api.depends("product_uom_qty", "price_unit")
    def _compute_subtotal_no_disc(self):
        for record in self:
            record.subtotal_no_disc = record.product_qty * record.price_unit

    def _prepare_stock_moves(self, picking):
        self.ensure_one()
        res = super()._prepare_stock_moves(picking)
        for line in res:
            line["analytic_account_id"] = self.account_analytic_id.id
        return res
