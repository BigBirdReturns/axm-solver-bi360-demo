import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple

_WORD_RE = re.compile(r"[A-Za-z0-9]+")

def _tokenize(text: str) -> List[str]:
    return [t.lower() for t in _WORD_RE.findall(text)]

@dataclass
class Hit:
    concept: Dict
    score: float
    excerpt: str

class CompiledStore:
    """Loads AXM compiled artifacts and provides deterministic lexical retrieval.

    This is intentionally simple and offline-friendly. It does not call an LLM.
    """
    def __init__(self, compiled_dir: Path):
        self.compiled_dir = Path(compiled_dir)
        self.concepts = self._load_jsonl(self.compiled_dir / "concepts.jsonl")
        self.provenance = self._load_provenance(self.compiled_dir / "provenance.jsonl")
        self._build_index()

    def _load_jsonl(self, path: Path) -> List[Dict]:
        rows: List[Dict] = []
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            rows.append(json.loads(line))
        return rows

    def _load_provenance(self, path: Path) -> Dict[str, Dict]:
        prov: Dict[str, Dict] = {}
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            target_id = row.get("target_id")
            if target_id:
                prov[target_id] = row
        return prov

    def _build_index(self) -> None:
        # Basic TF-IDF style scoring, deterministic.
        self.doc_tokens: List[List[str]] = []
        df: Dict[str, int] = {}
        for c in self.concepts:
            text = f"{c.get('title','')} {c.get('summary','')}"
            toks = _tokenize(text)
            self.doc_tokens.append(toks)
            seen = set(toks)
            for t in seen:
                df[t] = df.get(t, 0) + 1
        self.df = df
        self.N = max(1, len(self.concepts))

    def search(self, query: str, k: int = 5) -> List[Hit]:
        qtoks = _tokenize(query)
        if not qtoks:
            return []
        qset = set(qtoks)

        # IDF
        idf = {}
        for t in qset:
            dft = self.df.get(t, 0)
            idf[t] = 0.0 if dft == 0 else (1.0 + (self.N / dft))
        hits: List[Hit] = []
        for c, toks in zip(self.concepts, self.doc_tokens):
            if not toks:
                continue
            # term frequency
            tf = {}
            for t in toks:
                if t in qset:
                    tf[t] = tf.get(t, 0) + 1
            if not tf:
                continue
            score = 0.0
            for t, cnt in tf.items():
                score += cnt * idf.get(t, 0.0)
            excerpt = self._make_excerpt(c.get("summary",""), qset)
            hits.append(Hit(concept=c, score=score, excerpt=excerpt))
        hits.sort(key=lambda h: h.score, reverse=True)
        return hits[:k]

    def _make_excerpt(self, text: str, qset: set, max_len: int = 280) -> str:
        if not text:
            return ""
        # Find first line containing any query token
        for line in text.splitlines():
            low = line.lower()
            if any(t in low for t in qset):
                s = line.strip()
                return s[:max_len]
        return text.strip().splitlines()[0][:max_len] if text.strip() else ""
