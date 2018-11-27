
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

class ClassName(osv.Model):
    _name = 'citas'
    _description = 'citas que realiza un servicio'
 
    _columns = {
            'id':fields.char('ID', size=9, required=False),
            'f_asignacio':fields.date('fecha_asignacio', size=20, required=False),
            'f_cita':fields.date('fecha_cita', size=20, required=False),
            'descripcion':fields.char('descripcion', size=140, required=False),
            'servicios_id': fields.many2one('servicios', 'Servicioscitas'),
        }

