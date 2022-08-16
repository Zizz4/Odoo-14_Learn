from odoo import api, fields, models

class ObatPasien(models.Model):
    _inherit = "hospital.patient"

    deskripsi_obat = fields.Char(string='Deskripsi Obat',tracking=True)