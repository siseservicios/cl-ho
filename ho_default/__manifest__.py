##############################################################################
#
#    Copyright (C) 2020  jeo Software  (http://www.jeosoft.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your optiogitn) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#   le agregamos esto
##############################################################################

{
    'name': 'ho',
    'version': '13.0.1.0.0',
    'category': 'Tools',
    'summary': "Customizacion para Herramientas del oeste",
    'author': "jeo Software",
    'website': 'http://github.com/sebatista/cl-ho',
    'license': 'AGPL-3',
    'depends': [
	
        'standard_depends_ce',
		
		# Account - Contabilidad
		'account',
		'account_ux',
		'account_withholding',
		'account_debt_report',
		'account_check',
		'account_statement_aeroo_report',
		
		# Localization Arg - Localización argentina
		'l10n_ar_account_withholding',
		
		
		# 
		'website',
		'website_crm',
		'website_crm_sms',
		'website_sms',
		'website_sale',
		'website_form',
		'website_links',
		'website_mail',
		# faltan
		'website_sale_product_attachment',
		'website_sale_ux',
		#faltan
		'website_blog',
			
		'stock',
		'crm',
     ],
    'installable': True,

    # manifest version, if omitted it is backward compatible
    'env-ver': '2',

    # if Enterprise it installs in a different directory than community
    'odoo-license': 'CE',

    'port': '8069',

    'git-repos': [
        'https://github.com/siseservicios/cl-ho.git',
		
		# JEO
        'https://github.com/jobiols/odoo-jeo-ce jeo-odoo-jeo-ce',
        'https://github.com/jobiols/odoo-private-addons jeo-odoo-private-addons',
		'https://github.com/jobiols/odoo-addons jeo-odoo-addons',

		# Repositorio privado del tema utilizado por José Romero
        # ==========================================================
	        'git@github.com:sebatista/HO_teme_laze.git theme_laze',

        # Ing ADHOC 		# ===========================================================================
        'https://github.com/ingadhoc/odoo-argentina adhoc-odoo-argentina',
        'https://github.com/ingadhoc/odoo-argentina-ce adhoc-odoo-argentina-ce',
        'https://github.com/ingadhoc/account-financial-tools adhoc-account-financial-tools',
        'https://github.com/ingadhoc/aeroo_reports adhoc-aeroo_reports',
        'https://github.com/ingadhoc/miscellaneous adhoc-miscellaneous',
        'https://github.com/ingadhoc/sale adhoc-sale',
        'https://github.com/ingadhoc/product adhoc-product',
        'https://github.com/ingadhoc/argentina-sale adhoc-argentina-sale',
        'https://github.com/ingadhoc/account-payment adhoc-account-payment',
        'https://github.com/ingadhoc/stock adhoc-stock',
        'https://github.com/ingadhoc/website adhoc-website',
        'https://github.com/ingadhoc/partner adhoc-partner',
        'https://github.com/ingadhoc/account-invoicing adhoc-account-invoicing',
    
        # OCA 			# ===========================================================================
        'https://github.com/oca/web oca-web',
        'https://github.com/oca/partner-contact oca-partner-contact',
        'https://github.com/oca/sale-workflow oca-sale-workflow',
        'https://github.com/oca/server-ux oca-server-ux',
        'https://github.com/oca/contract oca-contract',
        'https://github.com/oca/social oca-social',
        'https://github.com/oca/stock-logistics-workflow oca-stock-logistics-workflow',
		'https://github.com/oca/server-tools oca-server-tools',
		'https://github.com/OCA/e-commerce oca-e-commerce',
		'https://github.com/OCA/website oca-website',
		
        # Odoomates 		# ===========================================================================
        'https://github.com/odoomates/odooapps om-odooapps',
		
		# Moldeo 			# ===========================================================================
		'https://github.com/ctmil/payment_mercadopago ctmil/payment_mercadopago',

        # Gabriela Rivero 	# ===========================================================================
        'https://github.com/regaby/odoo-custom regaby-odoo-custom',
    ],

    # list of images to use in the form 'name image-url'
    'docker-images': [
        'odoo jobiols/odoo-jeo:13.0',
        'postgres postgres:10.1-alpine',
        'nginx nginx',
		'dbtools jobiols/dbtools',
    ]
}
