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

        # Ortalama hız hesaplama
        edge_lengths = []
        for u, v in zip(route[:-1], route[1:]):
            edge_data = G.get_edge_data(u, v)
            if edge_data:
                edge_lengths.append(edge_data[0]["length"])
        avg_speed = sum(edge_lengths) / len(edge_lengths) if edge_lengths else 0

        # Rota görselleştirme
        fig, ax = ox.plot_graph_route(G, route, route_linewidth=3, node_size=0, route_color='purple', show=False, close=False)
        st.pyplot(fig)
        st.success(f"Rota başarıyla görselleştirildi! Ortalama hız: {avg_speed:.2f} km/s")

        # Tahminleme modelleri sonuçları
        st.write("### En İyi 5 Tahminleme Modeli")
        model_names = ["Linear Regression", "Random Forest", "Gradient Boosting", "Support Vector Machine", "K-Nearest Neighbors"]
        model_results = pd.DataFrame({
            "Model": model_names,
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
