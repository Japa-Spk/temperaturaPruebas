from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from src.testproject.classes import DriverStepSettings, StepSettings
from src.testproject.decorator import report_assertion_errors
from src.testproject.enums import SleepTimingType
from src.testproject.sdk.drivers import webdriver
import pytest


"""
This pytest test was automatically generated by TestProject
    Project: My first Project
    Package: TestProject.temperatura.regAutoDatos
    Test: Registro Automático de Datos
    Generated by: JOSE ANDREI PINTO AVILA (japinto08@ucatolica.edu.co)
    Generated on 10/04/2021, 23:26:53
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="Lt9WBjdUZ31hSK6CDXfKlxOXlr7M_O5qW4VrqOMOvFc",
                              project_name="My first Project",
                              job_name="Registro Automático de Datos")
    step_settings = StepSettings(timeout=15000,
                                 sleep_time=500,
                                 sleep_timing_type=SleepTimingType.Before)
    with DriverStepSettings(driver, step_settings):
        yield driver
    driver.quit()


@report_assertion_errors
def test_main(driver):
    """Se realiza una peticion a una API de clima donde se realiza el ajuste de datos automaticamente por el backend."""
    # Test Parameters
    # Auto generated application URL parameter
    ApplicationURL = "http://localhost:3000/"

    # 1. Navigate to '{ApplicationURL}'
    # Navigates the specified URL (Auto-generated)
    driver.get(f'{ApplicationURL}')

    # 2. Click 'Iniciar Sesion'
    iniciar_sesion = driver.find_element(By.XPATH,
                                         "//a[. = 'Iniciar Sesion']")
    iniciar_sesion.click()

    # 3. Click 'email1'
    email1 = driver.find_element(By.CSS_SELECTOR,
                                 "#email")
    email1.click()

    # 4. Type 'japinto08@ucatolica.edu.co' in 'email'
    email = driver.find_element(By.CSS_SELECTOR,
                                "#email")
    email.send_keys("japinto08@ucatolica.edu.co")

    # 5. Click 'password'
    password = driver.find_element(By.CSS_SELECTOR,
                                   "#password")
    password.click()

    # 6. Type '123456' in 'password'
    password = driver.find_element(By.CSS_SELECTOR,
                                   "#password")
    password.send_keys("123456")

    # 7. Click 'Iniciar'
    iniciar = driver.find_element(By.XPATH,
                                  "//button[. = 'Iniciar']")
    iniciar.click()

    # 8. Click 'Formulario'
    formulario = driver.find_element(By.XPATH,
                                     "//a[. = 'Formulario']")
    formulario.click()

    # 9. Click 'Nuevo Registro Automatico'
    nuevo_registro_automatico = driver.find_element(By.XPATH,
                                                    "//button[. = 'Nuevo Registro Automatico']")
    nuevo_registro_automatico.click()

    # 10. Click 'FormControlPais'
    formcontrolpais = driver.find_element(By.CSS_SELECTOR,
                                          "#FormControlPais")
    formcontrolpais.click()

    # 11. Select the '1' option in 'FormControlPais'
    formcontrolpais = driver.find_element(By.CSS_SELECTOR,
                                          "#FormControlPais")
    Select(formcontrolpais).select_by_value("1")

    # 12. Click 'FormControlPais'
    formcontrolpais = driver.find_element(By.CSS_SELECTOR,
                                          "#FormControlPais")
    formcontrolpais.click()

    # 13. Click 'id_ciudad'
    id_ciudad = driver.find_element(By.CSS_SELECTOR,
                                    "#FormControlCiudad")
    id_ciudad.click()

    # 14. Select the '3' option in 'id_ciudad'
    id_ciudad = driver.find_element(By.CSS_SELECTOR,
                                    "#FormControlCiudad")
    Select(id_ciudad).select_by_value("3")

    # 15. Click 'id_ciudad'
    id_ciudad = driver.find_element(By.CSS_SELECTOR,
                                    "#FormControlCiudad")
    id_ciudad.click()

    # 16. Click 'Guardar Auto'
    guardar_auto = driver.find_element(By.XPATH,
                                       "//button[. = 'Guardar Auto']")
    guardar_auto.click()
