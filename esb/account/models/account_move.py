# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Copyright 2020 Tecnativa - Pedro M. Baeza

from odoo import api, models


class AccountMove(models.Model):
    _inherit = "account.move"

    @api.depends("partner_id", "company_id")
    def _compute_sale_type_id(self):
        # sale_type_id is False when account_move create from PO
        super()._compute_sale_type_id()
        for record in self:
            if record.purchase_id:
                record.sale_type_id = False
