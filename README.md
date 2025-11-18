# Slop Detector: Cross-Media AI, Misinformation & Manipulation Detection


# OVERVIEW 👇



Slop Detector is a full end-to-end Intake → Understand → Decide → Review → Deliver automation built using Opus, designed to detect:

            AI-generated text
            
            Misinformation
            
            Manipulated images
            
            Linguistic anomalies
            
            Missing or fabricated metadata
            
            High-risk signals (virality, contradictions, low confidence, manipulation patterns)

The system processes text, images, PDFs, and JSON, along with public API data, and produces a structured audit artifact with full transparency across all decisions.

The workflow is reusable for industries such as:

Social media verification (Instagram Reels, TikTok, Twitter/X)
            
            Newsroom content validation
            
            Document fraud detection
            
            Compliance and risk
            
            Content authenticity screening

Key Features
✔ Multi-Format Intake
            
            Accepts:
            
            PDFs
            
            Images
            
            Text
            
            JSON records
            
            Public API data

✔ Modular AI Pipeline

        Includes specialized Agents for:
        
        AI-likelihood detection
        
        Linguistic anomaly detection
        
        Image manipulation / AI generation
        
        Claim extraction
        
        Metadata validation

✔ Deterministic + AI Decisioning

            Combination of:
            
            Threshold rules
            
            Weighted scoring engine
            
            Human-review fallback
            
            Agentic policy review

✔ Full Audit & Traceability

Each workflow run generates:

            Final risk score
            
            Triggered rules
            
            Rationale + model outputs
            
            Provenance
            
            Human/agent review logs

# Opus Workflow Architecture
# 1. Intake Stage

            Nodes:
            
            Multi-Format Input Node
            
            Data Import Node (Public API)
            
            Parallel Split →
            
            Branch A: Text Extraction
            
            Branch B: Image Analysis
            
            Branch C: Metadata / Claims

# 2. Understand Stage

            OCR
            
            AI-likelihood Agent
            
            Linguistic anomaly Agent
            
            Image detection Agent
            
            Claim check Agent
            
            Metadata rules (Python)
            
            Aggregator Node → understanding_bundle

# 3. Decide Stage

            Deterministic Rules Engine (Python)
            
            Scoring Engine (Python)
            
            Decision Node (Auto Approve / Agent Review / Human Review)

# 4. Review Stage

            Agentic Policy Review
            
            Human Review Node (override supported)

# 5. Deliver Stage

            Audit JSON Generator (Python)
            
            Send to: Google Sheets / Email / JSON Export

# How to Use
1. Upload Prompts to Opus

            In each Agent Node, attach the matching .txt file from the /prompts folder.

2. Attach Configs to Python Nodes

            Upload scoring_engine.py into the scoring Python node
            
            Upload deterministic_evaluator.py into deterministic rules node
            
            Upload metadata_rules.py for metadata checks
            
            Upload audit_json_generator.py for audit output

3. Build Nodes in Opus

            Follow the included PDF in /docs/instructions.pdf which contains:
            
            Node-by-node wiring
            
            Input/output mapping
            
            Parallel branches
            
            Review flow
            
            Delivery setup

4. Test with Sample Data

            Use files from /data/examples to test:
            
            Text
            
            Images
            
            Mixed-media inputs

5. Export Audit Results

            Final step:
            
            audit.json
            
            delivered to email/sheets
            
            final risk score + verdict
