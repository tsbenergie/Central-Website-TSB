import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime, timedelta


def render_dashboard(api_client):
    """Affiche le tableau de bord principal."""
    
    st.title("📊 Tableau de bord")
    st.markdown("Vue d'ensemble des activités de l'entreprise")
    
    # Données simulées (à remplacer par des appels API)
    mock_data = {
        'stats': {
            'total_clients': 127,
            'clients_actifs': 98,
            'clients_inactifs': 29,
            'total_vehicules': 45,
            'vehicules_operationnels': 38,
            'vehicules_en_maintenance': 5,
            'vehicules_en_panne': 2,
            'ca_prevu': 2450000,
            'ca_realise': 1890000,
            'taux_conversion': 68.5
        }
    }
    
    # KPIs principaux
    st.subheader("📈 Indicateurs clés")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="👥 Clients actifs",
            value=mock_data['stats']['clients_actifs'],
            delta=f"+5.2% vs mois dernier",
            help=f"Sur {mock_data['stats']['total_clients']} clients total"
        )
    
    with col2:
        availability_rate = (mock_data['stats']['vehicules_operationnels'] / 
                           mock_data['stats']['total_vehicules'] * 100)
        st.metric(
            label="🚛 Équipements opérationnels", 
            value=f"{mock_data['stats']['vehicules_operationnels']}/{mock_data['stats']['total_vehicules']}",
            delta=f"Disponibilité: {availability_rate:.1f}%"
        )
    
    with col3:
        st.metric(
            label="💰 CA prévisionnel",
            value=f"{mock_data['stats']['ca_prevu']:,.0f} €",
            delta=f"Réalisé: {mock_data['stats']['ca_realise']:,.0f} €"
        )
    
    with col4:
        st.metric(
            label="📊 Taux de conversion",
            value=f"{mock_data['stats']['taux_conversion']:.1f}%",
            delta="+2.1% vs mois dernier",
            help="Pourcentage de devis acceptés"
        )
    
    st.divider()
    
    # Graphiques et analyses
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Évolution du chiffre d'affaires")
        
        # Données simulées pour le graphique CA
        dates = pd.date_range(start='2025-01-01', end='2025-06-30', freq='M')
        ca_data = {
            'Date': dates,
            'CA Réalisé': [280000, 320000, 410000, 380000, 450000, 315000],
            'CA Objectif': [300000, 350000, 400000, 400000, 450000, 350000]
        }
        
        df_ca = pd.DataFrame(ca_data)
        
        fig_ca = go.Figure()
        fig_ca.add_trace(