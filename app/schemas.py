from pydantic import BaseModel, Field
from typing import List

class DiscrepancyLog(BaseModel):
    aspect: str = Field(description="The point of contradiction identified between the models.")
    agent_1_stance: str = Field(description="What the first agent extracted.")
    agent_2_stance: str = Field(description="What the second agent extracted.")
    resolution_rationale: str = Field(description="Deterministic reason for how the final value was selected safely.")

# 1. LEGAL SCHEMA
class ResolvedAuditReport(BaseModel):
    contract_title: str
    indemnity_risk_rating: str = Field(description="Must be STRICTLY one of: HIGH, MEDIUM, or LOW")
    payment_terms_days: int = Field(description="The settled invoice payment deadline in days.")
    resolved_discrepancies: List[DiscrepancyLog] = Field(default_factory=list)

# 2. MEDICAL SCHEMA
class MedicalAnalysisReport(BaseModel):
    patient_identifier: str
    primary_symptoms: List[str]
    suspected_drug_interactions: str = Field(description="Strict evaluation of potential contradictions between active medications.")
    resolved_discrepancies: List[DiscrepancyLog] = Field(default_factory=list)

# 3. E-COMMERCE SCHEMA
class MarketCompetitorReport(BaseModel):
    product_name: str
    lowest_detected_price_pkr: float
    competitor_shipping_timeline: str = Field(description="The fastest standard delivery estimate found.")
    resolved_discrepancies: List[DiscrepancyLog] = Field(default_factory=list)