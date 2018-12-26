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
    
    def eliminarMateriales(self,cr,uid,ids,context=None): #No ponemos la barra baja para no considerarlo privado y poder llamarlo desde fuera
        # ids es una lista de ids
        # desde la vista nos llega el id (en ids[0])de la clase
        # editada en la vista de formulario
        # Eliminamos los registros de la relación many2many
        res = self.write(cr,uid,ids,{'material_id':[ (5, ) ]}, context=None)   #el cuarto parametro es un diccionario val. Cuando te pidan id pones ids[0]
        return res
 
    _columns = {
            'id':fields.char('ID', size=9, required=False),
            'name':fields.char('Descripcion', size=140, required=True),
            'f_entrada':fields.date('Fecha Entrada', size=20, required=True),
            'f_salida':fields.date('Fecha Salida', size=20, required=True),
            'cita_id':fields.many2one('cita','Cita'),
            'material_id':fields.many2many('material','reparacion_material_rel','reparacion_id','material_id','Materiales usados'),
            'incidencia_id':fields.many2many('incidencia','reparacion_incidencia_rel','reparacion_id','incidencia_id','Incidencias en la reparacion'),
        }