import base64
import locale
from io import BytesIO

from odoo import fields, models, api


class AccountPaymentCustom(models.Model):
    _inherit = 'account.payment'

    @api.model
    def company_info(self):
        company = self.env.user.company_id
        logo_data = base64.b64decode(company.logo)
        return {
            'name': company.name,
            'vat': company.vat,
            'vrn': company.company_registry,
            'street': company.street,
            'street2': company.street2,
            'phone': company.phone,
            'email': company.email,
            'website': company.website,
            'logo': BytesIO(logo_data)
        }

    @api.multi
    def print_delivery_note_action(self):
        return self.env.ref('custom_sale.delivery_note_print_pdf_id').report_action(self)


class AccountInvoiceInherit(models.Model):
    _inherit = 'account.invoice'

    # def action_invoice_to_open(self):
    #     self.write({'state': 'open'})
    #     return True
