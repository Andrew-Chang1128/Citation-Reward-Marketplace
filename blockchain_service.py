from web3 import Web3
from config import Config

class BlockchainService:
    def __init__(self):
        self.w3 = Web3(Web3.HTTPProvider(Config.WEB3_PROVIDER))
        self.contract = self.w3.eth.contract(
            address=Config.CONTRACT_ADDRESS,
            abi=CONTRACT_ABI  # Load this from your contract JSON
        )
    
    def verify_paper_ownership(self, paper_hash, author_address, signature):
        return self.contract.functions.verifyPaperOwnership(
            paper_hash,
            author_address,
            signature
        ).call()
    
    def record_citation(self, paper_hash, citing_paper_hash, author_address):
        tx = self.contract.functions.recordCitation(
            paper_hash,
            citing_paper_hash
        ).build_transaction({
            'from': author_address,
            'nonce': self.w3.eth.get_transaction_count(author_address)
        })
        return tx
