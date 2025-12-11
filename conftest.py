from datetime import datetime, timedelta
import random
import pytest
from selenium import webdriver
from faker import Faker

from data import Urls

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()
    driver.get(Urls.BASE_URL)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def user():
    fake_ru = Faker('ru_RU')
    user = {
        "first_name": fake_ru.first_name(),
        "second_name": fake_ru.middle_name(),
        "adress": fake_ru.address().replace('/', '').replace(')', '').replace('(', '')[:20],
        "phone": f'7{fake_ru.msisdn()[3:]}'
    }
    return user

@pytest.fixture
def comment():
    fake_ru = Faker('ru_RU')
    return fake_ru.text()

@pytest.fixture
def date():
    start_date = datetime.now()
    end_date = start_date + timedelta(days=30)
    total_days = (end_date - start_date).days
    random_days = random.randint(0, total_days)
    random_future_date = start_date + timedelta(days=random_days)
    return random_future_date.strftime('%d.%m.%Y')
