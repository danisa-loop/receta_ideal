import streamlit as st
import pandas as pd 
import numpy as np

st.title("¿Qué comemos?")

t = st.markdown("Ingresá los ingredientes que tengas a mano, si sos cociner@ estrella o estrellad@, y nosotr@s te damos la receta* ideal para vos!! :sunglasses:")
t2 = st.caption("*Recetas extraídas de https://cocinerosargentinos.com/, con etiquetas de dificultad predichas por un modelo de machine learning entrenado por nuestro equipo de trabajo.")

#ingredientes con los que entrenamos el modelo
INGREDIENTES = ["naranja","verdeo","crema","azucar impalpable","batata","manzana","bondiola","durazno","berenjena","pechuga","oliva","harina", "leche", "azucar", "queso", "tomate", "huevo", "crema", "nuez", "arroz", "chocolate", "carne", "pollo","jengibre", "miel", "levadura", "papa", "almendra", "jamon", "calabaza", "atun", "aceitunas", "arveja", "garbanzos", "espinaca", "acelga", "quinoa", "frutilla", "avellana", "apio", "puerro", "limon", "chorizo", "avena", "salmon", "mani", "brocoli", "cerveza", "mozzarella", "ricota", "esparragos", "quinoa", "azafran", "panceta", "tofu"] 

#mismos ingredientes, pero con mayúsculas y tildes para la lista desplegable
ingred_choice = ('Aceitunas', 'Acelga', 'Almendra', 'Apio', 'Arroz', 'Arveja', 'Atún', 'Avellana', 'Avena', 'Azafrán', 'Azúcar', 'Azúcar impalpable', 'Batata', 'Berenjena', 'Bondiola', 'Brócoli', 'Calabaza', 'Carne', 'Cerveza', 'Chocolate', 'Chorizo', 'Crema', 'Durazno', 'Espinaca', 'Espárragos', 'Fideo', 'Frutilla', 'Garbanzos', 'Harina', 'Huevo', 'Jamón', 'Jengibre', 'Leche', 'Levadura', 'Limón', 'Manzana', 'Maní', 'Miel', 'Mozzarella', 'Naranja', 'Nuez', 'Oliva', 'Panceta', 'Papa', 'Pechuga', 'Pollo', 'Puerro', 'Queso', 'Quinoa', 'Ricota', 'Salmón', 'Tofu', 'Tomate', 'Verdeo')

#selección de ingredientes
option1 = st.selectbox("Ingrediente 1", ingred_choice)
option2 = st.selectbox("Ingrediente 2", ingred_choice)
option3 = st.selectbox("Ingrediente 3", ingred_choice)

#selección de dificultad
grade_map = {
    0: '"Con suerte te hago un huevo frito."',
    1: '"Tengo más estrellas Michelin que Martitegui."',
}

grade = st.slider('Dificultad', 0, 1, 1)
st.write("Dificultad elegida: ", grade_map[grade])

#reconvertidos datos seleccionados a palabras existentes en la lista de INGREDIENTES con la que buscamos en el df de ca
op1_l = option1.lower()
op2_l = option2.lower()
op3_l = option3.lower()

st.caption("Buscando...")
st.empty()

def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b)
    return s

nor1 = normalize(op1_l)
nor2 = normalize(op2_l)
nor3 = normalize(op3_l)

#levantamos el df de ca
df_cad = pd.read_csv('recetas_cocineros_argentinos_dif.csv',sep='|')

#armamos la máscara de los ingredientes seleccionados para que devuelva una receta

rango = df_cad.index
diccionario = {}
for indice in rango:
    dict_ing = {}
    dict_ing.clear()
    for ingrediente in INGREDIENTES:
        try:
            find = df_cad['Ingredientes'].iloc[indice].find(ingrediente)
        except:
            find = -1
        if find != -1:
            dict_ing[ingrediente] = 1
        else:
            dict_ing[ingrediente] = 0
        diccionario[indice] = dict_ing.copy()

ingredientes = pd.DataFrame(diccionario)
df = ingredientes.transpose()
def searchByIngredient(df,lista):
    acu = np.ones(len(df),dtype=bool)
    for ingredient in lista:
        acu = (acu) & (df[ingredient] == 1)
    return acu

data = pd.concat([df_cad,df],axis=1)

lista_ingredientes = [nor1,nor2,nor3]
busqueda = searchByIngredient(data,lista_ingredientes)

#imprimimos las recetas que salieron: nombre, ingredientes e instrucciones
st.markdown("**Receta(s) encontrada(s): **")

st.table(data[busqueda].iloc[:,2:5]) 

#wordcloud para darle diseño
st.image('./png1.png')