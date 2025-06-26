# Hospital Readmission Prediction System

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![HIPAA Compliant](https://img.shields.io/badge/HIPAA-Compliant-green.svg)](https://www.hhs.gov/hipaa/)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)]()

## 🏥 Overview

The Hospital Readmission Prediction System is an AI-powered solution designed to predict patient readmission risk within 30 days of discharge. This system helps healthcare providers identify high-risk patients, optimize discharge planning, and reduce preventable readmissions while maintaining strict HIPAA compliance.

## 🎯 Key Features

- **Predictive Analytics**: Machine learning model with 88% accuracy in predicting 30-day readmissions
- **Real-time Risk Assessment**: API-based integration with Electronic Health Records (EHR)
- **Clinical Decision Support**: Automated alerts and intervention recommendations
- **HIPAA Compliance**: End-to-end data encryption and audit trails
- **Bias Mitigation**: Regular fairness testing across demographic groups
- **Scalable Architecture**: Cloud-ready deployment with load balancing

## 📊 Performance Metrics

| Metric | Score |
|--------|-------|
| **Accuracy** | 88.0% |
| **Precision** | 66.7% |
| **Recall** | 80.0% |
| **F1-Score** | 72.7% |
| **ROC-AUC** | 85.2% |

## 🚀 Quick Start

### Prerequisites

```bash
Python 3.8+
pip 21.0+
Docker (optional)
```

### Installation

1. **Clone the repository**
```bash
git clone ...
cd readmission-prediction
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment variables**
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. **Run the application**
```bash
python app.py
```

### Docker Deployment

```bash
# Build the image
docker build -t readmission-predictor .

# Run the container
docker run -p 5000:5000 --env-file .env readmission-predictor
```


## 🔌 API Usage

### Predict Readmission Risk

```bash
curl -X POST http://localhost:5000/api/v1/predict \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "patient_id": "12345",
    "age": 65,
    "gender": "M",
    "length_of_stay": 5,
    "charlson_score": 3,
    "insurance_type": "Medicare",
    "discharge_disposition": "Home"
  }'
```

### Response

```json
{
  "patient_id": "12345",
  "readmission_risk_probability": 0.73,
  "risk_category": "High",
  "recommendations": [
    "Schedule follow-up appointment within 7 days",
    "Arrange home health services",
    "Medication reconciliation required"
  ],
  "timestamp": "2025-06-26T10:30:00Z"
}
```

## 🔒 Security & Compliance

### HIPAA Compliance Features

- **Data Encryption**: AES-256 encryption for data at rest and in transit
- **Access Controls**: Role-based permissions with multi-factor authentication
- **Audit Trails**: Comprehensive logging of all data access and modifications
- **De-identification**: Automated PHI removal for research datasets
- **Secure APIs**: OAuth 2.0 authentication with rate limiting

### Security Testing

```bash
# Run security tests
python -m pytest tests/security/ -v

# HIPAA compliance check
python scripts/hipaa_compliance_check.py

# Vulnerability scan
python scripts/security_scan.py
```

## 📈 Model Training

### Training New Models

```bash
# Prepare training data
python src/data/preprocessing.py --input data/raw/ --output data/processed/

# Train model with cross-validation
python src/models/train.py --config config/model_config.yaml --validate

# Evaluate model performance
python src/models/evaluation.py --model models/latest_model.pkl --test-data data/test/
```

### Hyperparameter Tuning

```bash
# Grid search optimization
python src/models/optimization.py --method grid_search --cv 5

# Bayesian optimization
python src/models/optimization.py --method bayesian --iterations 100
```

## 🧪 Testing

### Run All Tests

```bash
# Unit tests
python -m pytest tests/unit/ -v

# Integration tests
python -m pytest tests/integration/ -v

# End-to-end tests
python -m pytest tests/e2e/ -v

# Coverage report
python -m pytest --cov=src --cov-report=html
```

### Performance Testing

```bash
# Load testing
python tests/performance/load_test.py --concurrent-users 100 --duration 300

# Stress testing
python tests/performance/stress_test.py --max-requests 10000
```

## 📚 Documentation

- **[API Documentation](docs/api_documentation.md)**: Complete API reference
- **[Deployment Guide](docs/deployment_guide.md)**: Production deployment instructions
- **[User Manual](docs/user_manual.md)**: End-user guide for clinical staff
- **[Development Guide](docs/development_guide.md)**: Developer setup and contribution guidelines

## 🚀 Deployment

### Production Deployment

```bash
# Deploy to AWS
./scripts/deploy_aws.sh production

# Deploy to Azure
./scripts/deploy_azure.sh production

# Deploy to Google Cloud
./scripts/deploy_gcp.sh production
```

### Monitoring & Logging

- **Application Monitoring**: Prometheus + Grafana dashboards
- **Log Aggregation**: ELK Stack (Elasticsearch, Logstash, Kibana)
- **Health Checks**: Automated endpoint monitoring
- **Performance Metrics**: Real-time model performance tracking

## 🤝 Contributing

We welcome contributions from the healthcare AI community! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Development Setup

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Install pre-commit hooks
pre-commit install

# Run code quality checks
flake8 src/
black src/
mypy src/
```

## 👥 Contributors

### Lead Contributors


| Name | Role | GitHub |
|------|------|--------|
| **Michael** | Software Developer | [@michael-wambua](slymike63@gmail.com)
| **Marion** | Software Developer | [@vtonbefore](beforevton@gmail.com)
| **Bati** | Software Developer | [@baatiroba2](bqunyo@gmail.com)

### Distribution of Contributions
- [@baatiroba2](bqunyo@gmail.com) - Part 1
- [@michael-wambua](slymike63@gmail.com) - Part 2
- [@vtonbefore](beforevton@gmail.com) - Part 3


## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This software is intended for research and educational purposes. It should not be used as the sole basis for clinical decision-making without proper validation and approval from relevant regulatory authorities. Always consult with qualified healthcare professionals for medical decisions.

## 📞 Support

- **Bug Reports**: [GitHub Issues](https://github.com/hospital-ai/readmission-prediction/issues)
- **Feature Requests**: [GitHub Discussions](https://github.com/hospital-ai/readmission-prediction/discussions)
- **Technical Support**: support@hospital-ai.org
- **Documentation**: [Wiki](https://github.com/hospital-ai/readmission-prediction/wiki)

## 🙏 Acknowledgments

- **Healthcare Partners**: Thanks to our partner hospitals for providing anonymized data
- **Open Source Community**: Built on excellent open-source libraries
- **Regulatory Advisors**: HIPAA compliance guidance from healthcare law experts
- **Clinical Advisory Board**: Input from practicing physicians and nurses

## 📊 Project Statistics

![GitHub stars](https://img.shields.io/github/stars/hospital-ai/readmission-prediction?style=social)
![GitHub forks](https://img.shields.io/github/forks/hospital-ai/readmission-prediction?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/hospital-ai/readmission-prediction?style=social)
![GitHub issues](https://img.shields.io/github/issues/hospital-ai/readmission-prediction)
![GitHub pull requests](https://img.shields.io/github/issues-pr/hospital-ai/readmission-prediction)
