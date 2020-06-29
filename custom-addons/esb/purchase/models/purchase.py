# Copyright 2020 Ecosoft Co., Ltd (http://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

from odoo import api, fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    po_created = fields.Boolean(default=False)

    so_reference = fields.Char(string="SO Reference")

    discount_waranty = fields.Monetary(
        string="Waranty Discount",
        digits="Discount",
        compute="_compute_discount",
    )
    discount_special = fields.Monetary(
        string="Special Discount",
        digits="Discount",
        compute="_compute_discount",
    )
    # discount_last = fields.Float(
    #     string="Discount (%)",
    #     digits="Discount",
    #     default=0.0,
    # )
    # discount_last_amount = fields.Monetary(
    #     string="Amount Discount",
    #     digits="Discount",
    #     compute="_compute_discount",
    # )

    # _sql_constraints = [
    #     (
    #         "discount_last_limit",
    #         "CHECK (discount_last <= 100.0)",
    #         "Discount must be lower than 100%.",
    #     ),
    # ]

    # @api.onchange("discount_last", "order_line")
    # def _onchange_discount_last(self):
    #     # Change discount_last to discount3
    #     for record in self:
    #         for line in record.order_line:
    #             if line.product_id.type in ('product', 'consu'):
    #                 line.discount3 = record.discount_last

    @api.depends("order_line")
    def _compute_discount(self):
        for record in self:
            discount_waranty = 0.00
            discount_special = 0.00
            for line in record.order_line:
                discount_waranty += line.subtotal_no_disc * line.discount / 100
                discount_special += line.subtotal_no_disc * line.discount2 / 100
            record.discount_waranty = discount_waranty
            record.discount_special = discount_special

            # total = sum(record.order_line.mapped("subtotal_no_disc"))
            # record.discount_last_amount = total * record.discount_last / 100

    @api.model
    def create(self, vals):
        vals["po_created"] = True
        return super().create(vals)

    # def action_view_invoice(self):
    #     result = super().action_view_invoice()
    #     result['context']['default_discount_last'] = self.discount_last
    #     return result

    def _prepare_sale_order_data(
        self, name, partner, dest_company, direct_delivery_address
    ):
        res = super()._prepare_sale_order_data(
            name, partner, dest_company, direct_delivery_address
        )
        if partner.sale_type:
            res["type_id"] = partner.sale_type.id
        return res


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    mo_ref = fields.Char(string="MO Reference")

    account_analytic_id = fields.Many2one(
        comodel_name="account.analytic.account",
        string="Department",
    )

    subtotal_no_disc = fields.Monetary(
        string="Subtotal Before Discount",
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
