
# ProgramaEncuestaRenew

Este proyecto es una herramienta automatizada que utiliza Selenium y una interfaz gráfica con Tkinter para facilitar el llenado de encuestas docentes en la plataforma Mindbox del Instituto Tecnológico de Saltillo.

## Características

- Interfaz gráfica amigable para ingresar matrícula y contraseña.
- Automatiza el proceso de login.
- Navega automáticamente hacia la sección de "Evaluación docente".
- Responde todas las preguntas de las encuestas seleccionando "Totalmente de acuerdo".
- Agrega automáticamente el comentario "Excelente Docente" en las secciones correspondientes.
- Captura pantallas para depuración en caso de errores.
- Manejo de excepciones y tiempos de espera para asegurar la robustez del proceso.

## Requisitos

- Python 3.x
- Navegador Microsoft Edge
- Edge WebDriver compatible con la versión de tu navegador
- Paquetes de Python:
  - selenium
  - tkinter (incluido con la mayoría de las instalaciones de Python)

## Instalación

1. Clona este repositorio o descarga los archivos.
2. Instala las dependencias necesarias:

```bash
pip install selenium
```

3. Asegúrate de tener `msedgedriver.exe` descargado y que su ruta sea correcta en el script:

```python
edge_driver_path = 'C:\Users\TU_USUARIO\Ruta\msedgedriver.exe'
```

## Uso

1. Ejecuta el script Python.
2. Ingresa tu matrícula y contraseña.
3. Presiona "Iniciar Evaluación".
4. El programa comenzará el proceso de evaluación de manera automática.

## Aviso

De momento esta como predetarminada la opción totalmente de acuerdo, y en comentarios el mensaje "Excelente Docente". Es posible editarlo antes de ejecutar el codigo.

## Advertencia

Este software se proporciona con fines educativos. El uso indebido puede violar los términos y condiciones del portal de evaluación. Asegúrate de contar con autorización antes de automatizar procesos en plataformas oficiales.



## Authors

- [@mauroav21](https://www.github.com/mauroav21)

