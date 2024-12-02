import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
# import pandas as pd

st.title("Manipuler des graphiques")


# Import des datasets

flights  = sns.load_dataset('flights')
tips = sns.load_dataset('tips')
diamonds  = sns.load_dataset('diamonds')

datasets = ("flights", "tips", "diamonds")


# Sélection du dataset

data_selected = st.selectbox(
    "Quel DataSet veux-tu utiliser ?",
    datasets,
    index=None,
    placeholder="Select"
)

# On affiche le dataset sélectionné

data = flights # Je mets flights par défaut

if data_selected == "flights":
    st.write(flights)
    data = flights
elif data_selected == "tips":
    st.write(tips)
    data = tips
elif data_selected == "diamonds":
    st.write(diamonds)
    data = diamonds



# Sélection de la colonne X

# Je crée une liste pour récupérer tous les en-têtes
# pour ensuite la transformer en tuple
lst_entete = []

for i in data:
    lst_entete.append(i)

tpl_entete = tuple(lst_entete)

# Si mon dataset est sélectionné, 
# j'affiche le select de ma colonne_x

if data_selected:
    colonne_x = st.selectbox(
        "Choisissez la colonne X",
        tpl_entete, # Je récupère mon tuple
        index=None,
        placeholder="Select"
    )

    # Sélection de la colonne Y
    # Si ma colonne_x est sélectionnée

    if colonne_x:

        colonne_y = st.selectbox(
            "Choisissez la colonne Y",
            tpl_entete,
            index=None,
            placeholder="Select"
        )

        # Si colonne_x et _y ont été choisie
        # Je sélectionne un graph

        if colonne_y:

            graphsets = ("bar_chart", "line_chart", "scatter_chart")

            graph_selected = st.selectbox(
                "Quel graphique veux-tu utiliser ?",
                graphsets,
                index=None,
                placeholder="Select"
            )
            
            # graph_selected = bar_chart # Par défaut
                
            fig, ax = plt.subplots()    
            if graph_selected == "bar_chart":
                sns.barplot(x=colonne_x, y=colonne_y, data=data, ax=ax)
                st.pyplot(fig)
                ax.set_title("Bar Chart")
            elif graph_selected == "line_chart":
                sns.lineplot(x=colonne_x, y=colonne_y, data=data, ax=ax)
                st.pyplot(fig)
                ax.set_title("Line Chart")
            elif graph_selected == "scatter_chart":
                sns.scatterplot(x=colonne_x, y=colonne_y, data=data, ax=ax)
                st.pyplot(fig)
                ax.set_title("Scatter Chart")

            
            # J'affiche mon Checkbox

            if graph_selected:

                display_matrice = st.checkbox("Afficher la matrice de corrélation")

                if display_matrice:

                    numeric_data = data.select_dtypes(include=['number'])

                    if not numeric_data.empty: 
                        fig, ax = plt.subplots()
                        sns.heatmap(numeric_data.corr(), ax=ax)
                        ax.set_title("Matrice de corrélation")
                        st.pyplot(fig)
                    
