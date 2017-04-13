# -*- coding: utf-8 -*-
"""Add process_camt method to account.bank.statement.import."""
# © 2017 Compassion CH <http://www.compassion.ch>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp import api, models
from ..camt import CamtDetailsParser as Parser


class AccountBankStatementImport(models.TransientModel):
    """Add process_camt method to account.bank.statement.import."""
    _inherit = 'account.bank.statement.import'

    @api.model
    def _get_camt_parser(self):
        return Parser()
