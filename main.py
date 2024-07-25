import asyncio
import random
import nodriver as uc
import logging

logging.basicConfig(level=logging.INFO)


async def get_html_content(url):
    config = uc.Config()
    config.headless = False
    config.browser_args.extend([
        '--disable-blink-features=AutomationControlled',
        '--disable-extensions',
        '--no_sandbox=True',
        '--disable-infobars',
        '--disable-gpu'
    ])

    browser = None
    try:
        browser = await uc.start(config=config)
        if not browser:
            logging.error("Failed to start browser")
            return None

        page = await browser.get(url)

        await asyncio.sleep(random.uniform(2, 5))
        await page.scroll_down(random.randint(100, 300))
        await asyncio.sleep(random.uniform(1, 3))

        content = await page.get_content()
        return content[:1000]
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return None
    finally:
        if browser:
            try:
                await browser.stop()
            except Exception as e:
                logging.error(f"Error stopping browser: {e}")


async def main():
    content = await get_html_content("https://www.olx.kz/list/q-%D1%81%D0%BF%D0%B0%D0%BD%D1%87-%D0%B1%D0%BE%D0%B1/#368934842")
    if content:
        print(f"Первые 1000 символов HTML:\n{content}")
    else:
        print("Не удалось получить содержимое страницы.")


if __name__ == "__main__":
    asyncio.run(main())