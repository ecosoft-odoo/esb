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
        "stock_secondary_unit",
        "purchase_order_secondary_unit",
        "purchase_order_type",
        "sale_order_type",
        "manufacturing_order_type",
        "report_qweb_element_page_visibility",
        "purchase_triple_discount",
        "sale_triple_discount",
        "l10n_th_withholding_tax_cert",
    ],
    "data": [
        "account/views/account_move_views.xml",
        "mrp/reports/mrp_report_bom_structure.xml",
        "mrp/views/mrp_production_views.xml",
        "mrp/views/mrp_bom_views.xml",
        "mrp/wizards/mrp_product_produce_views.xml",
        "product/views/product_views.xml",
        "purchase/views/purchase_views.xml",
        "sale/views/sale_views.xml",
        "stock/reports/report_deliveryslip.xml",
        "stock/reports/report_picking_operations.xml",
        "stock/views/stock_move_views.xml",
        "stock/views/stock_picking_views.xml",
        "stock/views/stock_inventory_views.xml",
        "stock/views/stock_scrap_views.xml",
        "fonts/style_report.xml",
        # Packing List
        "packing_list/datas/paper_format.xml",
        "packing_list/datas/report_data.xml",
        "packing_list/reports/delivery_order_form.xml",
        "packing_list/reports/packing_list_form.xml",
        "packing_list/security/ir.model.access.csv",
        "packing_list/security/security.xml",
        "packing_list/views/packing_list_type_views.xml",
        "packing_list/views/packing_list_views.xml",
        "packing_list/views/res_partner_views.xml",
        # Forms
        "account_form/datas/paper_format.xml",
        "account_form/datas/report_data.xml",
        "account_form/reports/tax_invoice_form.xml",
        "account_form/reports/official_commercial_invoice_form.xml",
        "account_form/reports/customer_commercial_invoice_form.xml",
        "account_form/reports/payment_form.xml",
        "account_form/reports/payment_receipt_form.xml",
        "account_form/reports/invoice_form.xml",
        "purchase_form/datas/paper_format.xml",
        "purchase_form/datas/report_data.xml",
        "purchase_form/reports/purchase_form.xml",
        "sale_order_form/datas/paper_format.xml",
        "sale_order_form/datas/report_data.xml",
        "sale_order_form/reports/sale_order_form.xml",
        "sale_order_form/reports/sale_order_performa_invoice_form.xml",
    ],
    "installable": True,
}
