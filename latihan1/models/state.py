from odoo import api, fields, models, _

class state(models.Model):
    _name = 'res.country.state'
    _inherit = 'res.country.state'

    kota_ids = fields.One2many(comodel_name="vit.kota",
                               inverse_name="state_id", string="Kota", required=False, )