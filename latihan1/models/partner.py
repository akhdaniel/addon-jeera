from odoo import api, fields, models
import logging
_logger = logging.getLogger(__name__)
import time
from odoo.exceptions import UserError

class partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    # field NPWP
    npwp = fields.Char(string="NPWP",
                       required=True,
                       help="Masukkan nomor NPWP",
                       )

    kota_id = fields.Many2one(comodel_name="vit.kota", string="Kota/Kab", required=False, )


    def create_invoice(self):
        _logger.warning('creating invoice')
        inv = self.env['account.invoice']

        product_id = self.env['product.product'].search([('name','=','Biaya Langganan Bulanan')])
        if not product_id:
            raise UserError("Product not found")

        account_id = self.env['account.account'].search([('name','=','Product Sales')])
        if not account_id:
            raise UserError("Account not found")

        data = {
            'partner_id': self.id,
            'date_invoice': time.strftime("%Y-%m-%d"),
            'invoice_line_ids': [(0,0,{
                'product_id': product_id.id,
                'name': 'Biaya bulanan',
                'account_id': account_id.id,
                'quantity': 1,
                'price_unit': 20000
            })]
        }
        new_inv = inv.create(data)

        new_inv.action_invoice_open()

