# Copyright 2023 The Open Source Company BV <https://tosc.nl>.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "Dutch partner names",
    "version": "14.0.1.0.0",
    "summary": "Adapt parter names to Dutch conventions (support infix)",
    "author": "The Open Source Company BV, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/l10n-netherlands",
    "category": "Contact management",
    "depends": ["partner_firstname"],
    "data": ["views/res_partner.xml", "data/ir.config_parameter.xml"],
    "installable": True,
    "license": "AGPL-3",
}
