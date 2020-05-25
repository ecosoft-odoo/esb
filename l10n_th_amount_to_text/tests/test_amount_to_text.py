# Copyright 2020 Ecosoft Co., Ltd (http://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

from odoo.tests.common import SavepointCase


class TestAmountToText(SavepointCase):
    def test_currency_th_amount_to_text(self):
        """ verify that amount_to_text converted text to thai language """
        currency = self.env.ref("base.THB")
        amount_text_en = currency.amount_to_text(1050.75)
        self.assertEqual(
            amount_text_en, "One Thousand And Fifty Baht and Seventy-Five Satang"
        )
        currency.with_context({"lang": "th_TH"}).amount_to_text(1050.75)
        # num2words need version 0.5.7+
        # amount_text_th = currency.with_context({"lang": "th_TH"}).amount_to_text(
        #     1050.75
        # )
        # self.assertEqual(amount_text_th, "หนึ่งพันห้าสิบบาทเจ็ดสิบห้าสตางค์")

    def test_currency_eur_amount_to_text(self):
        """ verify that amount_to_text works as expected """
        currency = self.env.ref("base.EUR")
        amount_text_eur = currency.amount_to_text(1050.75)
        self.assertEqual(
            amount_text_eur, "One Thousand And Fifty Euros and Seventy-Five Cents"
        )
