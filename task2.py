# Часть 2: Автоматизация тестирования
# Работа с Selenium или Playwright
# • Выберите любую из указанных библиотек (Selenium или Playwright).
# • Напишите скрипт, который:
# • Открывает веб-страницу (например, https://example.com).
# • Проверяет, что заголовок страницы содержит слово "Example".
# • Находит элемент по CSS-селектору, содержащему текст "More information" и кликает по нему.
# • Проверяет, что по клику произошло перенаправление на страницу с URL "https://www.iana.org/help/example-domains".


from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Запуск браузера (можно выбрать 'chromium', 'firefox' или 'webkit')
    browser = p.chromium.launch(headless=False)  # headless=False, чтобы видеть браузер
    page = browser.new_page()

    # 1. Открываем веб-страницу
    page.goto("https://example.com")

    # 2. Проверяем, что заголовок содержит "Example"
    assert "Example" in page.title()
    print("✅ Заголовок содержит 'Example'")

    # 3. Кликаем по ссылке с текстом "More information"
    page.click('a:has-text("More information")')

    # 4. Проверяем URL
    page.wait_for_url("https://www.iana.org/help/example-domains")
    assert page.url == "https://www.iana.org/help/example-domains"
    print("✅ Успешный переход на нужный URL")

    browser.close()



