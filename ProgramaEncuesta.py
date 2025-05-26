import os
import time
import tkinter as tk
from tkinter import messagebox, ttk

from selenium import webdriver
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
    WebDriverException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# Function to start the automation
def iniciar_automatizacion():
    matricula = entry_matricula.get()
    contrasena = entry_contrasena.get()

    if not matricula or not contrasena:
        messagebox.showwarning("Campos vacíos", "Por favor, completa todos los campos.")
        return

    messagebox.showinfo("Éxito", "La automatización ha comenzado.")

    # Path to your Edge WebDriver
    edge_driver_path = 'C:\Users\mauro\Documents\TecNM\8 semestre\ProgramaEncuesta\msedgedriver.exe'
    service = Service(executable_path=edge_driver_path)
    driver = webdriver.Edge(service=service)

    try:  # Main try block for the entire automation process
        driver.get("https://itsaltillo.mindbox.app/login/alumno")

        # Login process
        campo_texto_user = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "ncontrol"))
        )
        campo_texto_user.send_keys(matricula)

        campo_texto_pwd = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, 'password'))
        )
        campo_texto_pwd.send_keys(contrasena)

        boton_login = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'btn'))
        )
        boton_login.click()

        time.sleep(6)  # Give it a moment to redirect after login

        # Navigate to evaluations
        buscador_evaluaciones = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID, 'menu-search-bar'))
        )
        buscador_evaluaciones.click()

        buscador_evaluaciones_text = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.TAG_NAME, 'input'))
        )
        buscador_evaluaciones_text.send_keys('Evaluación docente')
        time.sleep(3)

        buscador_evaluacion_docenteA = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.ID, 'search-result-container'))
        )
        buscador_evaluacion_docenteA.click()

        time.sleep(6)  # Wait a bit longer for the first evaluation page to load

        # --- Main loop to handle multiple evaluation pages ---
        page_counter = 1
        # Set the number of the last question page before the comments section
        # If comments are on page 11, then the last question page is 10.
        LAST_QUESTION_PAGE = 10

        while True:
            print(f"\n--- Procesando Página de Evaluación #{page_counter} ---")

            # --- Handle the comment page (if it's the last page, i.e., page 11) ---
            if page_counter > LAST_QUESTION_PAGE:
                print(f"Detectada posible página de comentarios (Página {page_counter}).")

                # Take screenshot for debugging if it fails here
                screenshot_name = f"posible_comentarios_pagina_{page_counter}.png"
                driver.save_screenshot(os.path.join(os.getcwd(), screenshot_name))
                print(f"*** Captura de pantalla de posible página de comentarios guardada como: {screenshot_name} ***")

                try:  # This 'try' block handles comment page interactions
                    # Wait for the panel-body of the comment section to be present.
                    WebDriverWait(driver, 15).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, ".panel-body"))
                    )

                    # Use a precise XPath based on the HTML you provided for the textarea
                    # Now using find_elements to get ALL matching textareas
                    comment_textarea_xpath = "//div[@class='form-group']/label[text()='Comentarios']/following-sibling::textarea[1]"
                    
                    # Find ALL textareas that match the criteria
                    comment_textareas = WebDriverWait(driver, 15).until(
                        EC.presence_of_all_elements_located((By.XPATH, comment_textarea_xpath))
                    )
                    
                    if comment_textareas:
                        print(f"Se encontraron {len(comment_textareas)} secciones de comentarios. Escribiendo 'Excelente Docente' en cada una.")
                        for i, textarea in enumerate(comment_textareas):
                            try:
                                # Ensure textarea is visible and clickable before sending keys
                                driver.execute_script("arguments[0].scrollIntoView(true);", textarea)
                                WebDriverWait(driver, 5).until(EC.element_to_be_clickable(textarea))
                                textarea.send_keys("Excelente Docente")
                                print(f"  -> Comentario {i+1} llenado.")
                            except Exception as e:
                                print(f"  -> ERROR al llenar comentario {i+1}: {e}")
                                # Continue to try filling other textareas even if one fails
                                continue 
                        time.sleep(1) # Small pause to let the text appear
                    else:
                        print("ERROR: No se encontraron textareas de comentarios con el XPath especificado.")
                        time.sleep(999) # Keep browser open for debugging
                        break # Exit the loop if no textareas are found

                    # Attempt to click the "Continuar" or "Finalizar" button
                    xpath_submit_comment_button = "//button[@type='submit' and (contains(text(), 'Continuar') or contains(text(), 'Finalizar') or .//i[contains(@class, 'fa-check')] )]"
                    submit_comment_button = WebDriverWait(driver, 15).until(
                        EC.element_to_be_clickable((By.XPATH, xpath_submit_comment_button))
                    )
                    submit_comment_button.click()
                    print("Comentario(s) enviado(s) y botón de continuar/finalizar clickeado.")
                    time.sleep(5)  # Wait for final action or redirection
                    break  # Exit the main loop, as the process is finished.

                except TimeoutException:
                    print("TIMEOUT: No se pudo encontrar el textarea de comentarios o el botón final. El proceso podría haber terminado o hay un error.")
                    time.sleep(999)  # Keep browser open for manual debugging if this fails
                    break
                except NoSuchElementException:
                    print("NO_SUCH_ELEMENT: No se encontró el textarea o el botón final para comentarios.")
                    time.sleep(999)
                    break
                except Exception as e: # Generic catch for any other error in comment handling
                    print(f"ERROR_COMENTARIOS: Error inesperado al manejar la sección de comentarios: {e}")
                    time.sleep(999)
                    break

            # --- Handle question pages (when page_counter <= LAST_QUESTION_PAGE) ---
            else:
                try:  # This 'try' block checks for the presence of questions on the page
                    # Wait for the presence of .panel-body, indicating a question page.
                    WebDriverWait(driver, 15).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, ".panel-body"))
                    )
                    print(f"La estructura de preguntas para la Página {page_counter} parece haber cargado completamente.")

                    # Try to wait if there's a loading overlay
                    try: # This 'try' block specifically handles the loading overlay
                        WebDriverWait(driver, 5).until(
                            EC.invisibility_of_element_located((By.CLASS_NAME, "loading-overlay-class"))
                        )
                        print("El overlay de carga ha desaparecido (o no existe).")
                    except TimeoutException: # Catches if overlay doesn't disappear in time
                        print("El overlay de carga no desapareció a tiempo o no se encontró. Continuando...")
                    except Exception as e: # Generic catch for any other overlay error
                        print(f"Error al manejar el overlay: {e}")


                    question_sections = WebDriverWait(driver, 20).until(
                        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".panel-body"))
                    )

                    if not question_sections:
                        print("No se encontraron secciones de preguntas en esta página. Posiblemente la última página o un error.")
                        break

                    for section_index, section in enumerate(question_sections):
                        questions_legends = section.find_elements(By.CSS_SELECTOR, "legend.text-sm.font-bold")

                        for i, question_legend in enumerate(questions_legends):
                            try: # This 'try' block handles individual question processing
                                question_num_str = question_legend.text.split(' ')[0].replace('-', '').strip()
                                question_num = int(question_num_str)

                                print(f"  --> Página {page_counter}, Panel {section_index + 1}, Procesando Pregunta {question_num}.")

                                xpath_label_value_5 = "./following-sibling::div[1]//label[./input[@type='radio' and @value='5']]"

                                print(f"      XPATH de la leyenda al label: {xpath_label_value_5}")

                                label_to_click = WebDriverWait(question_legend, 15).until(
                                    EC.presence_of_element_located((By.XPATH, xpath_label_value_5))
                                )

                                print(f"  --> Etiqueta para Pregunta {question_num} encontrada. Intentando hacer clic.")

                                driver.execute_script("arguments[0].scrollIntoView(true);", label_to_click)
                                time.sleep(0.5)

                                WebDriverWait(driver, 15).until(
                                    EC.element_to_be_clickable(label_to_click)
                                )
                                driver.execute_script("arguments[0].click();", label_to_click)  # Click with JavaScript

                                print(f"Página {page_counter}, Panel {section_index + 1}, Pregunta {question_num}: Opción 'Totalmente de acuerdo' seleccionada.")

                            except TimeoutException:
                                print(f"TIMEOUT: La etiqueta para la pregunta {question_num} en el panel {section_index + 1} no se encontró o no era clickeable.")
                                screenshot_name = f"error_pagina_{page_counter}_panel_{section_index+1}_pregunta_{question_num}.png"
                                driver.save_screenshot(os.path.join(os.getcwd(), screenshot_name))
                                print(f"*** Captura de pantalla guardada como: {screenshot_name} ***")
                                continue # Continue to the next question
                            except NoSuchElementException:
                                print(f"NO_SUCH_ELEMENT: No se encontró el input o la etiqueta para la pregunta {question_num} en el panel {section_index + 1}.")
                                continue # Continue to the next question
                            except Exception as e: # Generic catch for any other error during question processing
                                print(f"ERROR_DESCONOCIDO: al procesar la pregunta {question_num} en el panel {section_index + 1}: {e}")
                                continue # Continue to the next question

                    # --- Attempt to click "Continuar" to advance to the next section/page ---
                    print("Intentando hacer clic en 'Continuar'...")
                    xpath_continue_button = "//button[@type='submit' and (contains(@class, 'btn') or contains(text(), 'Continuar') or contains(text(), 'Finalizar'))]"

                    try: # This 'try' block handles clicking the "Continuar" button
                        click_continuar = WebDriverWait(driver, 15).until(
                            EC.element_to_be_clickable((By.XPATH, xpath_continue_button))
                        )
                        click_continuar.click()
                        print("Clic en 'Continuar' exitoso.")
                        page_counter += 1
                        time.sleep(7)  # Wait a bit longer for the next page to load
                    except TimeoutException:
                        print("TIMEOUT: El botón 'Continuar' no se encontró o no era clickeable. Asumiendo que es la última página de preguntas o la página de comentarios.")
                        break  # If "Continuar" is not found, break from question loop to handle comments or finish.
                    except Exception as e: # Generic catch for any other error when clicking continue
                        print(f"ERROR_GENERAL: al procesar la página {page_counter} al intentar continuar: {e}")
                        break

                except TimeoutException: # This catch is for the initial WebDriverWait for .panel-body on question pages
                    print(f"La Página {page_counter} no parece ser una página de preguntas con '.panel-body'. Podría ser la página de comentarios o el final del proceso.")
                    break # Break from the while loop to allow the comment handling logic (or end of process) to take over.
                except Exception as e: # Generic catch for any other error in the main question page handling
                    print(f"ERROR_PRINCIPAL_PAGINA_PREGUNTAS: Error inesperado al procesar la página de preguntas {page_counter}: {e}")
                    time.sleep(999) # Keep browser open for debugging
                    break

        print("\n--- Proceso de evaluación completado o no hay más páginas. ---")

    except Exception as main_e: # Catch-all for any errors not caught by more specific blocks
        messagebox.showerror("Error de Automatización", f"Ocurrió un error principal: {main_e}")
        print(f"Error principal durante el proceso de la encuesta: {main_e}")

    finally: # This block always executes, regardless of errors
        if driver:
            driver.quit()
            print("Navegador cerrado.")


