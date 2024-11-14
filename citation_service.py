import requests
from config import Config

class CitationService:
    def __init__(self, db, blockchain_service):
        self.db = db
        self.blockchain_service = blockchain_service
    
    async def verify_citation(self, citing_doi, cited_doi):
        # Verify citation using CrossRef API
        response = requests.get(f"{Config.CROSSREF_API}{citing_doi}")
        if response.status_code == 200:
            data = response.json()
            references = data.get('references', [])
            return cited_doi in [ref.get('DOI') for ref in references]
        return False
    
    def record_verified_citation(self, citing_paper, cited_paper):
        return self.db.citations.insert_one({
            "citing_paper": citing_paper,
            "cited_paper": cited_paper,
            "verified": True,
            "timestamp": datetime.utcnow()
        })
