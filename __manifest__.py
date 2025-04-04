{
    'name': 'Percepción RG 5329',
    'version': '1.0',
    'author': 'Klap / FwCorp',
    'category': 'Accounting',
    'summary': 'Aplica percepción RG 5329 IVA 3% a productos alcanzados',
    'license': 'LGPL-3',
    'depends': ['base', 'product', 'account'],
    'data': [
        'views/product_view.xml',
        'views/product_data.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
