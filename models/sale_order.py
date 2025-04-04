from odoo import models, api

class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.onchange("order_line", "partner_id")
    def _onchange_rg_5329_check(self):
        for order in self:
            if order.partner_id.l10n_ar_afip_responsibility_type_id.code != "1":
                return

            total_alcanzado = sum(
                line.price_subtotal
                for line in order.order_line
                if line.product_id.product_tmpl_id.x_rg_5329_iva_3
            )

            for line in order.order_line:
                if (
                    line.product_id.product_tmpl_id.x_rg_5329_iva_3
                    and total_alcanzado > 100000
                ):
                    impuesto = self.env.ref("rg5329_percepcion.tax_rg_5329", raise_if_not_found=False)
                    if impuesto and impuesto not in line.tax_id:
                        line.tax_id += impuesto