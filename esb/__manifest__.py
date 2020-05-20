# Copyright 2020 Ecosoft Co., Ltd (http://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

{
    "name": "ESB :: Custom addons",
    "summary": "Custom addons for only esb project",
    "version": "13.0.1.0.0",
    "category": "Hidden",
    "author": "Ecosoft Co., Ltd",
    "license": "AGPL-3",
    "website": "https://ecosoft.co.th",
    "depends": [
        "purchase_order_secondary_unit",
        "purchase_order_type",
        "sale_order_type",
        "manufacturing_order_type",
        "report_qweb_element_page_visibility",
    ],
    "data": [
        "mrp/views/mrp_production_views.xml",
        "product/views/product_views.xml",
        "purchase/views/purchase_views.xml",
        "sale/views/sale_views.xml",
        "fonts/style.xml",
        # Packing List
        "packing_list/datas/paper_format.xml",
        "packing_list/datas/report_data.xml",
        "packing_list/reports/packing_list_form.xml",
        "packing_list/security/ir.model.access.csv",
        "packing_list/views/packing_list_views.xml",
        # Forms
        "account_form/datas/paper_format.xml",
        "account_form/datas/report_data.xml",
        "account_form/reports/tax_invoice_form.xml",
        "purchase_form/datas/paper_format.xml",
        "purchase_form/datas/report_data.xml",
        "purchase_form/reports/purchase_form.xml",
    ],
    "installable": True,
}
