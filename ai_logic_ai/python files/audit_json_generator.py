import json
from datetime import datetime

audit = {
    "timestamp": datetime.utcnow().isoformat(),
    "input_summary": inputs.get("intake_output", {}),
    "analysis": {
        "text": inputs.get("extracted_text", ""),
        "ai_likelihood": inputs.get("ai_likelihood_output", {}),
        "linguistic": inputs.get("linguistic_output", {}),
        "image_ai": inputs.get("image_ai_output", {}),
        "claims": inputs.get("claims", {})
    },
    "metadata": inputs.get("metadata_flags", {}),
    "rules_triggered": inputs.get("rule_flags", {}),
    "final_score": inputs.get("final_risk_score", {}),
    "review": inputs.get("agentic_review_output", {}),
    "human_review": inputs.get("human_review", {})
}

outputs = {
    "audit_json": audit
}
