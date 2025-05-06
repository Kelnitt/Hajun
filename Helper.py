import tensorflow_data_validation as tfdv

def AnomaliesValidation(stats, schemas):
  """
  TensorFlow Data Validation Anomalies Validation
  """
  anomalies = tfdv.validate_statistics(stats, schemas)
  total = len(anomalies.anomaly_info.items())
  if total == 0:
    return total
  tfdv.display_anomalies(anomalies)