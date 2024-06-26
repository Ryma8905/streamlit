import streamlit as st


def contexte():
    """st.set_page_config(
        page_title="London Fire Brigade Project",
        page_icon="🎆",
    )"""

    st.image("Images/LFB_image.png", caption='Fire Brigade in action', use_column_width=True) 
    st.title("London Fire Brigade Project")

    st.write("""
    Dans le cadre de ce projet, notre objectif principal est d'analyser et d'estimer les temps de réponse et de mobilisation de la 
             Brigade des Pompiers de Londres. En tant que service d'incendie et de sauvetage le plus actif du Royaume-Uni, 
             la Brigade des Pompiers de Londres joue un rôle crucial dans la sécurité et la protection des citoyens de la ville. 
             Forte de son expertise et de son expérience, elle est également reconnue comme l'une des plus grandes organisations 
             de lutte contre l'incendie et de sauvetage au niveau mondial.
""")


    st.write(""" 
            À travers cette étude, nous cherchons à mieux comprendre les dynamiques opérationnelles de la Brigade des Pompiers de 
             Londres afin d'optimiser ses interventions et de renforcer sa capacité à répondre efficacement aux situations d'urgence. 
""")
    

           
    st.markdown(
        """
        ### Sources des données : London Datastore
        - Survenance des [Incidents](https://data.london.gov.uk/dataset/london-fire-brigade-incident-records)
        - Enregistrement des [Mobilisations](https://data.london.gov.uk/dataset/london-fire-brigade-mobilisation-records)
        
    """
    )
contexte()


