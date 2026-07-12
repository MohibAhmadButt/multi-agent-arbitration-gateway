import pytest
from app.pipeline import run_industry_pipeline
from app.schemas import ResolvedAuditReport

def test_pipeline_legal_extraction():
    """Verify that the parallel architecture successfully falls back and extracts legal fields correctly."""
    sample_text = (
        "CONFIDENTIAL AGREEMENT. This contract is entered into by TechCorp and Vendor. "
        "Outstanding balance invoices must be executed completely within 45 days. "
        "Indemnity risk rating is evaluated as HIGH."
    )
    
    # Run the updated multi-mode pipeline function targeting 'Legal'
    result = run_industry_pipeline(sample_text, mode="Legal")
    
    # Assertions to ensure the validation schema populates correctly
    assert result is not None
    assert isinstance(result, ResolvedAuditReport)
    assert result.payment_terms_days == 45