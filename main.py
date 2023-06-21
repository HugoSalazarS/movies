from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import pandas as pd
from data import df
import re
from unidecode import unidecode
import uvicorn
from IPython.display import display
from pandas import DataFrame


# Instance api
app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def welcome_page():
    title = "Welcome to Movies Recommendation Project"

    footer = """
    <footer>
        <p><h1>Created by Hugo Salazar</h1></p>
        <p><a href="https://www.linkedin.com/in/hasalazars/">LinkedIn</a></p>
        <p><a href="https://github.com/HugoSalazarS">GitHub</a></p>
    </footer>
    """

    body = """
    <h2>About the Project</h2>
    <p>The Movies Recommendation Project is designed to provide movie recommendations based on various criteria. It offers the following functions:</p>
    <ol>
        <li>This function calculates the number of films released in a specific month. The month input should be provided in Spanish language. <a href="/cantidad_filmaciones_mes/enero" target="_blank">Click here</a> to try this function.</li>
        <li>This function calculates the number of films released in a specific day of the week. The day of the week should be provided in Spanish language. <a href="/total_films_day/lunes" target="_blank">Click here</a> to try this function.</li>
        <li>This function returns the title, the year released, and the score of the movie. If there is more than one movie with the same title, it returns all of them. <a href="/score_title/cinderella" target="_blank">Click here</a> to try this function.</li>
        <li>This function returns the title, the total number of votes, and the average vote value. <a href="/votos_titulo/Toy Story" target="_blank">Click here</a> to try this function.</li>
        <li>This function retrieves information about an actor, including the number of films they have participated in and the total return value. <a href="/get_actor/Tom Hanks" target="_blank">Click here</a> to try this function.</li>
        <li>This function retrieves information about a director, including the number of films they have directed and the total return value. <a href="/get_director/Steven Spielberg" target="_blank">Click here</a> to try this function.</li>
    </ol>
    """

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{title}</title>
        <style>
            table, th, td {{
                border: 1px solid black;
                border-collapse: collapse;
                padding: 8px;
                text-align: left;
            }}
        </style>
    </head>
    <body>
        <h1>{title}</h1>
        {body}
        {footer}
    </body>
    </html>
    """

meses = {
        "enero": "January",
        "febrero": "February",
        "marzo": "March",
        "abril": "April",
        "mayo": "May",
        "junio": "June",
        "julio": "July",
        "agosto": "August",
        "septiembre": "September",
        "octubre": "October",
        "noviembre": "November",
        "diciembre": "December"
    }

# 1 This function calculates the number of films released in a specific month. The month input should be provided in Spanish language.
@app.get("/cantidad_filmaciones_mes/{mes}")
def cantidad_filmaciones_mes(mes: str):

    # Convert month to spanish
    mes = mes.lower().strip()

    # Verify if the month is  in the dict
    if mes in meses:
        mes_en_ingles = meses[mes]
        cantidad = len(df[df["release_date"].str.contains(mes_en_ingles, case=False)])



    #cantidad = len(df[df["release_date"].str.contains(mes, case=False)])

    if cantidad == 0:
        return f"No se encontraron películas estrenadas en el mes de {mes}"

    # Generate link to view the films for the given month
    link_html = f'<a href="/view_films/{mes}" target="_blank">Ver películas</a>'

    response = f"{cantidad} películas fueron estrenadas en el mes de {mes}"
    response += f"<br/>{link_html}"

    return HTMLResponse(content=response, status_code=200)

@app.get("/view_films/{mes}")
def view_films_mes(mes: str):
    mes = mes.lower().strip()

    if mes in meses:
        mes_en_ingles = meses[mes]
        films = df[df["release_date"].str.contains(mes_en_ingles, case=False)][["title", "release_year"]].sort_values(by="release_year")

        if films.empty:
            return f"No se encontraron películas estrenadas en el mes de {mes}"

        table_html = films.to_html(index=False)

        page_title = f"Películas estrenadas en el mes de {mes}"

        complete_html = f"""
        <html>
        <head>
            <title>{page_title}</title>
        </head>
        <body>
            <h1>{page_title}</h1>
            {table_html}
        </body>
        </html>
        """

        return HTMLResponse(content=complete_html, status_code=200)
    else:
        return f"No se reconoce el mes '{mes}'. Por favor, ingresa un mes válido en español."


# 2 Calculate the number of films releasead in a specific day of the week. The day of the weew should be provided in Spanish Language.

dias = {
        "lunes": "Monday",
        "martes": "Tuesday",
        "miércoles": "Wednesday",
        "jueves": "Thursday",
        "viernes": "Friday",
        "sábado": "Saturday",
        "domingo": "Sunday"
    }

@app.get("/total_films_day/{dia}")
def total_films_day(dia: str):
    dia = dia.lower().strip()

    if dia in dias:
        dia_en_ingles = dias[dia]
        films = df[df["release_day"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8').str.lower().str.contains(dia_en_ingles, case=False)]

        if films.empty:
            return f"No se encontraron películas estrenadas en los días {dia}"

        link_html = f'<a href="/view_films_day/{dia}" target="_blank">Ver películas</a>'

        response = f"{len(films)} películas fueron estrenadas en los días {dia}"
        response += f"<br/>{link_html}"

        return HTMLResponse(content=response, status_code=200)
    else:
        return f"No se reconoce el día '{dia}'. Por favor, ingresa un día de la semana válido en español."

@app.get("/view_films_day/{dia}")
def view_films_day(dia: str):
    dia = dia.lower().strip()

    if dia in dias:
        dia_en_ingles = dias[dia]
        films = df[df["release_day"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8').str.lower().str.contains(dia_en_ingles, case=False)][["title", "release_year", "Director"]].sort_values(by="release_year")

        if films.empty:
            return f"No se encontraron películas estrenadas en los días {dia}"
    
    table_html = films.to_html(index=False)

    # Set the page title
    page_title = f"Películas estrenadas el día {dia}"

    # Embed the table in a complete HTML page
    complete_html = f"""
    <html>
    <head>
        <title>{page_title}</title>
    </head>
    <body>
        <h1>{page_title}</h1>
        {table_html}
    </body>
    </html>
    """

    return HTMLResponse(content=complete_html, status_code=200)


# 3 Returns the title, the year released and the score of the movie. If there is more than one movie with the same title, returns all of them
@app.get("/score_title/{film_title}")
def score_title(film_title: str):
    films = df[df["title"].str.lower() == film_title.lower()]
    if films.empty:
        return "No se encontró la filmación especificada."

    ordered_films = films.sort_values(by="release_year")

    table_html = "<table>"
    table_html += "<tr><th>Película</th><th>Año estreno</th><th>Score/Popularidad</th></tr>"

    for index, row in ordered_films.iterrows():
        title = row["title"]
        year_released = row["release_year"]
        score = row["popularity"]

        table_html += "<tr>"
        table_html += f"<td>{title}</td>"
        table_html += f"<td>{year_released}</td>"
        table_html += f"<td>{score}</td>"
        table_html += "</tr>"

    table_html += "</table>"

    return HTMLResponse(content=table_html, status_code=200)

# 4 Returns the title, the total of votes and the vote average

@app.get("/votos_titulo/{titulo_de_la_filmacion}", response_class=HTMLResponse)
def votos_titulo(titulo_de_la_filmacion: str):
    filmaciones = df[df["title"].str.lower() == titulo_de_la_filmacion.lower()]
    
    if filmaciones.empty:
        return "No se encontró la filmación especificada."
    
    respuestas = []
    
    for _, row in filmaciones.iterrows():
        cantidad_votos = row["vote_count"]
        
        if cantidad_votos < 2000:
            continue  # Saltar esta película si no cumple con la cantidad mínima de votos
        
        titulo = row["title"]
        promedio_votos = row["vote_average"]
        respuesta = f"<tr><td>{titulo}</td><td>{cantidad_votos}</td><td>{promedio_votos}</td></tr>"
        respuestas.append(respuesta)
    
    if not respuestas:
        return f"<h1>No se encontraron filmaciones que cumplan con la cantidad mínima de votos requerida (2000 votos).</h1>"
    
    tabla_html = "<table style='border-collapse: collapse; width: 100%;'>"
    tabla_html += "<tr style='border-bottom: 1px solid #ddd;'><th style='padding: 8px; text-align: left;'>Título</th>"
    tabla_html += "<th style='padding: 8px; text-align: left;'>Cantidad de votos</th>"
    tabla_html += "<th style='padding: 8px; text-align: left;'>Valor promedio de votaciones</th></tr>"
    tabla_html += "".join(respuestas)
    tabla_html += "</table>"
    
    return f"<h1>Filmaciones con título '{titulo_de_la_filmacion}'</h1>{tabla_html}"


# 5 Returns the total films and the average return
@app.get("/get_actor/{actor_name}")
def get_actor(actor_name):
    actor_films = df[df["actor_name"].str.contains(fr"\b{actor_name}\b", case=False, regex=True, na=False)]
    
    if actor_films.empty:
        return "No se encontró el actor especificado."

    film_count = len(actor_films)
    total_return = actor_films["return"].sum()
    average_return = total_return / film_count

    respuesta = f"El actor {actor_name} ha participado en {film_count} filmaciones. Ha conseguido un retorno total de {total_return} con un promedio de {average_return} por filmación."
    return respuesta



# 6 Returns the Director's information, how many films have been directed, and the total return value
@app.get("/get_director/{director_name}")
def get_director(director_name: str):
    # Filter movies by director
    director_movies = df[df['Director'].str.contains(fr"\b{director_name}\b", case=False, regex=True, na=False)]

    if director_movies.empty:
        return "No se encontró el director especificado."

    film_count = len(director_movies)
    total_return = director_movies['return'].sum()
    answer = f"El director {director_name} ha dirigido {film_count} pelicula(s). Con un ROI total de {total_return}"

    # HTML response
    movies_table = director_movies[['Director', 'title', 'release_date', 'return', 'budget', 'revenue']]
    movies_table_html = movies_table.to_html()

    # text and table generated
    response_content = f"<h1>{answer}</h1>{movies_table_html}"
    return HTMLResponse(content=response_content)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10000)
