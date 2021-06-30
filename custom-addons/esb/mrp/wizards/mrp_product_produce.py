# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from datetime import datetime

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.tools import float_compare


# class MrpProductProduce(models.TransientModel):
#     _inherit = "mrp.product.produce"

#     # def _get_default_location_ids(self):
#     #     company_id = self.env.context.get('default_company_id') or self.env.company.id
#     #     warehouse = self.env['stock.warehouse'].search([('company_id', '=', company_id)], limit=1)
#     #     if warehouse:
#     #         return warehouse.lot_stock_id.id
#     #     return None

#     location_id = fields.Many2one(
#         comodel_name='stock.location',
#         domain="[('usage', '=', 'internal'), ('company_id', 'in', [company_id, False])]",
#         # default=_get_default_location_ids,
#         check_company=True,
#         string="Source Location",
#     )


class MrpProductProduceLine(models.TransientModel):
    _inherit = 'mrp.product.produce.line'

    location_id = fields.Many2one(
        comodel_name="stock.location",
        # compute="_compute_location_id",
        string="Source Location",
        # store=True,
    )

    # @api.depends("raw_product_produce_id.location_id")
    # def _compute_location_id(self):
    #     for loc in self:
    #         loc.location_id = loc.raw_product_produce_id.location_id
