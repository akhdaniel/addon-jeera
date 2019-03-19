from odoo import api, fields, models, _
import time
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)

class account_move(models.Model):
    _name = 'account.move'
    _inherit = 'account.move'


    def batch_journal(self, data):
        _logger.info(data)
        am_obj = self.env['account.move']
        partner_obj = self.env['res.partner']
        coa_obj = self.env['account.account']

        for am in data:
            #sql = "insert into account_move () values ()"
            journal_id = am['journal_id']
            ref = am['ref']
            date = am['date']
            line_ids = [ ]

            for line in am['line_ids']:
                va = line['partner_id']

                partner_id = partner_obj.search([('x_jeera_v_a','=',va)])
                if not partner_id:
                    _logger.info('parnter not found ********** VA %s', va)
                    continue

                coa_id = coa_obj.search([('code','=', line['account_id'])])
                if not coa_id:
                    _logger.info('coa_id not found **********')
                    continue

                line_ids.append((0,0,{
                    'account_id': coa_id.id ,
                    'partner_id': partner_id.id,
                    'name': line['name'],
                    'debit': line['debit'],
                    'credit': line['credit']
                }))

            values = {
                'journal_id': journal_id,
                'date': date,
                'ref': ref,
                'line_ids': line_ids
            }
            am_id = am_obj.create(values)
            am_id.post()

        return am_id.id
