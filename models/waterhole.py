from openerp import api, fields, models


class Waterhole(models.Model):
    _name = 'waterhole'

    name = fields.Char(string="Watterhole ID", required=True)
    owner = fields.Many2one('res.partner', required=True)
    cubic_meters = fields.Float(required=True)
    expiration_date = fields.Date(required=True)
    coordinates = fields.Char(required=True)

    _sql_constraints = [
        ('waterhole_id_unique',
         'UNIQUE(name)',
         _("The waterhole id must be unique")),
    ]
