import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import json

from app.frontend.components.dashboard import render_dashboard
from app.frontend.components.clients import render_clients
from app.frontend.components.vehicles import render_vehicles  
from app.frontend.components.quotes import render_quotes
from app.frontend.components.alerts import render_alerts
from app.frontend.utils.auth import check_authentication
from app.frontend.utils.helpers import format_currency, get_status_color

# Configuration de la page
st.set_page_config(
    page_title="GestionPro",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #1e3a8a 0%, #3b82f6 100%);
        padding: 1rem;
        border-radius: 0.5rem;
        color: white;
        margin-bottom: 2rem;
    }
    
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 0.5rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        border-left: 4px solid #3b82f6;
    }
    
    .status-badge {
        padding: 0.25rem 0.75rem;
        border-radius: 1rem;
        font-size: 0.75rem;
        font-weight: 600;
    }
    
    .status-actif { background-color: #dcfce7; color: #166534; }
    .status-prospect { background-color: #fef3cd; color: #92400e; }
    .status-inactif { background-color: #f3f4f6; color: #374151; }
    
    .sidebar .sidebar-content {
        background: #f8fafc;
    }
</style>
""", unsafe_allow_html=True)

# Configuration de l'API
API_BASE_URL = "http://localhost:8000/api/v1"

class APIClient:
    """Client pour communiquer avec l'API FastAPI."""
    
    def __init__(self, base_url: str):
        self.base_url = base_url
        
    def get(self, endpoint: str):
        """Effectue une requête GET."""
        try:
            response = requests.get(f"{self.base_url}{endpoint}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            st.error(f"Erreur lors de la requête: {e}")
            return None
            
    def post(self, endpoint: str, data: dict):
        """Effectue une requête POST."""
        try:
            response = requests.post(f"{self.base_url}{endpoint}", json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            st.error(f"Erreur lors de la requête: {e}")
            return None

# Instance du client API
api_client = APIClient(API_BASE_URL)

def main():
    """Fonction principale de l'application."""
    
    # Vérification de l'authentification (pour plus tard)
    # if not check_authentication():
    #     return
    
    # En-tête principal
    st.markdown("""
    <div class="main-header">
        <h1>🏗️ GestionPro</h1>
        <p>Plateforme de gestion professionnelle pour équipements et clients</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar pour la navigation
    with st.sidebar:
        st.title("Navigation")
        
        # Menu principal
        page = st.selectbox(
            "Choisir une section",
            [
                "📊 Tableau de bord",
                "👥 Clients", 
                "🚛 Équipements",
                "📋 Devis",
                "🔔 Alertes"
            ]
        )
        
        st.divider()
        
        # Informations système
        st.subheader("Système")
        st.info(f"Dernière mise à jour: {datetime.now().strftime('%H:%M')}")
        
        # Alertes rapides
        st.subheader("Alertes")
        
        # Simulation d'alertes (à remplacer par des données réelles)
        alert_count = 3
        if alert_count > 0:
            st.warning(f"⚠️ {alert_count} alertes actives")
            if st.button("Voir les alertes", use_container_width=True):
                st.session_state.page = "🔔 Alertes"
                st.rerun()
        else:
            st.success("✅ Aucune alerte")
    
    # Rendu des pages selon la sélection
    if page == "📊 Tableau de bord":
        render_dashboard(api_client)
    elif page == "👥 Clients":
        render_clients(api_client)
    elif page == "🚛 Équipements":
        render_vehicles(api_client)
    elif page == "📋 Devis":
        render_quotes(api_client)
    elif page == "🔔 Alertes":
        render_alerts(api_client)
    
    # Footer
    st.divider()
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.caption("📧 support@gestionpro.fr")
    with col2:
        st.caption("📞 +33 1 23 45 67 89")
    with col3:
        st.caption("🕒 Lun-Ven 8h-18h")


if __name__ == "__main__":
    main()