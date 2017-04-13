# -*- coding: utf-8 -*-
"""Add process_camt method to account.bank.statement.import."""
# © 2017 Compassion CH <http://www.compassion.ch>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp import models, fields


class AccountBankStatementLine(models.TransientModel):
    """Add process_camt method to account.bank.statement.import."""
    _inherit = 'account.bank.statement.line'

    partner_address = fields.Char()
    partner_account = fields.Char()
    partner_bic = fields.Char()
