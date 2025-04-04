{
    'name': 'RG 5329 Percepción IVA 3%',
    'version': '1.0',
    'depends': ['sale', 'account', 'l10n_ar'],
    'author': 'FWCorp',
    'category': 'Accounting',
    'description': 'Aplica automáticamente la percepción RG 5329 del 3% a productos alcanzados cuando el neto supera los $100.000 y el cliente es Responsable Inscripto.',
    'data': [
        'data/tax_data.xml',
        'views/product_view.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': False
}