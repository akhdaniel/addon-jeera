from odoo import api, fields, models

class kota(models.Model):
    _name = 'vit.kota'

    name = fields.Char("Name", required=True)

    state_id = fields.Many2one(comodel_name="res.country.state",
                               string="State", required=True, )