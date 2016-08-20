from openerp import fields, models

class hr_device(models.Model):
    _name = "hr.device"
    name = fields.Char('Device #', size=10, required=True)
    ip_address = fields.Char('Ip Address', size=20)
    
    


