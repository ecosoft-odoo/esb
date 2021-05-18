# Copyright 2019 Ecosoft Co., Ltd (https://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

from odoo import fields, models

class WithholdingTaxCertLine(models.Model):
    _inherit = "withholding.tax.cert.line"

    # Change required=False
    # As it was required=True, we have null error when update module cert.
    # Still don't know the real reason
    wt_cert_income_type = fields.Selection(
        required=False
    )