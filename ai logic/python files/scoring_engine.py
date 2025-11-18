import json

def load_json(s):
    try:
        return json.loads(s)
    except:
        return {}

bundle = inputs.get("understanding_bundle", {})
metadata = bundle.get("metadata", {})

config = load_json(inputs.get("scoring_config_json", "{}"))

weights = config.get("weights", {})
normalize = config.get("normalization", {})
penalties_cfg = config.get("penalties", {})
thresholds = config.get("thresholds", {})

def normalize_value(value, scale):
    if scale == "0-1":
        return value
    if scale == "0-5":
        return value / 5
    if scale == "0-100":
        return value / 100
    return value

score = 0.0

features = {
    "ai_likelihood": bundle.get("ai_likelihood", 0),
    "linguistic_anomaly": bundle.get("linguistic_anomaly", 0),
    "misinformation_risk": bundle.get("misinformation_risk", 0),
    "manipulation_likelihood": bundle.get("manipulation_likelihood", 0),
    "fact_check_false_ratio": bundle.get("fact_check_false_ratio", 0),
    "missing_metadata_penalty": metadata.get("missing_count", 0),
    "virality_score": bundle.get("virality_score", 0)
}

# Weighted sum
for key, weight in weights.items():
    raw_val = features.get(key, 0)
    norm = normalize_value(raw_val, normalize.get(key, "0-1"))
    score += weight * norm

# Penalties
penalty = 0

for field, val in metadata.items():
    if field in penalties_cfg.get("missing_metadata", {}):
        penalty += penalties_cfg["missing_metadata"][field]

score = max(0, min(100, score * 100 - penalty))

outputs = {
    "final_risk_score": score
}
