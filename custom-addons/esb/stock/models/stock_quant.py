# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from odoo.tools.float_utils import float_is_zero


class StockQuant(models.Model):
    _inherit = 'stock.quant'

    categ_id = fields.Many2one(
        'product.category',
        compute='_compute_categ_id',
        string="Product Category"
        )

    @api.depends('product_id')
    def _compute_categ_id(self):
        for quant in self:
            quant.categ_id = quant.product_id.categ_id
