# -*- coding: utf-8 -*-
# Coded by German Ponce Dominguez 
#     ▬▬▬▬▬.◙.▬▬▬▬▬  
#       ▂▄▄▓▄▄▂  
#    ◢◤█▀▀████▄▄▄▄▄▄ ◢◤  
#    █▄ █ █▄ ███▀▀▀▀▀▀▀ ╬  
#    ◥ █████ ◤  
#     ══╩══╩═  
#       ╬═╬  
#       ╬═╬ Dream big and start with something small!!!  
#       ╬═╬  
#       ╬═╬ You can do it!  
#       ╬═╬   Let's go...
#    ☻/ ╬═╬   
#   /▌  ╬═╬   
#   / \
# Cherman Seingalt - german.ponce@outlook.com

{
    'name': 'Modificaciones Facturación - Gobierno',
    'category': 'Cegasa',
    'description': """

        Este modulo agrega modificaciones.

    """,
    'author': 'German Ponce Dominguez',
    'website': 'http://poncesoft.blogspot.com',
    "support": "german.ponce@outlook.com",
    'depends': ['base','stock','stock_account','l10n_mx_edi'],
    'update_xml': [
        # 'stock_view.xml',
        'report/inventory_account_report_pdf.xml',
        'cfdi_template_view.xml',
        ],
    'installable': True,
}