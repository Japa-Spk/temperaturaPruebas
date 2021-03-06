from selenium.webdriver.common.by import By
from src.testproject.classes import DriverStepSettings, StepSettings
from src.testproject.decorator import report_assertion_errors
from src.testproject.enums import SleepTimingType
from src.testproject.sdk.drivers import webdriver
import pytest


"""
This pytest test was automatically generated by TestProject
    Project: My first Project
    Package: TestProject.temperatura.login
    Test: Inicio de Sesion
    Generated by: JOSE ANDREI PINTO AVILA (japinto08@ucatolica.edu.co)
    Generated on 10/04/2021, 23:27:39
"""


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(token="Lt9WBjdUZ31hSK6CDXfKlxOXlr7M_O5qW4VrqOMOvFc",
                              project_name="My first Project",
                              job_name="Inicio de Sesion")
    step_settings = StepSettings(timeout=15000,
                                 sleep_time=500,
                                 sleep_timing_type=SleepTimingType.Before)
    with DriverStepSettings(driver, step_settings):
        yield driver
    driver.quit()


@report_assertion_errors
def test_main(driver):
    """Se espera que al ingresar el email y contraseña previamente registrado en el módulo de registro y dar click en el botón de Iniciar Sesión se permita ver la opción de seleccionar la ciudad de la cual queremos ver la temperatura."""
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

    # 3. Click 'email'
    email = driver.find_element(By.CSS_SELECTOR,
                                "#email")
    email.click()

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
