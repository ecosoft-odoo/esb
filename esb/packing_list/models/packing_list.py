# Copyright 2020 Ecosoft Co., Ltd (http://ecosoft.co.th/)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class ESBPackingList(models.Model):
    _name = "esb.packing.list"
    _description = "Printout Packing List for ESB"

    name = fields.Char(
        readonly=True,
        states={
            "draft": [("readonly", False)],
            "done": [("readonly", True)],
            "cancel": [("readonly", True)],
        },
    )
    ref = fields.Char(
        string="Reference",
        copy=False,
        states={
            "draft": [("readonly", False)],
            "done": [("readonly", True)],
            "cancel": [("readonly", True)],
        },
    )
    date = fields.Date(
        string="Date",
        states={
            "draft": [("readonly", False)],
            "done": [("readonly", True)],
            "cancel": [("readonly", True)],
        },
    )
    origin = fields.Char(
        string="Source Document",
        copy=False,
        default=lambda self: self._get_default_origin(),
        states={
            "draft": [("readonly", False)],
            "done": [("readonly", True)],
            "cancel": [("readonly", True)],
        },
    )
    incoterm_id = fields.Many2one(
        comodel_name="account.incoterms",
        string="Incoterm",
        states={
            "draft": [("readonly", False)],
            "done": [("readonly", True)],
            "cancel": [("readonly", True)],
        },
    )
    ship_from = fields.Char(
        string="Ship Form",
        default=lambda self: self._get_default_ship_form(),
        states={
            "draft": [("readonly", False)],
            "done": [("readonly", True)],
            "cancel": [("readonly", True)],
        },
    )
    ship_to = fields.Char(
        string="Ship To",
        default=lambda self: self._get_default_ship_to(),
        states={
            "draft": [("readonly", False)],
            "done": [("readonly", True)],
            "cancel": [("readonly", True)],
        },
    )
    note = fields.Text(
        string="Notes",
        copy=False,
        states={
            "draft": [("readonly", False)],
            "done": [("readonly", True)],
            "cancel": [("readonly", True)],
        },
    )
    partner_id = fields.Many2one(
        comodel_name="res.partner",
        string="Partner",
        required=True,
        copy=False,
        default=lambda self: self._get_default_partner_id(),
        states={
            "draft": [("readonly", False)],
            "done": [("readonly", True)],
            "cancel": [("readonly", True)],
        },
    )
    pl_type_id = fields.Many2one(
        comodel_name="esb.packing.list.type",
        string="Type",
        required=True,
    )
    company_id = fields.Many2one(
        comodel_name="res.company",
        string="Company",
        default=lambda self: self.env.company,
        required=True,
        states={
            "draft": [("readonly", False)],
            "done": [("readonly", True)],
            "cancel": [("readonly", True)],
        },
    )
    responsible_person = fields.Char(
        string="Responsible Person",
        states={
            "draft": [("readonly", False)],
            "done": [("readonly", True)],
            "cancel": [("readonly", True)],
        },
    )
    picking_ids = fields.Many2many(
        comodel_name="stock.picking",
        string="Packing List",
        domain="[('partner_id', '=', partner_id)]",
        required=True,
        copy=False,
        states={
            "draft": [("readonly", False)],
            "done": [("readonly", True)],
            "cancel": [("readonly", True)],
        },
    )
    picking_count = fields.Integer(
        string="Picking Count",
        compute="_compute_picking_count",
        readonly=True,
    )
    line_ids = fields.One2many(
        "esb.packing.list.line",
        inverse_name="packing_list_id",
        string="Lines",
        copy=False,
        states={
            "draft": [("readonly", False)],
            "done": [("readonly", True)],
            "cancel": [("readonly", True)],
        },
    )
    state = fields.Selection(
        selection=[("draft", "Draft"), ("done", "Done"), ("cancel", "Cancelled")],
        string="Status",
        default="draft",
        required=True,
        readonly=True,
        copy=False,
    )
    quantity_total = fields.Float(
        string="Total Quantity",
        digits="Product Unit of Measure",
        compute="_compute_total",
        store=True,
    )
    package_total = fields.Float(
        string="Total Package",
        digits="Product Unit of Measure",
        compute="_compute_total",
        store=True,
    )
    net_weight_total = fields.Float(
        string="Total Net Weight",
        digits="Stock Weight",
        compute="_compute_total",
        store=True,
    )
    gross_weight_total = fields.Float(
        string="Total Gross Weight",
        digits="Stock Weight",
        compute="_compute_total",
        store=True,
    )
    _sql_constraints = [(
        "name_unique",
        "unique(name)",
        "This name is already used by another packing list!"
    )]

    def _get_default_partner_id(self):
        if self._context.get("default_picking_ids"):
            pickings = self.env["stock.picking"].browse(self._context["default_picking_ids"])
            partners = pickings.mapped("partner_id")
            if len(partners) != 1:
                raise ValidationError(_("Selected pickings do not belong to the same partner!"))
            return partners[0].id

    def _get_default_origin(self):
        if self._context.get("default_picking_ids"):
            pickings = self.env["stock.picking"].browse(self._context["default_picking_ids"])
            origins = pickings.mapped("origin")
        return ", ".join(origin for origin in origins if origin not in (False, ""))

    def _get_default_ship_form(self):
        if self.company_id:
            return ", ".join([self.company_id.state_id.name, self.company_id.country_id.name])
        return False

    def _get_default_ship_to(self):
        if self.partner_id:
            return ", ".join([self.partner_id.state_id.name, self.partner_id.country_id.name])
        return False

    @api.depends("line_ids")
    def _compute_total(self):
        for rec in self:
            rec.quantity_total = sum(rec.line_ids.mapped("quantity"))
            rec.package_total = sum(rec.line_ids.mapped("package"))
            rec.net_weight_total = sum(rec.line_ids.mapped("net_weight"))
            rec.gross_weight_total = sum(rec.line_ids.mapped("gross_weight"))

    @api.onchange("partner_id")
    def _onchange_partner_id(self):
        if not self._context.get("default_picking_ids"):
            self.picking_ids = False
            self.line_ids = False
        if self.partner_id and self.partner_id.pl_type_id:
            self.pl_type_id = self.partner_id.pl_type_id

    @api.onchange("pl_type_id")
    def _onchange_pl_type_id(self):
        for rec in self:
            if rec.pl_type_id.incoterm_id:
                rec.incoterm_id = rec.pl_type_id.incoterm_id

    def action_draft(self):
        self.write({"state": "draft"})

    def action_done(self):
        self.write({"state": "done"})

    def action_cancel(self):
        self.write({"state": "cancel"})

    def write(self, vals):
        res = super().write(vals)
        if "line_ids" in vals:
            self.action_run_number()
        return res

    @api.model
    def create(self, vals):
        if vals.get("name", "/") == "/" and vals.get("pl_type_id"):
            pl_type = self.env["esb.packing.list.type"].browse(vals["pl_type_id"])
            if pl_type.sequence_id:
                vals["name"] = pl_type.sequence_id.next_by_id()
        if "line_ids" in vals:
            self.action_run_number()
        return super().create(vals)

    def action_compute(self):
        for rec in self:
            lines = []
            rec.line_ids.unlink()
            for picking in rec.picking_ids:
                for move in picking.move_lines:
                    lines.append((0, 0, {
                        "move_id": move.id,
                        "product_id": move.product_id.id,
                        "name": move.name,
                        "quantity": move.product_uom_qty,
                        "package": move.product_uom_qty / move.product_id.pack_carton,
                        "net_weight": move.product_uom_qty * move.product_id.weight,
                        "gross_weight": move.product_uom_qty * move.product_id.gross_weight,
                    }))
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
        pickings = self.mapped("picking_ids")
        action = self.env.ref("stock.stock_picking_action_picking_type").read()[0]
        action["domain"] = [("id", "in", pickings.ids)]
        return action

    @api.depends("picking_ids")
    def _compute_picking_count(self):
        for rec in self:
            rec.picking_count = len(self.picking_ids)


class ESBPackingListLine(models.Model):
    _name = "esb.packing.list.line"
    _description = "Printout Packing List for ESB"
    _order = "sequence"

    packing_list_id = fields.Many2one(
        comodel_name="esb.packing.list",
        index=True,
        required=True,
        ondelete="cascade",
    )
    display_type = fields.Selection(
        selection=[("line_section", "Section"), ("line_note", "Note")],
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
        comodel_name="stock.move",
        string="Stock Move",
    )
    product_id = fields.Many2one(
        comodel_name="product.product",
        string="Product",
    )
    name = fields.Text(
        string="Description",
    )
    quantity = fields.Float(
        string="Quantity",
        digits="Product Unit of Measure",
    )
    package = fields.Float(
        string="Packages",
        digits="Product Unit of Measure",
    )
    net_weight = fields.Float(
        string="Net Weight",
        digits="Stock Weight",
    )
    gross_weight = fields.Float(
        string="Gross Weight",
        digits="Stock Weight",
    )
