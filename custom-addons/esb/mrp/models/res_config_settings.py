# Copyright 2019 Elico Corp, Dominique K. <dominique.k@elico-corp.com.sg>
# Copyright 2019 Ecosoft Co., Ltd., Kitti U. <kittiu@ecosoft.co.th>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    default_location_id = fields.Many2one(
        comodel_name='stock.location',
        domain="[('usage', '=', 'internal'), ('company_id', 'in', [company_id, False])]",
        string="Produce Source Location",
        default_model="mrp.product.produce.line",
        help="Select source location in production process",
    )
