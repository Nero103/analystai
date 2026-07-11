import streamlit as st
import pandas as pd
import time
from ai_engine import analyze_text, analyze_pdf, format_report
from document_utils import extract_pdf_text
from config import MODEL, PDF_LIMIT

# ------------------
# UI
# ------------------

st.title("⬢ Moros AnalystAI")
st.markdown("## Transform Data into Decsions")
st.caption("AI-Powered Business & Document Intelligence")
st.divider()

st.markdown("""
Upload a **CSV** or **PDF**, ask a question in plain English, and receive a structured, executive insights by a local AI.

**Built for analysts, business, and decision-making.**
""")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("📈 Buiness Inteligence\n\nAnalyze CSV datasets to uncover trends, anomalies, and business insights.")

with col2:
    st.info("📄 Document Intelligence\n\nSummarize PDF reports and ask questions using local AI.")

with col3:
    st.info("💾 Executive Reporting\n\nGenerate structured reports that can be downloaded and shared")

# Sidebar for input
with st.sidebar:
    st.header("📂 Controls")
    st.caption("Configure your analysis")
    st.divider()
    uploaded_file = st.file_uploader(
        "Upload a CSV or PDF",
        type = ["csv", "pdf"]
    )

    user_question = st.text_input(
            "Ask a question about the data",
            placeholder = "Example: what stands out in this dataset?"
    )
    st.divider()
    st.markdown("### 🤖 model")
    st.info(MODEL)

# Main area
if uploaded_file is not None:
    #st.success(f"Uploaded: {uploaded_file.name}")

    # ------------------
    # CSV
    # ------------------

    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)

        st.success("✅ CSV uploaded successfully")
        st.caption(f"File: {uploaded_file.name}")

        left_col, right_col = st.columns([1, 1])

        with left_col:

            st.subheader("CSV Preview")
            st.dataframe(df.head(3))

        with right_col:

            st.subheader("🤖 AI Workspace")

            analysis_placeholder = st.empty()

            if st.button("Generate Analyst Brief"):
                with st.spinner("Analyze data..."):
                    start_time = time.perf_counter()
                    
                    question = (
                        user_question 
                        if user_question 
                        else "What stands out in this dataset?"
                    )

                    brief = analyze_text(df, question)

                    processing_time = time.perf_counter() - start_time

                st.subheader("Analysis Brief")

                st.success("✅ Analysis Complete")

                sumcol1, sumcol2, sumcol3, sumcol4, sumcol5 = st.columns(5)

                with sumcol1:
                    st.metric("File Type", "CSV")

                with sumcol2:
                    st.metric("Rows", len(df))

                with sumcol3:
                    st.metric("AI Model", MODEL)

                with sumcol4:
                    st.metric("Time", f"{processing_time:.1f}s")

                with sumcol5:
                    st.metric("Status", "Complete")

                with analysis_placeholder.container():

                    with st.container(border= True):
                        st.markdown(format_report(brief))

                st.download_button(
                    label = "Download Analysis Brief",
                    data = brief,
                    file_name = "analystai_brief.txt",
                    mime = "text/plain"
                )

    # --------------------
    # PDF Area
    #---------------------

    elif uploaded_file.name.endswith(".pdf"):

        st.success("✅ PDF uploaded successfully")
        st.caption(f"File: {uploaded_file.name}")
        

        pdf_text = extract_pdf_text(uploaded_file)

        left_col, right_col = st.columns([1, 1])

        with left_col:
            st.subheader("📄 PDF Preview")
            st.text(pdf_text[:2000])

            pdf_question = st.text_input(
                "Ask a question about this PDF",
                placeholder ="Example: What are the key findings?"
            )

        with right_col:

            st.subheader("🤖 AI Workspace")

            analysis_placeholder = st.empty()

            if st.button("Generate PDF Analysis"):
                with st.spinner("Analyzing PDF..."):
                    start_time = time.perf_counter()

                    question = (
                        pdf_question
                        if pdf_question 
                        else "Summarize the key points in this PDF."
                    )

                    pdf_brief = analyze_pdf(pdf_text, question)

                    processing_time = time.perf_counter() - start_time

                st.success("✅ Analysis Complete")

                sumcol1, sumcol2, sumcol3, sumcol4, sumcol5 = st.columns(5)

                with sumcol1:
                    st.metric("File Type", "PDF")

                with sumcol2:
                    st.metric("Characters", len(pdf_text))

                with sumcol3:
                    st.metric("AI Model", MODEL)

                with sumcol4:
                    st.metric("Time", f"{processing_time:.1f}s")

                with sumcol5:
                    st.metric("Status", "Complete")    

                with analysis_placeholder.container():    
                    
                    with st.container(border= True):
                        st.markdown(format_report(pdf_brief))

                st.download_button(
                    label = "Download PDF Analysis",
                    data = pdf_brief,
                    file_name = "analystai_pdf_analysis.txt",
                    mime = "text/plain"
                )

else:
    st.info("Upload csv or pdf file to begin analysis.")

    st.markdown("""
    ### What AnalystAI can do:
    - Analyze CSV datasets
    - Summarize PDF documents
    - Answer natural language questions
    - Generate analyst-style reports
    - Download results as text files
    - Run locally using Ollama
    """)

# ----------------
# Footer
# ----------------

st.divider()
st.caption(
    "⬢ Moros AnalystAI v3.0  •  Powered by Python, Streamlit, Pandas, and Ollama  •  Local AI Processing"
)


