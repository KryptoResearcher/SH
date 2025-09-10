from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class RelationalContext:
    """Defines the environment for legal interpretation (Def 3.6)."""
    relationship_type: str  # "corporate", "personal", "public"
    context_type: str       # "audit", "dispute", "compliance"
    jurisdiction: str
    legal_framework: str
    verdict_space: List[str] # The list of possible verdicts for this context
    # ... other fields as needed

@dataclass
class LegalSemantics:
    """Represents extracted legal meaning (Def 3.5)."""
    field_element: int        # Original field element
    verdict: str              # Base verdict from verdict_space
    contextual_meaning: str   # Context-specific interpretation
    interpretation_confidence: float
    applicable_laws: List[str]
    opposability_components: Dict[str, float]  # {'explainability': 0.8, 'contestability': 0.7, 'verifiability': 1.0}

@dataclass
class LegalTrace:
    """Captures the complete computation and interpretation history (Def 3.4)."""
    computation_trace: List[int]  # [h, f(h), f²(h), ..., fⁿ(h)]
    semantic_trace: List[LegalSemantics]  # Legal meaning at each step
    final_interpretation: LegalSemantics
    stark_proof: bytes  # Serialized proof

@dataclass
class SHParameters:
    """Parameter structure for the SH primitive (Def 3.3)."""
    field_size: int          # q
    alpha: int               # α, the quadratic non-residue
    iterations: int          # n
    security_param: int      # λ
    min_opposability: float = 0.60 # θ_min