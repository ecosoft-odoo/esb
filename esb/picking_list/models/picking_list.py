# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class ESBPickingList(models.Model):
    _name = 'esb.picking.list'
    _description = 'Printout Picking List for ESB'

    name = fields.Char(
        required=True,
        states={'draft': [('readonly', False)], 'done': [('readonly', True)]},
    )
    ref = fields.Text(
        string='Reference',
        copy=False,
        states={'draft': [('readonly', False)], 'done': [('readonly', True)]},
    )
    note = fields.Text(
        string='Notes',
        copy=False,
        states={'draft': [('readonly', False)], 'done': [('readonly', True)]},
    )
    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Partner',
        required=True,
        copy=False,
        default=lambda self: self._get_default_partner_id(),
        states={'draft': [('readonly', False)], 'done': [('readonly', True)]},
    )
    picking_ids = fields.Many2many(
        comodel_name='stock.picking',
        string='Picking List',
        domain="[('partner_id', '=', partner_id)]",
        required=True,
        copy=False,
        states={'draft': [('readonly', False)], 'done': [('readonly', True)]},
    )
    picking_count = fields.Integer(
        string='Picking Count',
        compute='_compute_picking_count',
        readonly=True,
    )
    line_ids = fields.One2many(
        'esb.picking.list.line',
        inverse_name='picking_list_id',
        string='Lines',
        copy=False,
        states={'draft': [('readonly', False)], 'done': [('readonly', True)]},
    )
    state = fields.Selection(
        [('draft', 'Draft'),
         ('done', 'Done')],
        string='Status',
        default='draft',
        required=True,
        readonly=True,
        copy=False,
    )
    quantity_done_total = fields.Float(
        string='Quantity Total',
        digits='Product Unit of Measure',
        compute='_compute_quantity_done_total',
        store=True,
    )
    _sql_constraints = [(
        'name_unique',
        'unique(name)',
        'This name is already used by another picking list!'
    )]

    def _get_default_partner_id(self):
        if self._context.get('default_picking_ids'):
            pickings = self.env['stock.picking'].browse(self._context['default_picking_ids'])
            partners = pickings.mapped('partner_id')
            if len(partners) != 1:
                raise ValidationError(_('Selected pickings do not belong to the same partner!'))
            return partners[0].id

    @api.depends('line_ids')
    def _compute_quantity_done_total(self):
        for rec in self:
            rec.quantity_done_total = sum(rec.line_ids.mapped('quantity_done'))

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        if not self._context.get('default_picking_ids'):
            self.picking_ids = False
            self.line_ids = False

    def action_draft(self):
        self.write({'state': 'draft'})

    def action_done(self):
        self.write({'state': 'done'})

    def write(self, vals):
        res = super().write(vals)
        if 'line_ids' in vals:
            self.action_run_number()
        return res

    @api.model
    def create(self, vals):
        res = super().create(vals)
        if 'line_ids' in vals:
            self.action_run_number()
        return res

    def action_compute(self):
        for rec in self:
            lines = []
            rec.line_ids.unlink()
            for picking in rec.picking_ids:
                for move in picking.move_lines:
                    lines.append((0, 0, {'move_id': move.id,
                                         'product_id': move.product_id.id,
                                         'name': move.name,
                                         'quantity_done': move.quantity_done}))
            rec.line_ids = lines

    def action_run_number(self):
        # Run number and reset on each section
        for rec in self:
            number = 1
            for line in rec.line_ids:
                line.number = number
                number += 1
                if not line.product_id:
                    number = 1
                    continue

    def action_view_pickings(self):
        pickings = self.mapped('picking_ids')
        action = self.env.ref('stock.stock_picking_action_picking_type').read()[0]
        action['domain'] = [('id', 'in', pickings.ids)]
        return action

    @api.depends('picking_ids')
    def _compute_picking_count(self):
        for rec in self:
            rec.picking_count = len(self.picking_ids)



class ESBPickingListLine(models.Model):
    _name = 'esb.picking.list.line'
    _description = 'Printout Picking List for ESB'
    _order = 'sequence'

    picking_list_id = fields.Many2one(
        comodel_name='esb.picking.list',
        index=True,
        required=True,
        ondelete='cascade',
    )
    display_type = fields.Selection(
        [('line_section', "Section"),
         ('line_note', "Note")],
        default=False,
        help="Technical field for UX purpose.",
    )
    number = fields.Integer(
        string="#",
        readonly=True,
    )
    sequence = fields.Integer(
        default=10,
    )
    move_id = fields.Many2one(
        comodel_name='stock.move',
        string='Stock Move',
    )
    product_id = fields.Many2one(
        comodel_name='product.product',
        string='Product',
    )
    name = fields.Text(
        string="Description",
    )
    quantity_done = fields.Float(
        string='Quantity',
        digits='Product Unit of Measure',
    )
