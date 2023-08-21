# Copyright 2023 The Open Source Company BV <https://tosc.nl>.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import api, fields, models

from odoo.addons.mail.models.mail_render_mixin import jinja_safe_template_env

class ResPartner(models.Model):
    """Extend res.partner with extra fields for Dutch names."""

    _inherit = "res.partner"

    initials = fields.Char()
    infix = fields.Char()

    @api.depends("firstname", "lastname", "initials", "infix")
    def _compute_name(self):
        for record in self:
            record.name = record._get_computed_name(
                record.lastname, record.firstname, record.initials, record.infix
            )

    @api.model
    def _get_computed_name(self, lastname, firstname, initials=None, infix=None):
        name_template = jinja_safe_template_env.from_string(
            self.env.context.get(
                "name_format",
                "${firstname or initials or ''}"
                "${(firstname or initials) and ' ' or ''}"
                "${infix or ''}${infix and ' ' or ''}${lastname or ''}",
            )
        )
        name = name_template.render(
            {
                "firstname": firstname,
                "lastname": lastname,
                "initials": initials,
                "infix": infix,
            }
        )
        return name if name else ""
