import streamlit as st

# ضبط إعدادات الصفحة
st.set_page_config(
    page_title="Libyan Grid - SMR Calculator",
    page_icon="⚡",
    layout="centered"
)

# العنوان الرئيسي والترويسة الأكاديمية
st.title("⚡ Libyan Energy Grid: SMR Feasibility & Carbon Offset Calculator")
st.markdown("""
**An Academic Assessment Tool for Clean Energy Transition & Grid Modernization in Libya**  
*Developed & Designed by Lena Elsaieti*  
---
""")

# الشريط الجانبي للمدخلات
st.sidebar.header("📊 Grid & Regional Parameters")
city_demand = st.sidebar.number_input("Target Regional Peak Demand (MWe)", min_value=100, max_value=5000, value=1200, step=100)
smr_target_pct = st.sidebar.slider("SMR Target Integration (% of Grid)", 10, 100, 30) / 100.0
smr_unit_capacity = st.sidebar.selectbox("SMR Unit Capacity Model (MWe)", [50, 77, 100, 300], index=2)

# الحسابات الهندسية والفيزياء
required_smr_capacity = city_demand * smr_target_pct
num_smrs = max(1, round(required_smr_capacity / smr_unit_capacity))
actual_installed_capacity = num_smrs * smr_unit_capacity

# حساب الإنتاج السنوي بالـ GWh (مع معامل سعة 90%)
annual_energy_gwh = (actual_installed_capacity * 8760 * 0.90) / 1000.0

# حساب الوفر الكربوني مقارنة بالغاز الطبيعي والديزل
co2_saved_tons = annual_energy_gwh * 1000 * 0.45 

# عرض النتائج في بطاقات رقمية
st.subheader("💡 Feasibility & SMR Deployment Metrics")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Required SMR Units", value=f"{num_smrs} Units")
with col2:
    st.metric(label="Total SMR Capacity", value=f"{actual_installed_capacity} MWe")
with col3:
    st.metric(label="Annual Energy Output", value=f"{annual_energy_gwh:,.0f} GWh")

st.markdown("---")

# عرض التأثير البيئي والمكاني
st.subheader("🌱 Environmental & Spatial Impact Analysis")
st.success(f"🍃 **CO2 Reduction:** Offsets approximately **{co2_saved_tons:,.0f} Metric Tons** of CO₂ emissions annually compared to conventional fossil fuel generation.")
st.info(f"📍 **Land Savings:** Requires ~**{(actual_installed_capacity * 0.05):,.1f} km²** of land, saving vast spatial footprints compared to equivalent output solar farms (~**{(actual_installed_capacity * 2.5):,.1f} km²**).")

st.markdown("""
---
*Technical Note: Calculations based on standard IAEA Small Modular Reactor (SMR) technical profiles and North African baseline grid emission factors.*
""")
