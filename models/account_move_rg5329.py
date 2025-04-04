from odoo import models, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.onchange('invoice_line_ids')
    def _check_rg5329_condition(self):
        try:
            rg_tax = self.env.ref('rg5329_percepcion.tax_rg5329_pais_25')
        except ValueError:
            return  # Si el impuesto no existe aún, salimos

        total_rg_lines = sum(
            line.price_subtotal
            for line in self.invoice_line_ids
            if line.product_id.x_rg_5329_iva_3 and rg_tax in line.tax_ids
        )

        for line in self.invoice_line_ids:
            if rg_tax in line.tax_ids:
                if total_rg_lines <= 100000:
                    line.tax_ids -= rg_tax
                else:
                    if rg_tax not in line.tax_ids:
                        line.tax_ids += rg_tax