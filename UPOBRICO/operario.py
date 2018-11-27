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

class operario(osv.Model):

    _name = 'operario'
    _description = 'Operario de la empresa'
 
    _columns = {
            'name': fields.char('Nombre', size=60, required=True),
            'dni': fields.char('DNI', size=9, required=True),
            'photo': fields.binary('Foto'), #Si quieres que salgan fotos debes de poner un tipo de dato binario
            'company_id': fields.many2one('empresa', 'Company', required=True),
            'servicios_ids': fields.many2many('servicio','operario_servicio_rel','operario_id','servicio_id','Servicios que realiza'),
        }