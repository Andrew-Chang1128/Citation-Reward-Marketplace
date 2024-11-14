from web3 import Web3

class Config:
    # Web3 settings
    WEB3_PROVIDER = "http://localhost:8545"
    CONTRACT_ADDRESS = "YOUR_CONTRACT_ADDRESS"
    
    # API settings
    CROSSREF_API = "https://api.crossref.org/works/"
    GOOGLE_SCHOLAR_API = "YOUR_GOOGLE_SCHOLAR_API"
    
    # Database settings
    MONGODB_URI = "mongodb://localhost:27017/citation_marketplace"
    
    # JWT settings
    JWT_SECRET_KEY = "your-secret-key"
    JWT_ACCESS_TOKEN_EXPIRES = 3600
