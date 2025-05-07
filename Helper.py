import tensorflow_data_validation as tfdv
from tensorflow_metadata.proto.v0 import schema_pb2
from typing import List, Optional

def AnomaliesValidation(stats, schemas, display):
  """
  TensorFlow Data Validation Anomalies Validation
  """
  anomalies = tfdv.validate_statistics(stats, schemas)
  total = len(anomalies.anomaly_info.items())
  if display and total > 0:
    tfdv.display_anomalies(anomalies)
  return total

def SelectColSchemas(schema : schema_pb2.Schema, columns : List[str], display : bool):
  """
  Select Partially Schemas
  """
  partial_schema = schema_pb2.Schema()
  missing_columns = []
  for cols in columns:
    feature = tfdv.get_feature(schema, cols)
    if feature:
      partial_schema.feature.add().CopyFrom(feature)
    else:
      missing_columns.append(cols)
  if missing_columns:
    raise ValueError(f"The Following Cols Unavailable in Schema : {missing_columns}")
  if display:
    tfdv.display_schema(partial_schema)
  return partial_schema
