from typing import Dict, List, Tuple
from pathlib import Path

def enforce_provenance(concept: Dict, provenance_row: Dict) -> Tuple[bool, str]:
    """Hard gate: concept must have provenance mapping to a source_path and matching hash."""
    if not provenance_row:
        return False, "Missing provenance"
    sp = provenance_row.get("source_path")
    if not sp:
        return False, "Missing source_path in provenance"
    # Optional hash check
    c_hash = concept.get("content_hash")
    p_hash = provenance_row.get("source_sha256")
    if c_hash and p_hash and c_hash != p_hash:
        return False, "Hash mismatch between concept and provenance"
    return True, ""
