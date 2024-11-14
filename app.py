from flask import Flask
from flask_pymongo import PyMongo
from routes import api
from config import Config

app = Flask(__name__)
app.config['MONGO_URI'] = Config.MONGODB_URI
mongo = PyMongo(app)

# Initialize services
blockchain_service = BlockchainService()
paper_service = PaperService(mongo.db)
citation_service = CitationService(mongo.db, blockchain_service)

# Register blueprints
app.register_blueprint(api, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
