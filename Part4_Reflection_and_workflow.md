# Part 4 – Reflection and Workflow

## A. Reflection on the AI Workflow Project (5 marks)

Working on the hospital readmission prediction project has been a powerful learning experience. It allowed me to move beyond theoretical machine learning and apply AI concepts in a real-world, high-impact setting. I realized that successful AI systems are not only defined by their technical accuracy but also by their ability to function ethically, transparently, and sustainably.

One of the key challenges I encountered was understanding how to address fairness and bias in a practical way. Reading about bias in models is one thing—but detecting and mitigating it in actual datasets is much harder. I learned to ask critical questions: who is represented in the data? Who might be left out? How do model predictions vary across groups?

Another key takeaway was the importance of **explainability**. I had to think deeply about how to help non-technical healthcare staff understand what the model is doing and why. Tools like SHAP and LIME were extremely useful in this regard, and I now consider them essential components of responsible AI development.

I also gained hands-on experience in model selection, metric interpretation (especially precision vs recall trade-offs), and designing a clean deployment plan using APIs. I now better understand the full AI lifecycle—from data collection and preprocessing, all the way to deployment and monitoring.

If I were to do this project again, I would engage domain experts (such as nurses or doctors) earlier in the process. Their insights could improve the feature selection and interpretation of results. Overall, this project has strengthened my technical skills, broadened my ethical understanding, and prepared me to build human-centered AI systems.

---

## B. AI Workflow Diagram Description (5 marks)

The hospital readmission prediction system was developed using a clear AI workflow that followed best practices in machine learning and software development. Below is a detailed explanation of each stage in the workflow diagram.

### 1. Problem Definition
We started by clearly defining the problem: *predicting whether a patient will be readmitted within 30 days of discharge*. The objectives were to reduce preventable readmissions, optimize resource use, and improve patient care outcomes.

### 2. Data Collection
We collected data from electronic health records (EHRs), which included patient demographics, diagnosis codes, hospital stay durations, comorbidities, and historical readmission records.

### 3. Data Preprocessing
This phase involved:
- Handling missing values and inconsistent records
- Encoding categorical variables
- Normalizing numerical features
- Anonymizing sensitive data
- Checking for bias across demographics

### 4. Model Training & Selection
We experimented with several models including:
- Logistic Regression (baseline)
- Random Forest (final choice)
- XGBoost (high performance but lower explainability)

We selected **Random Forest** due to its balance between accuracy and interpretability. Cross-validation and hyperparameter tuning were used to optimize the model.

### 5. Model Evaluation
Key evaluation metrics included:
- **Recall**: prioritized to catch high-risk patients
- **F1-Score**: balance between precision and recall
- **AUC-ROC**: assess model discrimination

We also used **SHAP plots** to visualize the top contributing features in predictions.

### 6. Deployment
The model was wrapped into a **Flask API** to simulate real-world integration into a hospital’s IT system. This allowed healthcare staff to input patient data and receive readmission risk predictions in real-time.

### 7. Monitoring and Feedback
Once deployed, the system requires regular monitoring:
- Track model performance over time
- Detect **concept drift** using periodic validation
- Schedule retraining with new patient data every 3–6 months
- Collect feedback from healthcare users to improve usability

---

The visual version of this workflow is shown in the `workflow_diagram.png` file submitted alongside this document.
