from odoo import api, fields, models

class HospitalMedicine(models.Model):
    _name = "hospital.medicine"
    _description = "Hospital Medicine"

    name = fields.Char(string='Name', required=True)
    harga = fields.Integer(string='Price')
    jenis = fields.Selection([
        ('kapsul', 'Kapsul'),
        ('tablet', 'Tablet'),
        ('other', 'Other')
    ], required=True, default='kapsul')
    note = fields.Text(string='Description')