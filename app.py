import streamlit as st
import math

st.title("Alopecia Areata Risk Hesaplayıcı")

# Kullanıcıdan veri al
calreticulin = st.number_input("Calreticulin düzeyi (ng/mL)", min_value=0.0, value=3000.0)
aso10 = st.number_input("ASO-10 skoru (0-40)", min_value=0.0, max_value=40.0, value=20.0)
ai_hastalik_yok = st.selectbox("AI hastalık YOK?", ["Var", "Yok"]) == "Yok"
cinsiyet_kadin = st.selectbox("Cinsiyet", ["Erkek", "Kadın"]) == "Kadın"
antitpo_yuksek = st.selectbox("Anti-TPO yüksek?", ["Hayır", "Evet"]) == "Evet"

# Hesapla butonu
if st.button("Riski Hesapla"):
    # Model katsayıları
    intercept = 0.0302
    b_calreticulin = 0.0003
    b_aso10 = 0.0919
    b_ai = -2.3483
    b_cinsiyet = -1.0413
    b_antitpo = 0.8444

    # Lojit hesapla
    logit = (
        intercept
        + b_calreticulin * calreticulin
        + b_aso10 * aso10
        + b_ai * (1 if ai_hastalik_yok else 0)
        + b_cinsiyet * (1 if cinsiyet_kadin else 0)
        + b_antitpo * (1 if antitpo_yuksek else 0)
    )

    # Sigmoid
    probability = 1 / (1 + math.exp(-logit))
    st.success(f"Alopecia Areata riski: %{probability * 100:.1f}")
