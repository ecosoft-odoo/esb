# Copyright 2015-2019 See manifest
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import api, fields, models, _
from odoo.tools.safe_eval import safe_eval
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_round


class ESBPickingList(models.Model):
    _name = 'esb.picking.list'
    _description = 'Printout Picking List for ESB'

    name = fields.Char(required=True)
    ref = fields.Text(
        string='Reference',
        copy=False)
    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Partner',
        required=True,
    )
    picking_ids = fields.Many2many(
        comodel_name='stock.picking',
        string='Picking List',
        domain="[('partner_id', '=', partner_id)]",
        required=True,
    )
    line_ids = fields.One2many(
        'esb.picking.list.line',
        inverse_name='picking_list_id',
        string='Lines',
    )
    state = fields.Selection(
        [('draft', 'Draft'),
         ('done', 'Done')],
        string='Status',
        default='draft',
        required=True,
    )
    _sql_constraints = [(
        'name_unique',
        'unique(name)',
        'This name is already used by another picking list!'
    )]

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        self.picking_ids = False
        self.line_ids = False

    @api.multi
    def action_draft(self):
        self.write({'state': 'draft'})

    @api.multi
    def action_done(self):
        self.write({'state': 'done'})

    @api.multi
    def action_compute(self):
        for rec in self:
            lines = []
            for picking in rec.picking_ids:
                for move in picking.move_lines:
                    lines.append((0, 0, {'move_id': move.id,
                                         'product_id': move.product_id.id,
                                         'quantity_done': move.quantity_done}))
            rec.line_ids = lines


class ESBPickingListLine(models.Model):
    _name = 'esb.picking.list.line'
    _description = 'Printout Picking List for ESB'

    picking_list_id = fields.Many2one(
        comodel_name='esb.picking.list',
        index=True,
        required=True,
        ondelete='cascade',
    )
    move_id = fields.Many2one(
        comodel_name='stock.move',
        string='Stock Move',
    )
    product_id = fields.Many2one(
        comodel_name='product.product',
        string='Product',
    )
    quantity_done = fields.Float(
        string='Done',
        digits=dp.get_precision('Product Unit of Measure')
    )

    @api.onchange('move_id')
    def _onchange_move_id(self):
        self.product_id = self.move_id.product_id
        self.quantity_done = self.move_id.quantity_done