# --- Tkinter GUI Setup ---
ventana = tk.Tk()
ventana.title("ProgramaEncuestaRenew")
ventana.geometry("400x250")
ventana.configure(bg="#f0f4f7")

style = ttk.Style()
style.configure("TLabel", font=("Segoe UI", 11), background="#f0f4f7")
style.configure("TEntry", font=("Segoe UI", 11))
style.configure("TButton", font=("Segoe UI", 11), padding=6)

frame = ttk.Frame(ventana, padding=20)
frame.pack(expand=True)

ttk.Label(frame, text="Inicio de Sesión", font=("Segoe UI", 14, "bold")).grid(column=0, row=0, columnspan=2, pady=10)

ttk.Label(frame, text="Matrícula:").grid(column=0, row=1, sticky="e", pady=5, padx=5)
entry_matricula = ttk.Entry(frame, width=25)
entry_matricula.grid(column=1, row=1)

ttk.Label(frame, text="Contraseña:").grid(column=0, row=2, sticky="e", pady=5, padx=5)
entry_contrasena = ttk.Entry(frame, width=25, show="*")
entry_contrasena.grid(column=1, row=2)

ttk.Button(frame, text="Iniciar Evaluación", command=iniciar_automatizacion).grid(column=0, row=3, columnspan=2, pady=20)

ventana.mainloop()