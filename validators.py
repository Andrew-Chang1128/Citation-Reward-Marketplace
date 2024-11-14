from web3 import Web3
import re

def validate_ethereum_address(address):
    return Web3.is_address(address)

def validate_doi(doi):
    doi_pattern = r"^10.\d{4,9}/[-._;()/:\w]+$"
    return bool(re.match(doi_pattern, doi))

def validate_paper_metadata(metadata):
    required_fields = ['title', 'authors', 'publication_date', 'doi']
    return all(field in metadata for field in required_fields)
