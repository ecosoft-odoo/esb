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

    @api.depends("invoice_line_ids")
    def _compute_discount(self):
        for record in self:
            discount_waranty = 0.00
            discount_special = 0.00
            for line in record.invoice_line_ids:
                discount_waranty += line.subtotal_no_disc * line.discount1 / 100
                discount_special += line.subtotal_no_disc * line.discount2 / 100 * (100 - line.discount1) / 100
            record.discount_waranty = discount_waranty
            record.discount_special = discount_special

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
        string="Subtotal Before Discount",
        store=True,
        compute="_compute_subtotal_no_disc",
        currency_field="always_set_currency_id",
        help="Subtotal not including discount",
    )

    @api.depends("quantity", "price_unit")
    def _compute_subtotal_no_disc(self):
        for record in self:
            record.subtotal_no_disc = record.quantity * record.price_unit
