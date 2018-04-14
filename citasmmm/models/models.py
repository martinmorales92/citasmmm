# -*- coding: utf-8 -*-

from odoo import models, fields, api

class citasmmm(models.Model):
    _name = 'citasmmm.citasmmm'
    _order = "fecha, orden desc" 

    autor = fields.Char(required=True)
    fecha = fields.Date(default=fields.Date.today, required=True)
    orden = fields.Integer(required=True)
    cita = fields.Text(required=True)
    

    