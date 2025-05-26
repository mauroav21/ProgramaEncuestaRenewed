from selenium import webdriver
from selenium.webdriver.edge.service import Service 


edge_driver_path = 'C:\dedge\msedgedriver.exe'
service = Service(executable_path=edge_driver_path)
driver = webdriver.Edge(service=service)


driver.get("https://itsaltillo.mindbox.app/login/alumno")
driver.close()

