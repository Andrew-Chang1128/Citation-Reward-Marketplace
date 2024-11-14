import hashlib
from datetime import datetime

class PaperService:
    def __init__(self, db):
        self.db = db
        
    def register_paper(self, title, doi, author_address, metadata):
        paper_hash = self._generate_paper_hash(title, doi)
        paper = {
            "hash": paper_hash,
            "title": title,
            "doi": doi,
            "author_address": author_address,
            "metadata": metadata,
            "timestamp": datetime.utcnow(),
            "citations": []
        }
        return self.db.papers.insert_one(paper)
    
    def _generate_paper_hash(self, title, doi):
        content = f"{title}{doi}".encode()
        return hashlib.sha256(content).hexdigest()
