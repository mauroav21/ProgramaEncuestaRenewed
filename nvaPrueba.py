
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time


# Ruta del driver#

# Ruta del controlador de Microsoft Edge
edge_driver_path = 'C:\dedge\msedgedriver.exe'

# Opciones del navegador
options = webdriver.EdgeOptions()
options.use_chromium = True

# Configurar el controlador de Microsoft Edge
driver = webdriver.Edge(executable_path=edge_driver_path, options=options)


# Ruta del forulario#
driver.get('https://itsaltillo.mindbox.app/login/alumno')

# Usuario


campo_texto_user = driver.find_element(By.ID, "ncontrol")
campo_texto_user.send_keys('')
driver.find_element
# Contraeña
campo_texto_pwd = driver.find_element(By.ID, 'password')
campo_texto_pwd.send_keys('')

# Click boton login
boton_login = driver.find_element(By.CLASS_NAME,'btn')
boton_login.click()

time.sleep(10)

# Click evaluaciones
buscador_evaluaciones = driver.find_element(By.ID, 'menu-search-bar')
buscador_evaluaciones.click()

# Insertar texto en buscador
buscador_evaluaciones_text = driver.find_element(By.TAG_NAME, 'input')
buscador_evaluaciones_text.send_keys('Evaluación docente')
time.sleep(3)

# Click opcion
buscador_evaluacion_docenteA = driver.find_element(By.ID, 'search-result-container')
buscador_evaluacion_docenteA.click()

time.sleep(3)


# Click en continuar
click_continuar = driver.find_element(By.CLASS_NAME, 'fa.fa-arrow-right')
click_continuar.click()

time.sleep(7)

# cLICK EN CADA CASILLA USANDO XPAD

# corresconde a calculo
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Af3"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)

seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Af3"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Af3"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)
seleccionar_op4 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q4_Af3"]'))
seleccionar_op4.select_by_value('5')
time.sleep(1)
seleccionar_op5 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q5_Af3"]'))
seleccionar_op5.select_by_value('5')

#corresponde a ed
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Bf3"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)
seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Bf3"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Bf3"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)
seleccionar_op4 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q4_Bf3"]'))
seleccionar_op4.select_by_value('5')
time.sleep(1)
seleccionar_op5 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q5_Bf3"]'))
seleccionar_op5.select_by_value('5')

# corresponde a tbd
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Cf5"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)
seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Cf5"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Cf5"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)
seleccionar_op4 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q4_Cf5"]'))
seleccionar_op4.select_by_value('5')
time.sleep(1)
seleccionar_op5 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q5_Cf5"]'))
seleccionar_op5.select_by_value('5')

#corresponde a io
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Df3"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)
seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Df3"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Df3"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)
seleccionar_op4 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q4_Df3"]'))
seleccionar_op4.select_by_value('5')
time.sleep(1)
seleccionar_op5 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q5_Df3"]'))
seleccionar_op5.select_by_value('5')

#corresponde a progra web
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Df8"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)
seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Df8"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Df8"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)
seleccionar_op4 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q4_Df8"]'))
seleccionar_op4.select_by_value('5')
time.sleep(1)
seleccionar_op5 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q5_Df8"]'))
seleccionar_op5.select_by_value('5')

#corresponde a principios electricos
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Ff4"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)
seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Ff4"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Ff4"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)
seleccionar_op4 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q4_Ff4"]'))
seleccionar_op4.select_by_value('5')
time.sleep(1)
seleccionar_op5 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q5_Ff4"]'))
seleccionar_op5.select_by_value('5')

#
# 2 /11
#
#


boton_continuar_e1 = driver.find_element(By.CLASS_NAME,'btn.btn-primary')
boton_continuar_e1.click()
time.sleep(10)


# corresconde a calculo
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Af3"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)

seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Af3"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Af3"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)


#corresponde a ed
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Bf3"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)
seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Bf3"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Bf3"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)


# corresponde a tbd
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Cf5"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)
seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Cf5"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Cf5"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)


#corresponde a io
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Df3"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)
seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Df3"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Df3"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)


#corresponde a progra web
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Df8"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)
seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Df8"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Df8"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)


#corresponde a principios electricos
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Ff4"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)
seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Ff4"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Ff4"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)


#
# 3 /11
#
#


boton_continuar_e1 = driver.find_element(By.CLASS_NAME,'btn.btn-primary')
boton_continuar_e1.click()
time.sleep(10)


# corresconde a calculo
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Af3"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)

seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Af3"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Af3"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)
seleccionar_op4 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q4_Af3"]'))
seleccionar_op4.select_by_value('5')
time.sleep(1)
seleccionar_op5 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q5_Af3"]'))
seleccionar_op5.select_by_value('5')

#corresponde a ed
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Bf3"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)
seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Bf3"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Bf3"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)
seleccionar_op4 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q4_Bf3"]'))
seleccionar_op4.select_by_value('5')
time.sleep(1)
seleccionar_op5 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q5_Bf3"]'))
seleccionar_op5.select_by_value('5')

# corresponde a tbd
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Cf5"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)
seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Cf5"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Cf5"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)
seleccionar_op4 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q4_Cf5"]'))
seleccionar_op4.select_by_value('5')
time.sleep(1)
seleccionar_op5 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q5_Cf5"]'))
seleccionar_op5.select_by_value('5')

#corresponde a io
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Df3"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)
seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Df3"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Df3"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)
seleccionar_op4 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q4_Df3"]'))
seleccionar_op4.select_by_value('5')
time.sleep(1)
seleccionar_op5 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q5_Df3"]'))
seleccionar_op5.select_by_value('5')

#corresponde a progra web
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Df8"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)
seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Df8"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Df8"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)
seleccionar_op4 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q4_Df8"]'))
seleccionar_op4.select_by_value('5')
time.sleep(1)
seleccionar_op5 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q5_Df8"]'))
seleccionar_op5.select_by_value('5')

#corresponde a principios electricos
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Ff4"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)
seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Ff4"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Ff4"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)
seleccionar_op4 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q4_Ff4"]'))
seleccionar_op4.select_by_value('5')
time.sleep(1)
seleccionar_op5 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q5_Ff4"]'))
seleccionar_op5.select_by_value('5')

time.sleep(7)

#
# 4 /11
#
#


boton_continuar_e1 = driver.find_element(By.CLASS_NAME,'btn.btn-primary')
boton_continuar_e1.click()
time.sleep(10)


# corresconde a calculo
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Af3"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)

seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Af3"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Af3"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)
seleccionar_op4 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q4_Af3"]'))
seleccionar_op4.select_by_value('5')
time.sleep(1)
seleccionar_op5 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q5_Af3"]'))
seleccionar_op5.select_by_value('5')
time.sleep(1)
seleccionar_op6 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q6_Af3"]'))
seleccionar_op6.select_by_value('5')
time.sleep(1)
seleccionar_op7 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q7_Af3"]'))
seleccionar_op7.select_by_value('5')

#corresponde a ed
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Bf3"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)
seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Bf3"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Bf3"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)
seleccionar_op4 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q4_Bf3"]'))
seleccionar_op4.select_by_value('5')
time.sleep(1)
seleccionar_op5 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q5_Bf3"]'))
seleccionar_op5.select_by_value('5')
time.sleep(1)
seleccionar_op6 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q6_Bf3"]'))
seleccionar_op6.select_by_value('5')
time.sleep(1)
seleccionar_op7 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q7_Bf3"]'))
seleccionar_op7.select_by_value('5')

# corresponde a tbd
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Cf5"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)
seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Cf5"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Cf5"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)
seleccionar_op4 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q4_Cf5"]'))
seleccionar_op4.select_by_value('5')
time.sleep(1)
seleccionar_op5 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q5_Cf5"]'))
seleccionar_op5.select_by_value('5')
time.sleep(1)
seleccionar_op6 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q6_Cf5"]'))
seleccionar_op6.select_by_value('5')
time.sleep(1)
seleccionar_op7 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q7_Cf5"]'))
seleccionar_op7.select_by_value('5')

#corresponde a io
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Df3"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)
seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Df3"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Df3"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)
seleccionar_op4 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q4_Df3"]'))
seleccionar_op4.select_by_value('5')
time.sleep(1)
seleccionar_op5 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q5_Df3"]'))
seleccionar_op5.select_by_value('5')
time.sleep(1)
seleccionar_op6 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q6_Df3"]'))
seleccionar_op6.select_by_value('5')
time.sleep(1)
seleccionar_op7 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q7_Df3"]'))
seleccionar_op7.select_by_value('5')

#corresponde a progra web
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Df8"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)
seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Df8"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Df8"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)
seleccionar_op4 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q4_Df8"]'))
seleccionar_op4.select_by_value('5')
time.sleep(1)
seleccionar_op5 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q5_Df8"]'))
seleccionar_op5.select_by_value('5')
time.sleep(1)
seleccionar_op6 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q6_Df8"]'))
seleccionar_op6.select_by_value('5')
time.sleep(1)
seleccionar_op7 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q7_Df8"]'))
seleccionar_op7.select_by_value('5')

