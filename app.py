import streamlit as st
import pandas as pd
import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt
import random

# Başlık
st.title("Trafik Tahmini ve Rota Optimizasyonu")
st.write("Bu uygulama, trafik ve rota verilerini analiz ederek optimizasyon sağlar.")

# Kullanıcıdan parametreler alma
st.sidebar.header("Parametreler")
weather_condition = st.sidebar.selectbox("Hava Durumu", ["Güneşli", "Yağmurlu", "Bulutlu"])
start_location = st.sidebar.text_input("Başlangıç Konumu (enlem, boylam)", "41.015137, 28.979530")
end_location = st.sidebar.text_input("Bitiş Konumu (enlem, boylam)", "41.008237, 28.978358")

if st.sidebar.button("Rota Bul ve Görselleştir"):
    st.write("Veriler işleniyor...")

    # Rota Bulma
    try:
        # Başlangıç ve bitiş koordinatlarını ayırma
        start_coords = tuple(map(float, start_location.split(',')))
        end_coords = tuple(map(float, end_location.split(',')))

        # OSMnx ile yol ağı oluşturma
        G = ox.graph_from_point(start_coords, dist=2000, network_type='drive')

        # En yakın düğümleri bulma
        orig_node = ox.distance.nearest_nodes(G, start_coords[1], start_coords[0])
        dest_node = ox.distance.nearest_nodes(G, end_coords[1], end_coords[0])

        # Rota bulma
        route = nx.shortest_path(G, orig_node, dest_node, weight='length')

        # Rota görselleştirme
        fig, ax = ox.plot_graph_route(G, route, route_linewidth=3, node_size=0, route_color='purple', show=False, close=False)
        st.pyplot(fig)
        st.success("Rota başarıyla görselleştirildi!")

        # Örnek tahminleme modelleri sonuçları
        st.write("### En İyi 5 Tahminleme Modeli")
        # Örnek verilerle DataFrame oluşturuluyor
        model_results = pd.DataFrame({
            "Model": ["Model A", "Model B", "Model C", "Model D", "Model E"],
            "Doğruluk (%)": [random.uniform(85, 95) for _ in range(5)],  # Örnek doğruluk değerleri
            "Tahmin Süresi (sn)": [random.uniform(0.5, 2) for _ in range(5)]  # Örnek süreler
        })
        model_results = model_results.sort_values(by="Doğruluk (%)", ascending=False)
        
        # Tabloyu ekrana yazdırma
        st.table(model_results)

    except Exception as e:
        st.error(f"Bir hata oluştu: {e}")

# Kullanıcı bilgilendirme
st.write("Lütfen başlangıç ve bitiş konumlarını girerek rotayı görselleştirebilir ve en iyi modelleri inceleyebilirsiniz.")
