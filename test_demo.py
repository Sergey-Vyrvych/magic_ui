import re
from playwright.sync_api import Page, expect
from time import sleep


def test_one(page: Page):
    page.goto('https://www.google.com')
    search_field = page.get_by_role('combobox')
    search_field.fill('cat')
    page.keyboard.press('Enter')
    expect(page).to_have_title(re.compile('^cat'))


def test_by_role(page: Page):
    page.goto('https://magento.softwaretestingboard.com/')
    page.get_by_role('menuitem', name="What's New").click()
    page.get_by_role('link', name='Search terms').click()


def test_by_text(page: Page):
    page.goto('https://www.qa-practice.com/')
    sleep(2)
    page.get_by_text('Single UI Elements').click()
    sleep(2)


def test_by_label(page: Page):
    sleep(2)
    page.goto('https://www.qa-practice.com/elements/input/simple')
    page.get_by_label('Text string').fill('wsfsfsdfssfd')
    sleep(3)



def test_by_placeholder(page: Page):
    sleep(3)
    page.goto('https://www.qa-practice.com/elements/input/simple')
    page.get_by_placeholder('Submit me').fill('sdfdsfsdf')
    sleep(3)


def test_by_alt_text(page: Page):
    sleep(3)
    page.goto('https://www.epam.com/')
    page.get_by_alt_text('The Complex Path of GenAI Adoption').click()
    sleep(2)


def test_by_title(page: Page):
    page.goto('https://www.google.com')
    page.get_by_title('Поиск').fill('cat')
    sleep(2)


def test_by_testis(page: Page):
    page.goto('https://www.airbnb.com/')
    page.get_by_test_id('')