#corresponde a principios electricos
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Ff4"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)
seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Ff4"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Ff4"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)
seleccionar_op4 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q4_Ff4"]'))
seleccionar_op4.select_by_value('5')
time.sleep(1)
seleccionar_op5 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q5_Ff4"]'))
seleccionar_op5.select_by_value('5')
time.sleep(1)
seleccionar_op6 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q6_Ff4"]'))
seleccionar_op6.select_by_value('5')
time.sleep(1)
seleccionar_op7 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q7_Ff4"]'))
seleccionar_op7.select_by_value('5')

time.sleep(7)


#
# 5 /11
#
#


boton_continuar_e1 = driver.find_element(By.CLASS_NAME,'btn.btn-primary')
boton_continuar_e1.click()
time.sleep(10)


# corresconde a calculo
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Af3"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)

seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Af3"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Af3"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)
seleccionar_op4 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q4_Af3"]'))
seleccionar_op4.select_by_value('5')
time.sleep(1)
seleccionar_op5 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q5_Af3"]'))
seleccionar_op5.select_by_value('5')
time.sleep(1)
seleccionar_op6 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q6_Af3"]'))
seleccionar_op6.select_by_value('5')
time.sleep(1)
seleccionar_op7 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q7_Af3"]'))
seleccionar_op7.select_by_value('5')

#corresponde a ed
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Bf3"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)
seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Bf3"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Bf3"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)
seleccionar_op4 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q4_Bf3"]'))
seleccionar_op4.select_by_value('5')
time.sleep(1)
seleccionar_op5 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q5_Bf3"]'))
seleccionar_op5.select_by_value('5')
time.sleep(1)
seleccionar_op6 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q6_Bf3"]'))
seleccionar_op6.select_by_value('5')
time.sleep(1)
seleccionar_op7 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q7_Bf3"]'))
seleccionar_op7.select_by_value('5')

# corresponde a tbd
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Cf5"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)
seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Cf5"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Cf5"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)
seleccionar_op4 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q4_Cf5"]'))
seleccionar_op4.select_by_value('5')
time.sleep(1)
seleccionar_op5 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q5_Cf5"]'))
seleccionar_op5.select_by_value('5')
time.sleep(1)
seleccionar_op6 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q6_Cf5"]'))
seleccionar_op6.select_by_value('5')
time.sleep(1)
seleccionar_op7 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q7_Cf5"]'))
seleccionar_op7.select_by_value('5')

#corresponde a io
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Df3"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)
seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Df3"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Df3"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)
seleccionar_op4 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q4_Df3"]'))
seleccionar_op4.select_by_value('5')
time.sleep(1)
seleccionar_op5 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q5_Df3"]'))
seleccionar_op5.select_by_value('5')
time.sleep(1)
seleccionar_op6 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q6_Df3"]'))
seleccionar_op6.select_by_value('5')
time.sleep(1)
seleccionar_op7 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q7_Df3"]'))
seleccionar_op7.select_by_value('5')

#corresponde a progra web
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Df8"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)
seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Df8"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Df8"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)
seleccionar_op4 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q4_Df8"]'))
seleccionar_op4.select_by_value('5')
time.sleep(1)
seleccionar_op5 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q5_Df8"]'))
seleccionar_op5.select_by_value('5')
time.sleep(1)
seleccionar_op6 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q6_Df8"]'))
seleccionar_op6.select_by_value('5')
time.sleep(1)
seleccionar_op7 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q7_Df8"]'))
seleccionar_op7.select_by_value('5')

#corresponde a principios electricos
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Ff4"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)
seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Ff4"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Ff4"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)
seleccionar_op4 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q4_Ff4"]'))
seleccionar_op4.select_by_value('5')
time.sleep(1)
seleccionar_op5 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q5_Ff4"]'))
seleccionar_op5.select_by_value('5')
time.sleep(1)
seleccionar_op6 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q6_Ff4"]'))
seleccionar_op6.select_by_value('5')
time.sleep(1)
seleccionar_op7 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q7_Ff4"]'))
seleccionar_op7.select_by_value('5')

time.sleep(7)

time.sleep(7)

#
# 6 /11
#
#


boton_continuar_e1 = driver.find_element(By.CLASS_NAME,'btn.btn-primary')
boton_continuar_e1.click()
time.sleep(10)


