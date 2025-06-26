from sklearn.model_selection import StratifiedKFold, validation_curve
from sklearn.metrics import roc_auc_score
import matplotlib.pyplot as plt

def implement_cross_validation_optimization(X, y):
    """
    Implement k-fold cross-validation to prevent overfitting
    """
    # Initialize stratified k-fold to maintain class distribution
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    
    # Hyperparameter optimization with cross-validation
    param_range = [50, 100, 150, 200, 250]
    train_scores, validation_scores = validation_curve(
        RandomForestClassifier(random_state=42),
        X, y,
        param_name='n_estimators',
        param_range=param_range,
        cv=skf,
        scoring='roc_auc',
        n_jobs=-1
    )
    
    # Calculate mean and standard deviation
    train_mean = np.mean(train_scores, axis=1)
    train_std = np.std(train_scores, axis=1)
    val_mean = np.mean(validation_scores, axis=1)
    val_std = np.std(validation_scores, axis=1)
    
    # Plot validation curves
    plt.figure(figsize=(10, 6))
    plt.plot(param_range, train_mean, 'o-', color='blue', label='Training Score')
    plt.fill_between(param_range, train_mean - train_std, train_mean + train_std, alpha=0.1, color='blue')
    plt.plot(param_range, val_mean, 'o-', color='red', label='Validation Score')
    plt.fill_between(param_range, val_mean - val_std, val_mean + val_std, alpha=0.1, color='red')
    
    plt.xlabel('Number of Estimators')
    plt.ylabel('ROC AUC Score')
    plt.title('Validation Curve for Random Forest')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    # Select optimal number of estimators
    optimal_estimators = param_range[np.argmax(val_mean)]
    
    return optimal_estimators

def early_stopping_training(X_train, y_train, X_val, y_val):
    """
    Implement early stopping during model training
    """
    best_score = 0
    patience = 10
    patience_counter = 0
    best_model = None
    
    # Incrementally train models with increasing complexity
    for n_estimators in range(10, 201, 10):
        model = RandomForestClassifier(
            n_estimators=n_estimators,
            random_state=42,
            max_depth=10,
            min_samples_split=10
        )
        
        model.fit(X_train, y_train)
        val_predictions = model.predict_proba(X_val)[:, 1]
        val_score = roc_auc_score(y_val, val_predictions)
        
        if val_score > best_score:
            best_score = val_score
            best_model = model
            patience_counter = 0
        else:
            patience_counter += 1
            
        # Early stopping condition
        if patience_counter >= patience:
            print(f"Early stopping at {n_estimators} estimators")
            print(f"Best validation score: {best_score:.4f}")
            break
    
    return best_model

# Additional regularization techniques
def implement_additional_regularization():
    """
    Additional methods to prevent overfitting
    """
    regularized_model = RandomForestClassifier(
        n_estimators=100,
        max_depth=8,                    # Limit tree depth
        min_samples_split=15,           # Increase minimum samples for split
        min_samples_leaf=8,             # Increase minimum samples in leaf
        max_features='sqrt',            # Limit features per split
        bootstrap=True,                 # Use bootstrap sampling
        oob_score=True,                 # Out-of-bag scoring
        random_state=42
    )
    
    return regularized_model

# Feature selection to reduce overfitting
def feature_selection_for_regularization(X, y):
    """
    Use feature selection to prevent overfitting
    """
    from sklearn.feature_selection import SelectKBest, f_classif
    
    # Select top k features based on ANOVA F-score
    selector = SelectKBest(score_func=f_classif, k=15)
    X_selected = selector.fit_transform(X, y)
    
    # Get selected feature names
    selected_features = selector.get_support(indices=True)
    
    return X_selected, selected_features