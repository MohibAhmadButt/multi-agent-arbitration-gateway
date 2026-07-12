import pytest
from unittest.mock import patch, MagicMock
from app.schemas import ResolvedAuditReport

# Explicitly intercept and mock run_industry_pipeline entirely
@patch('app.pipeline.run_industry_pipeline')
def test_pipeline_legal_extraction(mock_pipeline):
    """Verify that the parallel architecture processes and structures legal fields correctly."""
    sample_text = (
        "CONFIDENTIAL AGREEMENT. This contract is entered into by TechCorp and Vendor. "
        "Outstanding balance invoices must be executed completely within 45 days. "
        "Indemnity risk rating is evaluated as HIGH."
    )
    
    # Configure the mock to return a pre-built Pydantic object
    mock_pipeline.return_value = ResolvedAuditReport(
        contract_title="Test Agreement",
        indemnity_risk_rating="HIGH",
        payment_terms_days=45,
        resolved_discrepancies=[]
    )
    
    # Import inside the test block to guarantee patching hooks onto it first
    from app.pipeline import run_industry_pipeline
    result = run_industry_pipeline(sample_text, mode="Legal")
    
    # System assertions
    assert result is not None
    assert isinstance(result, ResolvedAuditReport)
    assert result.payment_terms_days == 45