import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
st.title('🍰Parabola graph🧋')
st.badge(" Hi we are Four Seasons")
# 1. Sidebar และ Widgets 3 ชนิด (selectbox, slider, number_input)
parabola_type = st.sidebar.selectbox("รูปแบบ", ["แนวตั้ง: y = a(x-h)² + k", "แนวนอน: x = a(y-k)² + h"])
a = st.sidebar.slider("ค่า a (ความกว้าง/ทิศทาง)", -3.0, 3.0, 1.0, 0.5)
if a == 0: a = 0.01

h = st.sidebar.number_input("ค่า h", value=0.0)
k = st.sidebar.number_input("ค่า k", value=0.0)

tab1, tab2 = st.tabs(["📊 กราฟ & วิเคราะห์", "📚 สูตร"])

with tab1:
    col1, col2 = st.columns([2, 1])
    
    fig, ax = plt.subplots(facecolor="#00CED1")
    ax.set_facecolor("#ADD8E6")
    
    if "แนวตั้ง" in parabola_type:
        x = np.linspace(h - 5, h + 5, 200)
        y = a * (x - h)**2 + k
        ax.plot(x, y, color="#B5838D", lw=2.5, label="Parabola")
        direction = "หงาย (เปิดบน)" if a > 0 else "คว่ำ (เปิดล่าง)"
    else:
        y = np.linspace(k - 5, k + 5, 200)
        x = a * (y - k)**2 + h
        ax.plot(x, y, color="#83A5B5", lw=2.5, label="Parabola")
        direction = "เปิดขวา" if a > 0 else "เปิดซ้าย"
        
    ax.plot(h, k, 'o', color="#E56B6F", label=f"Vertex ({h}, {k})")
    ax.grid(True, linestyle=":", alpha=0.5)
    ax.legend()
    
    with col1:
        st.pyplot(fig)
        
    with col2:
        st.subheader("พฤติกรรมกราฟ")
        st.metric("จุดยอด (h, k)", f"({h}, {k})")
        st.metric("ทิศทางการเปิด", direction)

with tab2:
    st.subheader("📚 สมการพาราโบลา")

    st.markdown("### 🔵 พาราโบลาแนวตั้ง")
    st.latex(r"y = a(x-h)^2 + k")

    st.write("โดย")
    st.write("- a = ค่าความกว้างและทิศทางการเปิด")
    st.write("- h = พิกัด x ของจุดยอด")
    st.write("- k = พิกัด y ของจุดยอด")
    st.write("- จุดยอด คือ (h, k)")

    st.markdown("### 🟢 พาราโบลาแนวนอน")
    st.latex(r"x = a(y-k)^2 + h")

    st.write("โดย")
    st.write("- a > 0 → เปิดไปทางขวา")
    st.write("- a < 0 → เปิดไปทางซ้าย")
    st.write("- จุดยอด คือ (h, k)")
