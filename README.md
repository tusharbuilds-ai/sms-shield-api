# 🛡️ SMS Shield API

An AI-powered FastAPI backend for intelligent SMS spam detection and multilingual message analysis. This API serves as the backend for the SMS Shield Android application, providing spam classification and AI-generated explanations for incoming SMS messages.

---

## 🚀 Features

- 🤖 AI-powered SMS analysis
- 🚫 Spam and legitimate message detection
- 🌍 Multilingual support
- ⚡ High-performance REST API built with FastAPI
- 📱 Designed for Android integration
- 🐳 Docker support
- 📖 Interactive Swagger API documentation

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3.12 | Programming Language |
| FastAPI | REST API Framework |
| Uvicorn | ASGI Server |
| Pydantic | Data Validation |
| uv | Dependency Management |
| AI/LLM | Message Explanation |

---

## 📂 Project Structure

```text
sms-shield-api/
│
├── app/
│   ├── api/
│   ├── schemas/
│   ├── services/
│   ├── utils/
│   ├── core/
│   └── main.py
│
├── pyproject.toml
├── uv.lock
├── Dockerfile
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/tusharbuilds-ai/sms-shield-api.git
```

Move into the project directory

```bash
cd sms-shield-api
```

Install dependencies

```bash
uv sync
```

Run the development server

```bash
uv run uvicorn main:app --reload
```

---

## 🐳 Docker

Build the Docker image

```bash
docker build -t sms-shield-api .
```

Run the container

```bash
docker run -p 8000:8000 sms-shield-api
```

The API will be available at

```
http://localhost:8000
```

---

## 📖 API Documentation

FastAPI automatically generates interactive API documentation.

Swagger UI

```
http://localhost:8000/docs
```

ReDoc

```
http://localhost:8000/redoc
```

---

## 📡 API Endpoint

### Analyze SMS

**POST**

```
/api/v1/analyze
```

### Request

```json
{
  "sender": "VK-BANK",
  "message": "Congratulations! You won ₹1,00,000.",
  "language": "English"
}
```

### Response

```json
{
  "status_code": 200,
  "status": true,
  "message": "Message analyzed!",
  "data": {
    "AI Explanation": "This message appears suspicious because..."
  }
}
```

---

## 📱 Android Integration

This API is designed to work seamlessly with the SMS Shield Android application.

Workflow

```text
Incoming SMS
      │
      ▼
Android App
      │
      ▼
FastAPI Backend
      │
      ▼
AI Analysis
      │
      ▼
JSON Response
      │
      ▼
Android UI
```

---

## 🔒 Security

- Request validation using Pydantic
- Structured JSON responses
- Exception handling
- Modular architecture
- Easy to extend with authentication and rate limiting

---

## 📌 Future Enhancements

- User authentication
- Message history
- Analytics dashboard
- Cloud deployment
- Multiple AI model support
- Batch SMS analysis
- Real-time notifications

---

## 📄 License

This project is licensed under the MIT License.
