# Escritura y Lectura de Archivo de Texto

# Escritura de Archivo de Texto
# Abre el archivo my_notes.txt en modo escritura ('w'). Si no existe, lo crea.
with open('my_notes.txt', 'w') as file:
    # Escribe al menos tres líneas de notas personales en el archivo.
    file.write("Mi primera nota: Hoy aprendí sobre manejo de archivos en Python.\n")
    file.write("Mi segunda nota: Es importante cerrar los archivos después de usarlos.\n")
    file.write("Mi tercera nota: Practicaré más sobre lectura y escritura.\n")

print("Archivo 'my_notes.txt' creado y escrito exitosamente.")

# Lectura de Archivo de Texto
# Abre el archivo my_notes.txt en modo lectura ('r').
with open('my_notes.txt', 'r') as file:
    print("\nContenido del archivo 'my_notes.txt':")
    # Lee el contenido del archivo línea por línea utilizando el método adecuado.
    # Muestra en la consola cada línea leída.
    line = file.readline()
    while line:
        print(line, end='')
        line = file.readline()

# El archivo se cierra automáticamente al salir del bloque 'with'

print("\n\nLectura del archivo completada.")
