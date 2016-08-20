from openerp import fields, models

class hr_attendance(models.Model):
    _inherit = 'hr.attendance'
    device_id = fields.Many2one('hr.device', 'Device #')
    