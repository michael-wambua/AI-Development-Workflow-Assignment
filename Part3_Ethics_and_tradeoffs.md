# Part 3 – Critical Thinking

## A. Ethical Considerations and Bias in Healthcare AI (10 marks)

Artificial Intelligence (AI) in healthcare brings massive opportunities for improving diagnosis, treatment, and patient outcomes. However, with these advancements comes a great responsibility to ensure that AI systems are ethical, fair, and safe. In this section, I reflect on some of the major ethical challenges and how they are addressed in the context of building a hospital readmission prediction system.

### 1. **Bias in Training Data**

Bias in AI often begins with biased data. In healthcare, this could mean underrepresentation of certain groups—such as rural patients, women, elderly individuals, or low-income populations. If the model is trained primarily on data from urban hospitals or private facilities, it may perform poorly for patients from public or rural hospitals. This creates inequality in predictions and outcomes.

For example, if the dataset used for training consists mainly of patients between 25–45 years old, the model may fail to accurately predict readmission risks for older patients or those with chronic conditions. Such bias can lead to harmful consequences, including misdiagnosis, inappropriate discharge timing, or neglect of high-risk patients.

### 2. **Explainability and Trust**

Healthcare professionals must trust AI tools to use them in real practice. This trust cannot be built if the model behaves like a "black box." Clinicians need to understand why the AI made a certain prediction—especially when it influences critical decisions like discharge timing or resource allocation.

To ensure explainability, we applied tools such as:
- **SHAP (SHapley Additive Explanations)**: to visualize how individual features contribute to predictions.
- **LIME (Local Interpretable Model-Agnostic Explanations)**: to explain single-instance predictions in an interpretable way.

These tools help translate complex model outputs into actionable insights for medical staff.

### 3. **Privacy, Consent, and Legal Compliance**

Handling patient data demands strict privacy controls. Any AI model trained on Electronic Health Records (EHRs) or patient demographics must adhere to national and international privacy regulations.

In Kenya, the **Data Protection Act (2019)** governs how personal data must be collected, processed, stored, and shared. Additionally, globally recognized frameworks such as **HIPAA (Health Insurance Portability and Accountability Act)** provide guidance on protecting health data.

To ensure compliance:
- All datasets used in this project were anonymized.
- Personally identifiable information (PII) was removed during preprocessing.
- The data pipeline was designed to prevent leakage or exposure of sensitive information.

### 4. **Fairness and Responsible AI Practices**

To build a fair AI system:
- We used a **balanced dataset** with representation across gender, age, and geographical location.
- We monitored **fairness metrics** during evaluation to check for potential disparities.
- We documented model behavior and evaluation results to enable **accountability** and transparency.

### Summary

Ethics is not a side note in AI—it is core to deploying responsible healthcare systems. The success of AI in hospitals depends not only on accuracy but also on **fairness, trust, explainability, and compliance with law and human values**.

---

## B. Trade-offs in AI Model Development and Deployment (10 marks)

Every AI project requires making decisions between competing priorities. In a healthcare application such as hospital readmission prediction, these trade-offs must be made carefully to avoid compromising patient safety, model performance, or usability in the clinical environment.

### 1. **Accuracy vs Interpretability**

Highly accurate models like **XGBoost**, **neural networks**, or **ensemble methods** often offer superior performance on complex data. However, these models tend to be difficult to interpret. In contrast, models such as **logistic regression**, **decision trees**, or **Naive Bayes** are easier to explain but may underperform on some metrics.

In our case, we prioritized a balance between performance and transparency. **Random Forest** was chosen for its relatively high accuracy and moderate interpretability. Feature importance plots allowed us to explain model behavior to non-technical users.

### 2. **Precision vs Recall**

In hospital readmission prediction, **recall is more important than precision**. We want the model to capture as many high-risk patients as possible—even if it flags some low-risk patients incorrectly. A false negative (failing to identify a high-risk patient) can lead to a critical patient being discharged without proper follow-up.

Therefore, our evaluation focused on metrics such as:
- **Recall** (to reduce false negatives)
- **F1-score** (to balance precision and recall)
- **AUC-ROC** (to evaluate model performance across all thresholds)

### 3. **Model Complexity vs Practical Deployment**

A very complex model may offer small gains in accuracy but be hard to deploy in a real hospital system. Hospitals often have limited infrastructure and expect systems that integrate easily with existing workflows.

That’s why we prioritized a model that:
- Runs quickly
- Can be deployed via a REST API (e.g., Flask or FastAPI)
- Can be updated with new data without full retraining

This allows the hospital IT team to monitor performance, detect concept drift, and update the model in a cost-effective way.

### 4. **Computation Cost vs Sustainability**

Training deep learning models can be resource-intensive. In many Kenyan or low-resource hospital settings, using GPUs or cloud computing is not always feasible. We considered models that work well on standard hardware (CPU), and we optimized for speed without compromising essential performance.

---

### Summary

Trade-offs are not weaknesses—they are strategic decisions that reflect the **context** and **constraints** of the real-world environment. In healthcare AI, we must always ask:  
**"Does this choice help us save lives, reduce harm, and improve care?"**  
If not, we must rethink it.

---

