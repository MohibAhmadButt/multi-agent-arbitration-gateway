import streamlit as st
import os
from dotenv import load_dotenv
from pypdf import PdfReader  # Native text processing
load_dotenv()

from app.pipeline import run_industry_pipeline

st.set_page_config(page_title="Arbitration Engine Workspace", page_icon="🛡️", layout="wide")

st.title("🛡️ Multi-Agent Arbitration Engine Workspace")
st.markdown("A performance-optimized multi-agent validation gateway running **Llama 3.3 70B** and **Gemini 1.5 Flash** concurrently.")

# SIDEBAR: Mode & Security Controls
with st.sidebar:
    st.header("⚙️ Workspace Options")
    selected_mode = st.selectbox("🎯 Target Domain", ["Legal", "Medical", "E-commerce"])
    
    st.divider()
    st.header("🔑 Connection Health")
    if os.environ.get("GROQ_API_KEY") and os.environ.get("GEMINI_API_KEY"):
        st.success(f"{selected_mode} Agents Online")
    else:
        st.error("API Keys Unlinked")

# UI UPGRADE: PDF File Uploader Integration
uploaded_file = st.file_uploader("📥 Drag & drop or upload a document (.txt, .pdf)", type=["pdf", "txt"])

extracted_text = ""
if uploaded_file is not None:
    if uploaded_file.name.endswith(".pdf"):
        # Extract pages using local open-source library
        pdf_reader = PdfReader(uploaded_file)
        for page in pdf_reader.pages:
            extracted_text += page.extract_text() + "\n"
    else:
        extracted_text = uploaded_file.getvalue().decode("utf-8")
    
    st.success(f"Successfully processed: {uploaded_file.name} ({len(extracted_text)} characters identified)")
else:
    # Default visual backup prompt
    extracted_text = st.text_area("✍️ Manual Input Text Backup", value="Paste or type raw unstructured operational data records here...")

if st.button("🚀 Run Concurrent Multi-Agent Extraction"):
    if not extracted_text.strip():
        st.warning("Please insert text input data context before hitting run execution loops.")
    else:
        with st.spinner(f"Spawning asynchronous parallel instances for {selected_mode} Analysis..."):
            try:
                result = run_industry_pipeline(extracted_text, selected_mode)
                st.success("🎉 Multi-Agent Consensus Extraction Completed Successfully!")
                
                # Render UI dynamically based on the mode layout chosen
                if selected_mode == "Legal":
                    c1, c2 = st.columns(2)
                    c1.metric("Contract ID", result.contract_title)
                    c2.metric("Programmatic Risk Profile", result.indemnity_risk_rating)
                    st.info(f"**Resolved Invoice Clearance Terms:** {result.payment_terms_days} Days")
                    
                elif selected_mode == "Medical":
                    st.subheader(f"Patient ID: {result.patient_identifier}")
                    st.write("**Identified Symptoms:**", ", ".join(result.primary_symptoms))
                    st.warning(f"**Drug Interaction Analysis:** {result.suspected_drug_interactions}")
                    
                elif selected_mode == "E-commerce":
                    st.subheader(f"Product Tracked: {result.product_name}")
                    st.metric("Lowest Competitive Unit Rate", f"PKR {result.lowest_detected_price_pkr:,.2f}")
                    st.info(f"**Competitor Shipping Estimate:** {result.competitor_shipping_timeline}")

                # Display Consensus Log across all versions
                st.subheader("🤝 Programmatic Arbitration Logs")
                if result.resolved_discrepancies:
                    for idx, disc in enumerate(result.resolved_discrepancies):
                        with st.expander(f"Conflict Resolved #{idx+1}: {disc.aspect}"):
                            st.write(f"**Agent 1 Stance (Llama 3.3):** {disc.agent_1_stance}")
                            st.write(f"**Agent 2 Stance (Gemini Flash):** {disc.agent_2_stance}")
                            st.markdown(f"**⚖️ Consensus Resolution Rationale:** *{disc.resolution_rationale}*")
                else:
                    st.write("No conflicting interpretation flags raised during multi-agent alignment phases.")

            except Exception as e:
                st.error(f"Execution Error Encountered: {str(e)}")