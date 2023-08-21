# Copyright 2023 The Open Source Company BV <https://tosc.nl>.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo.tests.common import TransactionCase


class TestL10nNlPartnerName(TransactionCase):
    def test_l10n_nl_partner_name(self):
        partner = self.env["res.partner"].create({"name": "Mark Rutte"})
        self.assertEqual(partner.firstname, "Mark")
        self.assertEqual(partner.lastname, "Rutte")
        partner.firstname = "Willem-Alexander"
        partner.lastname = "van Oranje-Nassau"
        self.assertEqual(partner.name, "Willem-Alexander van Oranje-Nassau")
        partner.write({"name": partner.name})
        self.assertEqual(partner.firstname, "Willem-Alexander")
        self.assertEqual(partner.lastname, "van Oranje-Nassau")
        self.assertEqual(partner.name, "Willem-Alexander van Oranje-Nassau")
