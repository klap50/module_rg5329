from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.depends('order_line.price_subtotal', 'order_line.product_id')
    def _compute_rg_5329_applicable(self):
        for order in self:
            total_rg_5329 = sum(
                line.price_subtotal
                for line in order.order_line
                if line.product_id.x_rg_5329_iva_3
            )
            order.rg_5329_applicable = total_rg_5329 > 100000

    rg_5329_applicable = fields.Boolean(
        string="Aplicar Percepción RG 5329",
        compute="_compute_rg_5329_applicable",
        store=True
    )

    @api.onchange('order_line', 'order_line.product_id', 'order_line.price_unit')
    def _apply_rg_5329_tax(self):
        rg_5329_tax = self.env['account.tax'].search([('name', '=', 'Percepción RG 5329 IVA 3%')], limit=1)
        for order in self:
            for line in order.order_line:
                # Remover el impuesto si ya está y no debe aplicarse
                if rg_5329_tax in line.tax_id:
                    line.tax_id -= rg_5329_tax

            if order.rg_5329_applicable and rg_5329_tax:
                for line in order.order_line:
                    if line.product_id.x_rg_5329_iva_3:
                        line.tax_id |= rg_5329_tax
