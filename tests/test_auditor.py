import os
import pytest
from deepeval import assert_test
from deepeval.test_case import LLMTestCase
from deepeval.metrics import FaithfulnessMetric
from app.pipeline import run_contract_audit_pipeline

def test_production_audit_workflow():
    sample_contract = (
        "Enterprise Agreement. Section 9: Total liability under this agreement "
        "is capped completely at $10,000. Section 14: All net invoices must be fully "
        "cleared within 45 days from receipt."
    )
    
    structured_result = run_contract_audit_pipeline(sample_contract)
    serialized_output_text = structured_result.model_dump_json()

    test_case = LLMTestCase(
        input="Audit the provided contract payload for liability and payment structures.",
        actual_output=serialized_output_text,
        retrieval_context=[sample_contract]
    )

    faithfulness = FaithfulnessMetric(threshold=0.6)
    assert_test(test_case, [faithfulness])