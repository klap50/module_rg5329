from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    rg_5329_applicable = fields.Boolean(
        string="Aplicar Percepción RG 5329",
        compute="_compute_rg_5329_applicable",
        store=True
    )

    @api.depends('order_line.price_subtotal', 'order_line.product_id')
    def _compute_rg_5329_applicable(self):
        for order in self:
            total = sum(
                line.price_subtotal
                for line in order.order_line
                if line.product_id.x_rg_5329_iva_3
            )
            order.rg_5329_applicable = total > 100000

    def _recalculate_rg_5329(self):
        rg_5329_tax = self.env['account.tax'].search([
            ('name', '=', 'Percepción RG 5329 IVA 3%')
        ], limit=1)

        for order in self:
            for line in order.order_line:
                if rg_5329_tax in line.tax_id:
                    line.tax_id -= rg_5329_tax

            if order.rg_5329_applicable and rg_5329_tax:
                for line in order.order_line:
                    if line.product_id.x_rg_5329_iva_3:
                        line.tax_id |= rg_5329_tax

    @api.model
    def create(self, vals):
        order = super(SaleOrder, self).create(vals)
        order._recalculate_rg_5329()
        return order

    def write(self, vals):
        res = super(SaleOrder, self).write(vals)
        self._recalculate_rg_5329()
        return res
