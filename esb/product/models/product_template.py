# Copyright 2020 Ecosoft Co., Ltd (http://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = "product.template"

    short_name = fields.Char(string="Short Name", size=30)
    long_name = fields.Char(string="Long Name", size=100)
    brand = fields.Char(string="Brand", size=30)
    series = fields.Char(string="Series", size=30)
    spec1 = fields.Char(string="Spec 1", size=100)
    spec2 = fields.Char(string="Spec 2", size=100)
    spec3 = fields.Char(string="Spec 3", size=100)
    pack_carton = fields.Float(string="Pack per Carton", default=1.00)
    sale_ratio = fields.Float(string="Ratio (divider)", default=1.00)
    gross_weight = fields.Float(string="Gross Weight", digits="Stock Weight")
    gross_weight_uom_name = fields.Char(
        string="Gross weight unit of measure label",
        related="weight_uom_name",
        readonly=True,
    )
    # change Weight to Net Weight
    weight = fields.Float(
        string="Net Weight",
        compute="_compute_weight",
        digits="Stock Weight",
        inverse="_set_weight",
        store=True,
    )
