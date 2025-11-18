import json

def load_json_from_string(s):
    try:
        return json.loads(s)
    except:
        return {}

# Inputs from Opus
claims = inputs.get("claims", {})
raw_metadata = inputs.get("raw_metadata", {})
config_thresholds = load_json_from_string(inputs.get("thresholds_json", "{}"))

missing_fields = []
invalid_fields = []
pattern_flags = []

required_fields = ["timestamp", "source", "author", "location"]

# Check for missing metadata
for field in required_fields:
    if field not in raw_metadata or raw_metadata[field] in [None, "", "unknown"]:
        missing_fields.append(field)

# Example basic metadata validation
if "timestamp" in raw_metadata:
    if not isinstance(raw_metadata["timestamp"], str) or len(raw_metadata["timestamp"]) < 8:
        invalid_fields.append("timestamp_format_invalid")

# Example claim analysis integration
false_claims = 0
if isinstance(claims, list):
    for c in claims:
        if c.get("status") == "false":
            false_claims += 1

metadata_flags = {
    "missing_fields": missing_fields,
    "invalid_fields": invalid_fields,
    "false_claims": false_claims,
    "missing_count": len(missing_fields),
    "invalid_count": len(invalid_fields),
    "metadata_score": max(0, 1 - (len(missing_fields) * 0.1))
}

outputs = metadata_flags
