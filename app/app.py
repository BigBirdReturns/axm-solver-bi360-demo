import os
from pathlib import Path
import streamlit as st

from axm_core import CompiledStore, enforce_provenance

st.set_page_config(page_title="Solver BI360 AXM Demo", layout="wide")

st.title("Solver BI360 AXM Demo")
st.caption("Deterministic, source-cited answers for Solver BI360 workflows. No generation at query time.")

compiled_dir = Path(os.environ.get("COMPILED_DIR", "knowledge/compiled/solver-finance-mini"))

with st.sidebar:
    st.header("Library")
    st.write(f"Compiled dir: `{compiled_dir}`")
    top_k = st.slider("Top results", 1, 8, 5)
    refusal_threshold = st.slider("Refusal threshold (score)", 0.0, 50.0, 5.0, 0.5)
    st.divider()
    st.header("Optional local LLM hook")
    st.write("Off by default. When enabled, the model may only rewrite retrieved text, not invent facts.")
    use_llm = st.toggle("Enable local LLM rewriting", value=False)
    llm_note = st.text_input("Local LLM endpoint (optional)", value=os.environ.get("LOCAL_LLM_URL", ""))

@st.cache_resource
def load_store(path: Path) -> CompiledStore:
    return CompiledStore(path)

try:
    store = load_store(compiled_dir)
except Exception as e:
    st.error(f"Failed to load compiled library: {e}")
    st.stop()

query = st.text_input("Ask a Solver BI360 question", placeholder="Example: How do I set up drill-down in my report?")

examples = [
    "How do I set up drill-down in my report?",
    "Why is my data not refreshing?",
    "How do intercompany eliminations work?",
    "What's the difference between live and static database?",
    "How do I lock a period after month-end close?",
    "How do I connect QuickBooks to the data warehouse?",
    "What's the recommended month-end close sequence?",
    "How do I create a rolling 12-month report?",
]
with st.expander("Sample questions"):
    for q in examples:
        if st.button(q, key=q):
            query = q
            st.experimental_rerun()

if not query:
    st.stop()

hits = store.search(query, k=top_k)

if not hits or hits[0].score < refusal_threshold:
    st.warning("I cannot answer from this local library.")
    st.stop()

st.subheader("Results")

for i, hit in enumerate(hits, start=1):
    c = hit.concept
    prov = store.provenance.get(c.get("id"))
    ok, reason = enforce_provenance(c, prov)
    if not ok:
        continue

    with st.container(border=True):
        st.markdown(f"### {i}. {c.get('title','(untitled)')}")
        st.write(hit.excerpt)
        st.caption(f"Score: {hit.score:.2f}")

        sp = prov.get("source_path", "")
        st.markdown("**Source citation**")
        st.code(sp, language="text")

        with st.expander("Show full source text (from compiled library)"):
            st.text(c.get("summary", ""))

if use_llm:
    st.info("Local LLM rewriting is enabled, but this demo does not call an LLM by default. Wire this to your local runtime when needed.")