# corresconde a calculo
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Af3"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)

seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Af3"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Af3"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)
seleccionar_op4 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q4_Af3"]'))
seleccionar_op4.select_by_value('5')
time.sleep(1)
seleccionar_op5 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q5_Af3"]'))
seleccionar_op5.select_by_value('5')
time.sleep(1)
seleccionar_op6 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q6_Af3"]'))
seleccionar_op6.select_by_value('5')
time.sleep(1)
seleccionar_op7 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q7_Af3"]'))
seleccionar_op7.select_by_value('5')
time.sleep(1)
seleccionar_op8 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q8_Af3"]'))
seleccionar_op8.select_by_value('5')


#corresponde a ed
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Bf3"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)
seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Bf3"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Bf3"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)
seleccionar_op4 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q4_Bf3"]'))
seleccionar_op4.select_by_value('5')
time.sleep(1)
seleccionar_op5 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q5_Bf3"]'))
seleccionar_op5.select_by_value('5')
time.sleep(1)
seleccionar_op6 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q6_Bf3"]'))
seleccionar_op6.select_by_value('5')
time.sleep(1)
seleccionar_op7 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q7_Bf3"]'))
seleccionar_op7.select_by_value('5')
time.sleep(1)
seleccionar_op8 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q8_Bf3"]'))
seleccionar_op8.select_by_value('5')

# corresponde a tbd
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Cf5"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)
seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Cf5"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Cf5"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)
seleccionar_op4 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q4_Cf5"]'))
seleccionar_op4.select_by_value('5')
time.sleep(1)
seleccionar_op5 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q5_Cf5"]'))
seleccionar_op5.select_by_value('5')
time.sleep(1)
seleccionar_op6 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q6_Cf5"]'))
seleccionar_op6.select_by_value('5')
time.sleep(1)
seleccionar_op7 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q7_Cf5"]'))
seleccionar_op7.select_by_value('5')
time.sleep(1)
seleccionar_op8 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q8_Cf5"]'))
seleccionar_op8.select_by_value('5')

#corresponde a io
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Df3"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)
seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Df3"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Df3"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)
seleccionar_op4 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q4_Df3"]'))
seleccionar_op4.select_by_value('5')
time.sleep(1)
seleccionar_op5 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q5_Df3"]'))
seleccionar_op5.select_by_value('5')
time.sleep(1)
seleccionar_op6 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q6_Df3"]'))
seleccionar_op6.select_by_value('5')
time.sleep(1)
seleccionar_op7 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q7_Df3"]'))
seleccionar_op7.select_by_value('5')
time.sleep(1)
seleccionar_op8 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q8_Df3"]'))
seleccionar_op8.select_by_value('5')

#corresponde a progra web
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Df8"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)
seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Df8"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Df8"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)
seleccionar_op4 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q4_Df8"]'))
seleccionar_op4.select_by_value('5')
time.sleep(1)
seleccionar_op5 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q5_Df8"]'))
seleccionar_op5.select_by_value('5')
time.sleep(1)
seleccionar_op6 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q6_Df8"]'))
seleccionar_op6.select_by_value('5')
time.sleep(1)
seleccionar_op7 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q7_Df8"]'))
seleccionar_op7.select_by_value('5')
time.sleep(1)
seleccionar_op8 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q8_Df8"]'))
seleccionar_op8.select_by_value('5')

#corresponde a principios electricos
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Ff4"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)
seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Ff4"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Ff4"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)
seleccionar_op4 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q4_Ff4"]'))
seleccionar_op4.select_by_value('5')
time.sleep(1)
seleccionar_op5 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q5_Ff4"]'))
seleccionar_op5.select_by_value('5')
time.sleep(1)
seleccionar_op6 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q6_Ff4"]'))
seleccionar_op6.select_by_value('5')
time.sleep(1)
seleccionar_op7 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q7_Ff4"]'))
seleccionar_op7.select_by_value('5')
time.sleep(1)
seleccionar_op8 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q8_Ff4"]'))
seleccionar_op8.select_by_value('5')

time.sleep(7)

#
# 7 /11
#
#


boton_continuar_e1 = driver.find_element(By.CLASS_NAME,'btn.btn-primary')
boton_continuar_e1.click()
time.sleep(10)


# corresconde a calculo
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Af3"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)

seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Af3"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Af3"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)


#corresponde a ed
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Bf3"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)
seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Bf3"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Bf3"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)


# corresponde a tbd
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Cf5"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)
seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Cf5"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Cf5"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)


