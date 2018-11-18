
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
{
    "name": "upobrico",
    "version": "1.0",
    "depends": ["base"],
    "author": "Carrillo Bejarano Andres, Gomez Gonzalez Oscar, Lakidain de Arriba Ander",
    "category": "upobrico",
    "description": """
    Modulo de gestion de reparaciones a domicilio de la empresa upobrico
    """,
    "init_xml": [],
    'update_xml': [],
    'data': ['operario_view.xml','empresa_view.xml'], #tenemos ahora mismo operario como con la vista de primer nivel, posteriormente sera servicio el que lo tenga
    'demo_xml': [],
    'installable': True,
    'active': False,
#    'certificate': 'certificate',
}
