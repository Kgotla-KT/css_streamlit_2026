import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import io
import tempfile

# Ensure fpdf2 is used
try:
    from fpdf import FPDF
except ImportError:
    st.error("Please run 'pip install fpdf2' in your terminal.")

# --- PAGE CONFIG ---
st.set_page_config(page_title="Dr. Kgotla Katlego Masibi - Profile", layout="wide")

# --- DATA PREPARATION (Restoring Publications) ---
publications = pd.DataFrame([
    {"Year": "2025", "Title": "Nanomaterials in water pollution control", "Journal": "Next Sustainability", "DOI": "https://doi.org/10.1016/j.nxsust.2025.100210"},
    {"Year": "2021", "Title": "Detection of Endosulfan", "Journal": "Materials", "DOI": "https://doi.org/10.3390/ma14040723"},
    {"Year": "2020", "Title": "Electrochemical Determination of Caffeine", "Journal": "Electroanalysis", "DOI": "https://doi.org/10.1002/elan.202060198"},
    {"Year": "2018", "Title": "Electrocatalysis of Lindane", "Journal": "Frontiers in Chemistry", "DOI": "https://doi.org/10.3389/fchem.2018.00423"}
])

# --- PDF GENERATION FUNCTION (Restoring Logic) ---
def create_pdf(scan_rate, rev, epa, epc, dep, n_val, fig):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", 'B', 16)
    pdf.cell(0, 10, "ELECTROCHEMICAL LAB REPORT & SUMMARY", new_x="LMARGIN", new_y="NEXT", align='C')
    pdf.ln(5)
    
    pdf.set_font("helvetica", 'B', 12)
    pdf.cell(0, 10, "1. Experimental Parameters & Observed Data", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("helvetica", '', 11)
    pdf.cell(0, 7, f"System: 5mM [Fe(CN)6] 4- in 0.1M KCl | Scan Rate (v): {scan_rate} mV/s", new_x="LMARGIN", new_y="NEXT")
    
    pdf.write(7, f"Epa: {epa} V | Epc: {epc} V | ")
    pdf.set_font("symbol", '', 11)
    pdf.write(7, "D") 
    pdf.set_font("helvetica", '', 11)
    pdf.write(7, f"Ep: {dep:.1f} mV | n: {n_val:.2f}")
    pdf.ln(10)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmpfile:
        fig.savefig(tmpfile.name, format='png', bbox_inches='tight')
        pdf.image(tmpfile.name, x=40, w=130)
    pdf.ln(5)

    pdf.set_font("helvetica", 'B', 12)
    pdf.cell(0, 10, "2. Influence of Scan Rate (v) - Detailed Analysis", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("helvetica", 'B', 11)
    pdf.cell(0, 7, "A. Influence on Peak Current (ip):", new_x="LMARGIN", new_y="NEXT")
    
    pdf.set_font("helvetica", 'I', 10)
    pdf.write(7, "Randles-Sevcik Equation: ip = (2.69 x 10^5) * n^(3/2) * A * D^(1/2) * C * ")
    pdf.set_font("symbol", '', 10)
    pdf.write(7, "O") 
    pdf.set_font("helvetica", 'I', 10)
    pdf.write(7, "v")
    pdf.ln(8)
    
    pdf.set_font("helvetica", '', 10)
    pdf.multi_cell(0, 6, "Scan rate (v) dictates the flux of ions. Higher rates create steeper concentration gradients, forcing faster diffusion and higher ip. (ip proportional to sqrt(v)).")
    
    pdf.ln(4)
    pdf.set_font("helvetica", 'B', 11)
    pdf.write(7, "B. Influence on Peak Separation (")
    pdf.set_font("symbol", '', 11)
    pdf.write(7, "D")
    pdf.set_font("helvetica", 'B', 11)
    pdf.write(7, "Ep):")
    pdf.ln(7)
    pdf.set_font("helvetica", '', 10)
    pdf.multi_cell(0, 6, "Probes kinetics. Slow scans (25 mV/s) allow equilibrium (~59 mV). Fast scans show 'lag', causing peaks to shift further apart as electron transfer can't keep up.")

    return pdf.output()

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to:", ["Researcher Profile", "Publications", "Electrochemistry Lab Explorer"])

# --- 1. RESEARCHER PROFILE (Restored) ---
if page == "Researcher Profile":
    st.title("🔬 Researcher Profile")
    col1, col2 = st.columns([1, 2])
    with col1:
        try:
            img_path = r"C:\Users\kkmasibi\Downloads\Day_4\Image.JPEG" 
            st.image(img_path, caption="Dr. Kgotla Katlego Masibi", width=300)
        except:
            st.image("https://via.placeholder.com/200", caption="Image Path Not Found")
        st.markdown("**Core Expertise:**")
        st.markdown("- :blue[Material Science]\n- :green[Nanotechnology]\n- :orange[Electrochemical Sensors]\n- :violet[Green Synthesis]")
    with col2:
        st.header("Dr. Kgotla Katlego Masibi")
        st.subheader("Postdoctoral Research Fellow | iThemba LABS")
        st.write("""
        SACNASP-Certified Natural Scientist specializing in the development of electrochemical sensors 
        and nanotechnology. My career spans forensic analysis at the South African Police Service 
        to high-impact academic research in sustainability and energy-storage materials.
        """)
        with st.expander("Academic Background"):
            st.write("🎓 **PhD in Science (Chemistry)** - North-West University")
            st.write("🎓 **MSc in Chemistry** - North-West University")
        with st.expander("Professional Milestones"):
            st.write("- **iThemba LABS (2024 - Present):** Postdoctoral Fellow")
            st.write("- **SAPS (2011 - 2024):** Forensic Analyst")
            st.write("- **Gaetsho High School (2009 - 2011):** Educator")

# --- 2. PUBLICATIONS (Restored) ---
elif page == "Publications":
    st.title("📚 Peer-Reviewed Research")
    search = st.text_input("Search publications by keyword (e.g., 'Caffeine'):")
    df_filtered = publications[publications.apply(lambda r: search.lower() in str(r).lower(), axis=1)] if search else publications
    
    st.dataframe(
        df_filtered, 
        column_config={"DOI": st.column_config.LinkColumn("Access Article")},
        hide_index=True,
        use_container_width=True
    )

# --- 3. SENSOR LAB EXPLORER (The Advanced Lab) ---
elif page == "Electrochemistry Lab Explorer":
    st.title("⚡ Cyclic Voltammetry Explorer")
    st.info("🔬 System: 5mM [Fe(CN)6]4- in 0.1M KCl")

    scan_rate = st.sidebar.select_slider("Scan Rate (mV/s)", options=[10, 25, 50, 100, 200], value=100)
    reversibility = st.sidebar.slider("Kinetic Lag (Reversibility)", 0.8, 2.5, 1.0)

    # Simulation Function
    def generate_cv(rate, rev):
        E = np.linspace(-0.2, 0.6, 500)
        E0, dE = 0.22, (0.059 / 1) * rev
        epa, epc = E0 + (dE/2), E0 - (dE/2)
        ip = 20 * np.sqrt(rate/100)
        curr = np.concatenate([ip * np.exp(-((E - epa)**2)/0.005) + 0.1*E, 
                               -ip * np.exp(-((np.flip(E) - epc)**2)/0.005) + 0.1*np.flip(E)])
        return np.concatenate([E, np.flip(E)]), curr, epa, epc

    volts, current, epa_true, epc_true = generate_cv(scan_rate, reversibility)
    
    fig, ax = plt.subplots(figsize=(6,4))
    ax.plot(volts[:500], current[:500], label="Anodic (Oxidation)", color="red")
    ax.plot(volts[500:], current[500:], label="Cathodic (Reduction)", color="blue")
    ax.set_xlabel("Potential (V)")
    ax.set_ylabel("Current (µA)")
    ax.set_title(f"CV at {scan_rate} mV/s")
    ax.legend()
    st.pyplot(fig)

    st.markdown("---")
    st.subheader("🧮 Data Analysis Quiz")
    
    col_a, col_b = st.columns(2)
    with col_a:
        u_epa = st.number_input("Enter Epa (V):", format="%.3f", step=0.001)
        u_epc = st.number_input("Enter Epc (V):", format="%.3f", step=0.001)
    
    if st.button("Check My Answer"):
        u_dep = abs(u_epa - u_epc) * 1000
        u_n = 59 / u_dep if u_dep > 0 else 0
        
        if 0.7 <= u_n <= 1.3:
            st.balloons()
            st.success(f"Correct! n ≈ 1. ΔEp = {u_dep:.1f} mV")
            
            pdf_bytes = create_pdf(scan_rate, reversibility, u_epa, u_epc, u_dep, u_n, fig)
            st.download_button(label="📥 Download Full PDF Report", data=bytes(pdf_bytes), file_name="CV_Lab_Report.pdf", mime="application/pdf")
        else:
            st.error(f"Calculated n is {u_n:.2f}. Check your readings.")

# Footer
st.sidebar.markdown("---")
st.sidebar.caption("App developed for Dr. K.K. Masibi Lab")