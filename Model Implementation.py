from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

def train_readmission_model(X, y):
    """
    Train Random Forest model for readmission prediction
    """
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    # Initialize Random Forest with optimized hyperparameters
    rf_model = RandomForestClassifier(
        n_estimators=100,          # Number of trees
        max_depth=10,              # Maximum depth to prevent overfitting
        min_samples_split=10,      # Minimum samples to split a node
        min_samples_leaf=5,        # Minimum samples in leaf node
        max_features='sqrt',       # Number of features for best split
        random_state=42,
        class_weight='balanced'    # Handle class imbalance
    )
    
    # Train the model
    rf_model.fit(X_train, y_train)
    
    # Make predictions
    y_pred = rf_model.predict(X_test)
    y_pred_proba = rf_model.predict_proba(X_test)[:, 1]
    
    return rf_model, y_test, y_pred, y_pred_proba

def evaluate_model_performance(y_true, y_pred):
    """
    Comprehensive model evaluation
    """
    # Generate classification report
    print("Classification Report:")
    print(classification_report(y_true, y_pred))
    
    # Calculate confusion matrix
    cm = confusion_matrix(y_true, y_pred)
    return cm