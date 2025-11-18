AI-Genesis-Hackathon-Project
OPUS Workflow Automation
Overview!
(https://github.com/user-attachments/assets/b73b50e9-022a-413c-b1e9-2b7decbe6275)


This repository contains a complete OPUS workflow for multi-format data ingestion, text and image analysis, metadata and claim verification, risk scoring, and automated decision routing. The workflow integrates external data and supports automated, agentic, and human review paths. All prompts, configuration files, scripts, and workflow details are included.
Workflow Structure

    Multi-Format Intake

Node Type: Input Node

Fields: raw_text (string), raw_image (file), raw_file (file), raw_json (JSON)

    Data Import

Node Type: Data Import

Input: Public API / mock JSON

Output: external_data

    Parallel Processing

Branches:

A — Text Extraction

OCR/Text Extraction → extracted_text

AI Likelihood Analysis → ai_likelihood_output

Linguistic Anomaly Analysis → linguistic_output

B — Image Analysis

OCR/Image-to-Text → image_text

Image Detection → image_ai_output

C — Metadata & Claims

Claim Verification → claims

Metadata Rule Engine → metadata_flags

    Aggregation

Node Type: Aggregator

Input: Outputs from all branches + external data

Output: understanding_bundle

    Decision Stage

Deterministic Rules Engine → rule_flags

Scoring Engine → final_risk_score

Risk Routing Decision Node: routes items to human review, agentic review, or auto-delivery based on conditions.

    Review Stage

Agentic Review → agentic_review_output

Human Review Fields: decision, reviewer_comment, timestamp, override (yes/no)

    Delivery Stage

Audit JSON Generation → final_risk_score (audited)

Delivery Options: Google Sheets, Email, JSON Export → final_deliver
Usage

Ingest multi-format files (text, images, JSON, files) via the input nodes.

Workflow executes parallel processing, decision routing, and review stages automatically.

Review results through delivery outputs, either automatically or via agentic/human review.

Audit JSON files provide full traceability of decisions and scoring.
