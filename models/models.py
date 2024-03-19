# -*- coding: utf-8 -*-

from odoo import models, fields, api

class StockProductionLot(models.Model):
    _inherit = 'stock.production.lot'

    equipment_user = fields.Many2one('res.partner', string='Equipment User')
    equipment_location = fields.Char('Equipment Location')
    partner_id = fields.Many2one('res.partner', string="Customer", domain=[('is_company', '=', True)])
    project_id = fields.Many2one('project.project', string='Project')


    @api.onchange('equipment_user')
    def onchange_equipment_user(self):
        if self.equipment_user:
            self.partner_id = self.equipment_user.parent_id.id

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        return {'domain': {'equipment_user': [('parent_id', '=', self.partner_id.id)]}}

