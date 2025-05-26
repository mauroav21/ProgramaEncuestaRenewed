
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

Este software ha sido desarrollado únicamente con fines educativos, como ejemplo de automatización con Selenium y manipulación de interfaces gráficas con Tkinter. No está destinado para su uso en entornos de producción ni para la automatización masiva sin supervisión.

El uso de esta herramienta para automatizar el llenado de evaluaciones dentro de plataformas oficiales, como el portal de evaluación del TecNM o sistemas similares, puede violar sus términos y condiciones de uso. Además, este tipo de acciones podrían ser consideradas como prácticas deshonestas o no autorizadas por parte de las instituciones educativas.

Cada usuario es completamente responsable del uso que le dé a este software. Ni el autor ni los colaboradores del proyecto se hacen responsables por sanciones académicas, administrativas o legales que puedan derivarse de un uso indebido de la herramienta. Se recomienda encarecidamente consultar con la institución correspondiente y obtener permiso explícito antes de emplear este tipo de automatización en plataformas institucionales.

Recuerda: la integridad académica y el cumplimiento de las normas institucionales son fundamentales para una formación profesional ética y responsable.



## Authors

- [@mauroav21](https://www.github.com/mauroav21)

