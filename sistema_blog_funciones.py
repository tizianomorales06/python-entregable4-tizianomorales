perfil_autor = {
    "nombre": "Tiziano Morales",
    "bio": "Desarrollador de software con experiencia en Python y desarrollo web. Apasionado por la tecnología y la innovación.",
    "especialidades": "Python",
    "redes_sociales": ["twitter : @tizianomorales", "linkedin : tizianomorales"]
}

estados_post = ("borrador", "publicado", "archivado")
etiquetas_blog = {"Python", "Django", "Web", "Backend", "Python"}

posts = [
    {
        "id": 1,
        "titulo": "Primeros pasos con Python",
        "contenido": "cuales son los codigos basicos del lenguaje y cual es su funcion",
        "autor": perfil_autor,
        "tags": ["Python", "Principiantes"],
        "estado": "publicado"
    },
    {
        "id": 2,
        "titulo": "Qué es Django",
        "contenido": "introduccion a Django",
        "autor": perfil_autor,
        "tags": ["Python", "Django", "Web"],
        "estado": "borrador"
    },
    {
        "id": 3,
        "titulo": "Organizando datos con diccionarios",
        "contenido": "que son los datos en Python, como se ordenan y su importancia",
        "autor": perfil_autor,
        "tags": ["Python", "Diccionarios"],
        "estado": "archivado"
    }
]
def validar_post(post):
    errores = []
    claves_requeridas = ["id", "titulo", "contenido", "tags", "estado", "autor"]

    for clave in claves_requeridas:
        if clave not in post:
            errores.append(f"Falta la clave '{clave}'")
    if "estado" in post and post.get("estado") not in estados_post:
        errores.append(f"Estado inválido: '{post.get('estado')}'")
    if "tags" in post and not isinstance(post.get("tags"), list):
        errores.append("El campo 'tags' debe ser una lista")

    return errores


def listar_posts(lista):
    if not lista:
        print("No hay posts para mostrar.")
        return

    for post in lista:
        titulo = post.get("titulo", "(sin título)")
        estado = post.get("estado", "(sin estado)")
        errores = validar_post(post)

        print(f"- ID: {post.get('id', '¿?')} | Título: {titulo} | Estado: {estado}")
        if errores:
            print(f"Post con errores de estructura: {', '.join(errores)}")


def buscar_por_titulo(lista, termino):
    resultados = []
    termino = termino.lower()  

    for post in lista:
        titulo = post.get("titulo", "").lower()
        if termino in titulo:
            resultados.append(post)

    return resultados


def filtrar_por_tag(lista, tag):
    resultados = []
    tag = tag.lower()

    for post in lista:
        tags_post = post.get("tags", [])
        if isinstance(tags_post, list):
            tags_lower = [t.lower() for t in tags_post]
            if tag in tags_lower:
                resultados.append(post)

    return resultados


def mostrar_menu():
    print("\n===== MENÚ DEL BLOG =====")
    print("1. Listar todos los posts")
    print("2. Buscar post por título")
    print("3. Filtrar posts por etiqueta")
    print("4. Ver perfil del autor")
    print("5. Salir")
    opcion = input("Elige una opción: ")
    return opcion


def mostrar_resultados(resultados, mensaje_vacio):
    if not resultados:
        print(mensaje_vacio)
    else:
        listar_posts(resultados)

if __name__ == "__main__":
    menu_activo = True

    while menu_activo:
        try:
            opcion = int(mostrar_menu())  
        except ValueError:
            print("Opción inválida. Debes ingresar un número del 1 al 5.")
            continue

        if opcion == 1:
            listar_posts(posts)

        elif opcion == 2:
            termino = input("Escribe el término a buscar en el título: ")
            resultados = buscar_por_titulo(posts, termino)
            mostrar_resultados(resultados, "No se encontraron posts con ese título.")

        elif opcion == 3:
            print(f"Etiquetas disponibles: {', '.join(etiquetas_blog)}")
            tag = input("Escribe la etiqueta a filtrar: ")
            resultados = filtrar_por_tag(posts, tag)
            mostrar_resultados(resultados, "No se encontraron posts con esa etiqueta.")

        elif opcion == 4:
            print("\n--- Perfil del autor ---")
            print(f"Nombre: {perfil_autor.get('nombre')}")
            print(f"Usuario: {perfil_autor.get('usuario')}")
            print(f"Email: {perfil_autor.get('contacto', {}).get('email', 'No disponible')}")
            print(f"Bio: {perfil_autor.get('bio')}")

        elif opcion == 5:
            print("Hasta luego!")
            menu_activo = False

        else:
            print("Opción inválida. Elige un número del 1 al 5.")
