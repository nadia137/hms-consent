{
    'name': 'Hospital - Electronic Consent Forms',
    'summary': """ Manage Digital Signed Consent Forms for Patient. Electronic Consent Forms for Hospital and patient.""",
    'version': '1.0.1',
    'category': 'Medical',
    'author': 'TVS Odoo Apps',
    "license": "LGPL-3",
    'depends': ["tvs_hms", "tvs_consent_form"],
    'data' : [
        'security/ir.model.access.csv',
        'report/consent_report.xml',
        'views/consent_form_view.xml',
    ],
    'images': [
        'static/description/th.png',
    ],
    'installable': True,
    'application': True,
    'sequence': 1,
    'price': 9,
    'currency': 'USD',
}
