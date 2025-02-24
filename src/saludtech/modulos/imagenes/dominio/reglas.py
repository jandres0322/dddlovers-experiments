def validar_tamano_imagen(metadatos):
    if metadatos.tamano_mb > 5000:
        raise ValueError("El tamaño de la imagen no puede superar los 5GB.")