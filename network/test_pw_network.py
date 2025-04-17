from playwright.sync_api import Page, expect, Request, Response, Route
from time import sleep
import re
import json


def test_liten(page: Page):

    def print_request(request: Request):
        print('REQUEST:', request.post_data, request.url)

    sleep(3)
    page.on('request', print_request)
    page.on('response', lambda response: print('RESPONSE:', response.url, response.status))
    page.goto('https://www.qa-practice.com/')
    page.get_by_role('link', name='Text input').click()
    submit_me_field = page.locator('#id_text_string')
    submit_me_field.fill('Hello world')
    submit_me_field.press('Enter')


def test_catch_request(page: Page):
    sleep(3)
    page.goto('https://www.airbnb.ru/')
    # with page.expect_response(re.compile('autosuggestions'))
    with page.expect_response('**/autosuggestions**') as response_event:
         page.get_by_test_id('header-tab-search-block-tab-EXPERIENCES').click()

    response = response_event.value
    print(response.url)
    print(response.status)
    response_data = response.json()
    assert response_data['show_nearby'] is False


def test_pogoda(page: Page):

    def handle_route(route: Route):
        response = route.fetch()
        body = response.json()
        body['temperature'] = '+32'
        body['icon'] = 'A6'
        body = json.dumps(body)
        route.fulfill(
            response=response,
            body=body
        )

    def handle_route2(route: Route):
        url = route.request.url
        url = url.replace('api/', '')
        route.continue_(url=url)
    sleep(3)
    page.route('**/pogoda/**', handle_route2)
    page.goto('https://www.onliner.by/')
    page.locator('[name="query"]').click()
    sleep(16)


def test_api(page: Page):
    response = page.request.get('https://jsonplaceholder.typicode.com/posts/42')
    print(response.json(), response.status)
    assert response.json()['id'] == 42
    