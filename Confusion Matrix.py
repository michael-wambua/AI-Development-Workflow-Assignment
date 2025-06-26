# Hypothetical confusion matrix based on realistic hospital data
def create_hypothetical_confusion_matrix():
    """
    Create hypothetical confusion matrix for demonstration
    Assumes 1000 test patients with 20% readmission rate
    """
    # True Negatives: 720, False Positives: 80
    # False Negatives: 40, True Positives: 160
    cm = np.array([[720, 80],   # Not readmitted: 720 correct, 80 false alarms
                   [40, 160]])   # Readmitted: 40 missed, 160 caught
    
    return cm

def calculate_metrics(cm):
    """
    Calculate precision, recall, and other metrics from confusion matrix
    """
    tn, fp, fn, tp = cm.ravel()
    
    # Calculate metrics
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    specificity = tn / (tn + fp)
    accuracy = (tp + tn) / (tp + tn + fp + fn)
    f1_score = 2 * (precision * recall) / (precision + recall)
    
    metrics = {
        'Precision': precision,
        'Recall (Sensitivity)': recall,
        'Specificity': specificity,
        'Accuracy': accuracy,
        'F1-Score': f1_score
    }
    
    return metrics

# Generate hypothetical results
cm_hypothetical = create_hypothetical_confusion_matrix()
metrics = calculate_metrics(cm_hypothetical)

print("Confusion Matrix:")
print("                Predicted")
print("Actual          No Readmit  Readmit")
print(f"No Readmit      {cm_hypothetical[0,0]}        {cm_hypothetical[0,1]}")
print(f"Readmit         {cm_hypothetical[1,0]}         {cm_hypothetical[1,1]}")
print("\nPerformance Metrics:")
for metric, value in metrics.items():
    print(f"{metric}: {value:.3f}")

# Visualize confusion matrix
def plot_confusion_matrix(cm):
    """
    Plot confusion matrix heatmap
    """
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=['No Readmission', 'Readmission'],
                yticklabels=['No Readmission', 'Readmission'])
    plt.title('Confusion Matrix - 30-Day Readmission Prediction')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.show()