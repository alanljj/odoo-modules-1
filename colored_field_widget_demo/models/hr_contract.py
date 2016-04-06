#-*- coding:utf-8 -*-

from openerp import models, fields, api


class HrContract(models.Model):

    _inherit = 'hr.contract'

    mark_color = fields.Boolean('Mark name with color')
