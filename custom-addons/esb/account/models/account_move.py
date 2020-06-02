# Copyright 2020 Ecosoft Co., Ltd (http://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    packing_list_id = fields.Many2one(
        comodel_name="esb.packing.list",
        string="Packing List",
        ondelete="cascade",
    )
    discount_last = fields.Float(
        string="Discount (%)",
        digits="Discount",
        default=0.0,
    )
    discount_special = fields.Float(
        string="Special Discount (%)",
        digits="Discount",
        default=0.0,
    )

    _sql_constraints = [
        (
            "discount_last_limit",
            "CHECK (discount_last <= 100.0)",
            "Discount must be lower than 100%.",
        ),
        (
            "discount_special_limit",
            "CHECK (discount_special <= 100.0)",
            "Discount must be lower than 100%.",
        ),
    ]

    @api.onchange("discount_last", "discount_special")
    def _onchange_discount_last(self):
        # Change discount_last to discount3
        # Change discount_special to discount2
        for record in self:
            for line in record.invoice_line_ids:
                line.discount3 = record.discount_last
                line.discount2 = record.discount_special
                line._onchange_triple_discount()
                line._onchange_price_subtotal()
                line._onchange_balance()

    @api.depends("partner_id", "company_id")
    def _compute_sale_type_id(self):
        # sale_type_id is False when account_move create from PO
        super()._compute_sale_type_id()
        for record in self:
            if record.type not in ["out_invoice", "out_refund"]:
                record.sale_type_id = False


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    subtotal_no_disc = fields.Monetary(
        string="Subtotal",
        store=True,
        compute="_compute_subtotal_no_disc",
        currency_field="always_set_currency_id",
        help="Subtotal not including discount",
    )

    @api.depends("quantity", "price_unit")
    def _compute_subtotal_no_disc(self):
        for record in self:
            record.subtotal_no_disc = record.quantity * record.price_unit
