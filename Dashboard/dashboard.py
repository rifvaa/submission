from st_on_hover_tabs import on_hover_tabs
import pandas as pd
import streamlit as st
import plotly.graph_objs as go
from babel.numbers import format_currency
st.set_page_config(layout="wide")

st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)


with st.sidebar:
    tabs = on_hover_tabs(tabName=['Profile', 'Projects', 'Other'], 
                         iconName=['📃', '💻', '❕'], default_choice=0)

if tabs =='Profile':
    st.subheader("Name : Muhammad Rifva Maulana \n\n ✉\t gmail : maulanarifva@gmailcom\n\n")
    
elif tabs == 'Projects':
    st.header("Proyek Analisis Data: Bike-sharing-dataset")
    st.subheader("\n\nVisualization & Explanatory Analysis")
    st.write("Pertanyaan 1: Bagaimana perkembangan penyewaan sepeda selama 1 tahun ?\n\n Pertanyaan 2: Apa penyebab minat penyewa sepeda naik & turun ?")
    
    def plot_histogram():
        bulan = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        sum_val = [134933, 151352, 228920, 269094, 331686, 346342, 344948, 351194, 345991, 322352, 254831, 211036]

        bar_plot = go.Bar(
            x=bulan,
            y=sum_val,
            marker=dict(color='skyblue', opacity=0.7),
            text=sum_val,
            textposition='auto'
        )

        line_plot = go.Scatter(
            x=bulan,
            y=sum_val,
            mode='lines+markers',
            line=dict(color='gray', dash='dash'),
            marker=dict(symbol='circle-open', size=8)
        )

        data = [bar_plot, line_plot]

    
        layout = go.Layout(
            title='Histogram Jumlah Penyewa per Bulan',
            xaxis=dict(title='Bulan'),
            yaxis=dict(title='Jumlah Penyewa'),
            showlegend=False,
            xaxis_tickangle=-45,
            margin=dict(l=50, r=50, t=50, b=50),
            plot_bgcolor='rgba(0,0,0,0)'
        )

       
        fig = go.Figure(data=data, layout=layout)

       
        st.plotly_chart(fig)

    def plot_factors():
        
        musim = ['Fall', 'Spring', 'Summer', 'Winter']
        mean_ttl_penyewa_musim = [5644.30, 4035.86, 4330.17, 4527.10]

        cuaca = ['Berkabut/Berawan', 'Cerah/Sebagian Berawan', 'Salju Ringan/Hujan']
        mean_ttl_penyewa_cuaca = [4035.86, 5644.30, 1803.29]

        hari_kerja = ['Workingday', 'Holiday']
        mean_ttl_penyewa_hari = [4330.17, 4527.10]

        hari = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
        mean_ttl_penyewa_hari_weekday = [4338.12, 4510.66, 4548.54, 4667.26, 4690.29, 4550.54, 4228.83]

        
        fig = go.Figure()

        fig.add_trace(go.Bar(x=[x - 0.3 for x in range(len(musim))], y=mean_ttl_penyewa_musim, name='Musim', marker_color='blue'))
        fig.add_trace(go.Bar(x=[x - 0.1 for x in range(len(cuaca))], y=mean_ttl_penyewa_cuaca, name='Cuaca', marker_color='red'))
        fig.add_trace(go.Bar(x=[x + 0.1 for x in range(len(hari_kerja))], y=mean_ttl_penyewa_hari, name='Hari Kerja', marker_color='green'))
        fig.add_trace(go.Bar(x=[x + 0.3 for x in range(len(hari))], y=mean_ttl_penyewa_hari_weekday, name='Hari dalam Seminggu', marker_color='purple'))

        fig.update_layout(
            title='Penggunaan Sepeda Berdasarkan Faktor-faktor',
            xaxis=dict(
                title='Variabel Kategorikal',
                tickvals=list(range(len(musim) + len(cuaca) + len(hari_kerja) + len(hari))),
                ticktext=musim + cuaca + hari_kerja + hari,
                tickangle=45,
                tickmode='array',
                tickfont=dict(size=10)
            ),
            yaxis=dict(
                title='Jumlah Penggunaan Sepeda'
            ),
            barmode='group',
            legend=dict(
                title='Faktor',
                orientation='h',
                yanchor='bottom',
                y=1.02,
                xanchor='right',
                x=1
            )
        )

        st.plotly_chart(fig)

    def main():
        st.subheader("Diagram")

        option = st.selectbox("Visualisasi Data:", ["Pertanyaan 1", "Pertanyaan 2"])

        if option == "Pertanyaan 1":
            plot_histogram()
        elif option == "Pertanyaan 2":
            plot_factors()

    if __name__ == "__main__":
        main()

        
    
elif tabs == 'Other':
    st.title("NOTHING")
    st.write("HEHE...")
    
