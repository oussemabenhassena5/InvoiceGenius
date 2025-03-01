# InvoiceGenius API 💰

InvoiceGenius is a modern, AI-powered invoice management system built with FastAPI that helps businesses automate their invoice processing workflow.

## ✨ Features

- **AI-Powered Invoice Processing**: 
  - Extract data automatically using Azure Document Intelligence
  - Smart field detection for vendor names, dates, amounts
  - OCR processing for digital and scanned invoices

- **Smart Analysis with Azure OpenAI**: 
  - Automatic expense categorization
  - Approval status detection
  - Location and context extraction
  - Intelligent data validation

- **Comprehensive Invoice Management**:
  - Create and track invoices
  - Manage client contacts
  - Track invoice items and notes
  - Handle multiple invoice contacts
  - Full invoice lifecycle management

## 🛠️ Tech Stack

- **Framework**: FastAPI
- **Database**: MySQL with SQLModel ORM
- **AI Services**: 
  - Azure Document Intelligence
  - Azure OpenAI
- **Authentication**: JWT with bcrypt
- **Documentation**: OpenAPI (Swagger) & ReDoc
- **Migration**: Alembic

## 📋 API Endpoints

### Invoice Management
- `POST /api/invoice/create` - Create new invoice
- `GET /api/invoice/full` - Get complete invoice details
- `PUT /api/invoice/update` - Update existing invoice
- `DELETE /api/invoice/delete` - Delete invoice

### AI Processing
- `POST /api/ai-invoice/extract` - Process invoice with AI
  - Extracts vendor details, amounts, dates
  - Performs smart categorization 
  - Returns structured data

### Contact Management
- `POST /api/client-contact/create` - Create client contact
- `GET /api/client-contact/all` - List all client contacts
- `POST /api/invoice-contact/create` - Create invoice contact

## 🚀 Quick Start

1. **Clone and Install**
```bash
git clone https://github.com/yourusername/InvoiceGenius-API.git
cd InvoiceGenius-API
poetry install
```

2. **Configure Environment**
```bash
cp envs/dev.env.example envs/dev.env
# Update the following in dev.env:
# - Database credentials
# - Azure Document Intelligence credentials
# - Azure OpenAI credentials
```

3. **Setup Database**
```bash
# Start MySQL
mysql.server start

# Create and migrate database
alembic upgrade head
```

4. **Run the Application**
```bash
python -m app
```

The API will be available at:
- API: `http://localhost:8000`
- Swagger Docs: `http://localhost:8000/api/docs`
- ReDoc: `http://localhost:8000/api/redoc`

## 🔧 Configuration

Required environment variables in `dev.env`:

```env
# Database
db_type=mysql
db_user=root
db_pass=your_password
db_base=invoice_db
db_host=localhost
db_port=3306

# Azure Services
DOCUMENT_INTELLIGENCE_API_KEY=your_key
DOCUMENT_INTELLIGENCE_ENDPOINT=your_endpoint
AZURE_API_KEY=your_key
AZURE_URL=your_url
AZURE_API_VERSION=your_version
```


## 📦 Project Structure

```
InvoiceGenius-API/
├── app/
│   ├── routes/            # API endpoints
│   ├── models/           # Database models
│   ├── core/            # Core functionality
│   └── services/        # Business logic
└── alembic/            # Database migrations
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/)
- [Azure Document Intelligence](https://azure.microsoft.com/en-us/services/form-recognizer/)
- [Azure OpenAI](https://azure.microsoft.com/en-us/services/openai/)
- [SQLModel](https://sqlmodel.tiangolo.com/)

## 📞 Support

If you need help:
- Check the [documentation](http://localhost:8000/api/docs)
- Open an [issue](https://github.com/yourusername/InvoiceGenius-API/issues)
- Contact: oussemabenhassena5@gmail.com

---
Made with ❤️ by [Oussema]