#corresponde a io
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Df3"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)
seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Df3"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Df3"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)


#corresponde a progra web
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Df8"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)
seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Df8"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Df8"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)


#corresponde a principios electricos
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Ff4"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)
seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Ff4"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Ff4"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)

#
# 8 /11
#
#


boton_continuar_e1 = driver.find_element(By.CLASS_NAME,'btn.btn-primary')
boton_continuar_e1.click()
time.sleep(10)


# corresconde a calculo
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Af3"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)

seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Af3"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Af3"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)
seleccionar_op4 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q4_Af3"]'))
seleccionar_op4.select_by_value('5')


#corresponde a ed
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Bf3"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)
seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Bf3"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Bf3"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)
seleccionar_op4 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q4_Bf3"]'))
seleccionar_op4.select_by_value('5')


# corresponde a tbd
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Cf5"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)
seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Cf5"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Cf5"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)
seleccionar_op4 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q4_Cf5"]'))
seleccionar_op4.select_by_value('5')


#corresponde a io
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Df3"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)
seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Df3"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Df3"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)
seleccionar_op4 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q4_Df3"]'))
seleccionar_op4.select_by_value('5')


#corresponde a progra web
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Df8"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)
seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Df8"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Df8"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)
seleccionar_op4 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q4_Df8"]'))
seleccionar_op4.select_by_value('5')


#corresponde a principios electricos
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Ff4"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)
seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Ff4"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Ff4"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)
seleccionar_op4 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q4_Ff4"]'))
seleccionar_op4.select_by_value('5')

#
# 9 /11
#
#


boton_continuar_e1 = driver.find_element(By.CLASS_NAME,'btn.btn-primary')
boton_continuar_e1.click()
time.sleep(10)


# corresconde a calculo
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Af3"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)

seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Af3"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Af3"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)


#corresponde a ed
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Bf3"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)
seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Bf3"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Bf3"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)


# corresponde a tbd
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Cf5"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)
seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Cf5"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Cf5"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)


#corresponde a io
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Df3"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)
seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Df3"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Df3"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)


#corresponde a progra web
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Df8"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)
seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Df8"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Df8"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)


#corresponde a principios electricos
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Ff4"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)
seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Ff4"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Ff4"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)

#
# 10 /11
#
#


boton_continuar_e1 = driver.find_element(By.CLASS_NAME,'btn.btn-primary')
boton_continuar_e1.click()
time.sleep(10)


# corresconde a calculo
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Af3"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)

seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Af3"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Af3"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)


#corresponde a ed
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Bf3"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)
seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Bf3"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Bf3"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)


# corresponde a tbd
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Cf5"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)
seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Cf5"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Cf5"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)


#corresponde a io
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Df3"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)
seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Df3"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Df3"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)


#corresponde a progra web
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Df8"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)
seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Df8"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Df8"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)


#corresponde a principios electricos
seleccionar_op = Select(driver.find_element(By.XPATH, '//*[@id="answer_q1_Ff4"]'))
seleccionar_op.select_by_value('5')
print('si llegamos hasta aqui ')
time.sleep(1)
seleccionar_op2 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q2_Ff4"]'))
seleccionar_op2.select_by_value('5')
print('Si, tmb llegamos hasta aqui')
time.sleep(1)
seleccionar_op3 = Select(driver.find_element(By.XPATH, '//*[@id="answer_q3_Ff4"]'))
seleccionar_op3.select_by_value('5')
time.sleep(1)


#
# 11 /11
#
#


boton_continuar_e1 = driver.find_element(By.CLASS_NAME,'btn.btn-primary')
boton_continuar_e1.click()
time.sleep(10)

campo_texto_op = driver.find_element(By.ID, 'answer_Af3')
campo_texto_op.send_keys('excelente')

campo_texto_op = driver.find_element(By.ID, 'answer_Bf3')
campo_texto_op.send_keys('excelente')

campo_texto_op = driver.find_element(By.ID, 'answer_Cf5')
campo_texto_op.send_keys('excelente')

campo_texto_op = driver.find_element(By.ID, 'answer_Df3')
campo_texto_op.send_keys('excelente')

campo_texto_op = driver.find_element(By.ID, 'answer_Df8')
campo_texto_op.send_keys('excelente')

campo_texto_op = driver.find_element(By.ID, 'answer_Ff4')
campo_texto_op.send_keys('excelente')

boton_continuar_e1 = driver.find_element(By.CLASS_NAME,'btn.btn-primary')
boton_continuar_e1.click()
time.sleep(10)
