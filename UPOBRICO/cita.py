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

# Comprobacion on_change:
    
    
class cita(osv.Model):
    _name = 'cita'
    _description = 'citas que realiza un servicio'
 
# Comprobacion funcional
    def _check_fechas(self, cr, uid, ids):  # No puede haber clases con capacidad negativa o superior a 50
        for cita in self.browse(cr, uid, ids):  # Esto es si cambias varios registros
          if cita.f_asignacion > cita.f_cita:
                return False
        return True
    def on_change_reparacion(self, cr, uid, ids, estado):
        warning={
                'title' : 'Estado Incorrecto' ,
                'message' : 'El usuario debe estar admitido para añadir reparación' }
        if estado!="admitido" :
            return { 'value' :{ 'name' : 'ERROR' }, 'warning' :warning}
        return false
    _columns = {
            'id':fields.char('ID', size=9, required=False),
            'f_asignacion':fields.date('Fecha_asignacion', size=20, required=True),
            'f_cita':fields.date('Fecha_cita', size=20, required=True),
            'descripcion':fields.char('Descripcion', size=140, required=True),
            'servicio_id': fields.many2one('servicio', 'Servicio', required=True),
            'administrativo_id': fields.many2one('administrativo', 'Administrativo', required=True),
            'cliente_id': fields.many2one('cliente', 'Cliente', required=True),
            'reparacion_id': fields.many2one('reparacion', 'Reparacion'),
            'state':fields.selection([('solicitante', 'Solicitante'), ('admitido', 'Admitido'), ('enproceso', 'En Proceso'), ('terminado', 'Terminado')], 'Estados'),
        }
    
    _defaults = {'state':'solicitante'}
    
    _constraints = [(_check_fechas, 'La fecha de inicio debe ser menor a la de fin', ['f_asignacion', 'f_cita'])]
    
    
    
