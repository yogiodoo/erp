# -*- coding: utf-8 -*-
{
    'name': "uae_approval",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account', 'sale', 'purchase', 'stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/ds_report_inherited_doc.xml',
        'views/invoice_report_inherited_doc.xml',
        'views/po_report_inherited_doc.xml',
        'views/so_report_inherited_doc.xml',
        'views/po_reqQuotation_report_doc.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
