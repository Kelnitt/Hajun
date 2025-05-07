import tensorflow_data_validation as tfdv
from tensorflow_metadata.proto.v0 import schema_pb2
from typing import List, Optional

def AnomaliesValidation(stats, schemas, display):
  """
  TensorFlow Data Validation Anomalies Validation
  """
  # Validate Stats
  anomalies = tfdv.validate_statistics(stats, schemas)
  total = len(anomalies.anomaly_info.items())
  # Display Anomalies
  if display and total > 0:
    tfdv.display_anomalies(anomalies)
  return total

def SelectColSchemas(schema : schema_pb2.Schema, columns : List[str], display : bool):
  """
  Select Partially Schemas
  """
  partial_schema = schema_pb2.Schema()
  missing_columns = []
  # Validate Available Column
  for cols in columns:
    feature = tfdv.get_feature(schema, cols)
    if feature:
      partial_schema.feature.add().CopyFrom(feature)
    else:
      missing_columns.append(cols)
  # Raise Value Error
  if missing_columns:
    raise ValueError(f"The Following Cols Unavailable in Schema : {missing_columns}")
  # Display Schema
  tfdv.display_schema(partial_schema)
