# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (http://tiny.be). All Rights Reserved
#    
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################
from osv import osv
from osv import fields

class reparacion(osv.Model):
    _name = 'reparacion'
    _description = 'reparaciones de UPOBRICO'
 
    _columns = {
            'id':fields.char('ID', size=9, required=False),
            'descripcion':fields.char('descripcion', size=140, required=False),
            'f_entrada':fields.date('fecha_entrada', size=20, required=False),
            'f_salida':fields.date('fecha_salida', size=20, required=False),
            'cita_id':fields.many2one('cita','Cita',required=True),
            'material_id':fields.many2many('material','reparacion_material_rel','reparacion_id','material_id','Materiales usados'),
            'incidencia_id':fields.many2many('incidencia','reparacion_incidencia_rel','reparacion_id','incidencia_id','Incidencias en la reparacion')
        }










