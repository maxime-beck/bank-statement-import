# -*- coding: utf-8 -*-
"""Class to parse camt files."""
# © 2017 Compassion CH <http://www.compassion.ch>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp.addons.account_bank_statement_import_camt.camt import CamtParser


class CamtDetailsParser(CamtParser):
    """Parser for camt bank statement import files."""

    def parse_transaction_details(self, ns, node, transaction):
        """Parse transaction details (message, party, account...)."""
        super(CamtDetailsParser, self).parse_transaction_details(
            ns, node, transaction)

        # remote party values
        party_type = 'Dbtr'
        party_type_node = node.xpath(
            '../../ns:CdtDbtInd', namespaces={'ns': ns})
        if party_type_node and party_type_node[0].text != 'CRDT':
            party_type = 'Cdtr'
        address_node = node.xpath(
            './ns:RltdPties/ns:%s/ns:PstlAdr' % party_type,
            namespaces={'ns': ns})
        if address_node and not transaction.get('partner_address'):
            address_values = list()
            street_node = address_node[0].xpath(
                './ns:StrtNm', namespaces={'ns': ns})
            if street_node:
                address_values.append(street_node[0].text)
            building_node = address_node[0].xpath(
                './ns:BldgNb', namespaces={'ns': ns})
            if building_node:
                address_values.append(building_node[0].text)
            zip_node = address_node[0].xpath(
                './ns:PstCd', namespaces={'ns': ns})
            if zip_node:
                address_values.append(zip_node[0].text)
            city_node = address_node[0].xpath(
                './ns:TwnNm', namespaces={'ns': ns})
            if city_node:
                address_values.append(city_node[0].text)
            transaction['partner_address'] = ', '.join(address_values)

        # Transfer account info in fields
        transaction['partner_account'] = transaction.get('account_number')
        transaction['partner_bic'] = transaction.get('account_bic')
