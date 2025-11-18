import json
import yaml

def load_json(s):
    try:
        return json.loads(s)
    except:
        return {}

def eval_condition(cond, context):
    try:
        return eval(cond, {}, context)
    except:
        return False

# Load all inputs
bundle = inputs.get("understanding_bundle", {})
metadata = bundle.get("metadata", {})
thresholds = load_json(inputs.get("thresholds_json", "{}"))
rules_yaml = yaml.safe_load(inputs.get("deterministic_rules_yaml", ""))

context = {**bundle, **metadata, "thresholds": thresholds}

rule_results = []

for rule in rules_yaml["rules"]:
    rule_id = rule["id"]
    cond = rule["condition"]
    if eval_condition(cond, context):
        rule_results.append({
            "rule_id": rule_id,
            "action": rule.get("action"),
            "reason": rule.get("desc")
        })

outputs = {
    "rule_flags": rule_results
}
