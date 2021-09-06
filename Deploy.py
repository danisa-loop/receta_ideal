import streamlit as st
import pandas as pd 


st.title("¿Qué comemos?")

t = st.markdown("Ingresá los ingredientes que tengas a mano, si sos cociner@ estrella o estrellad@,              y nosotr@s te damos la receta ideal para vos!!")

option1 = st.selectbox("Ingrediente 1", ('Aceitunas', 'Acelga', 'Almendra', 'Apio', 'Arroz', 'Arveja', 'Atún', 'Avellana', 'Avena', 'Azafrán', 'Azúcar', 'Azúcar impalpable', 'Batata', 'Berenjena', 'Bondiola', 'Brócoli', 'Calabaza', 'Carne', 'Cerveza', 'Chocolate', 'Chorizo', 'Crema', 'Durazno', 'Espinaca', 'Espárragos', 'Fideo', 'Frutilla', 'Garbanzos', 'Harina', 'Huevo', 'Jamón', 'Jengibre', 'Leche', 'Levadura', 'Limón', 'Manzana', 'Maní', 'Miel', 'Mozzarella', 'Naranja', 'Nuez', 'Oliva', 'Panceta', 'Papa', 'Pechuga', 'Pollo', 'Puerro', 'Queso', 'Quinoa', 'Ricota', 'Salmón', 'Tofu', 'Tomate', 'Verdeo'))

option2 = st.selectbox("Ingrediente 2", ('Aceitunas', 'Acelga', 'Almendra', 'Apio', 'Arroz', 'Arveja', 'Atún', 'Avellana', 'Avena', 'Azafrán', 'Azúcar', 'Azúcar impalpable', 'Batata', 'Berenjena', 'Bondiola', 'Brócoli', 'Calabaza', 'Carne', 'Cerveza', 'Chocolate', 'Chorizo', 'Crema', 'Durazno', 'Espinaca', 'Espárragos', 'Fideo', 'Frutilla', 'Garbanzos', 'Harina', 'Huevo', 'Jamón', 'Jengibre', 'Leche', 'Levadura', 'Limón', 'Manzana', 'Maní', 'Miel', 'Mozzarella', 'Naranja', 'Nuez', 'Oliva', 'Panceta', 'Papa', 'Pechuga', 'Pollo', 'Puerro', 'Queso', 'Quinoa', 'Ricota', 'Salmón', 'Tofu', 'Tomate', 'Verdeo'))

option3 = st.selectbox("Ingrediente 3", ('Aceitunas', 'Acelga', 'Almendra', 'Apio', 'Arroz', 'Arveja', 'Atún', 'Avellana', 'Avena', 'Azafrán', 'Azúcar', 'Azúcar impalpable', 'Batata', 'Berenjena', 'Bondiola', 'Brócoli', 'Calabaza', 'Carne', 'Cerveza', 'Chocolate', 'Chorizo', 'Crema', 'Durazno', 'Espinaca', 'Espárragos', 'Fideo', 'Frutilla', 'Garbanzos', 'Harina', 'Huevo', 'Jamón', 'Jengibre', 'Leche', 'Levadura', 'Limón', 'Manzana', 'Maní', 'Miel', 'Mozzarella', 'Naranja', 'Nuez', 'Oliva', 'Panceta', 'Papa', 'Pechuga', 'Pollo', 'Puerro', 'Queso', 'Quinoa', 'Ricota', 'Salmón', 'Tofu', 'Tomate', 'Verdeo'))

grade_map = {
    0: '"Con suerte te hago un huevo frito"',
    1: '"Tengo más estrellas Michelin que Martitegui"',
}

grade = st.slider('Dificultad', 0, 1, 1)
st.write("Dificultad elegida: ", grade_map[grade])

