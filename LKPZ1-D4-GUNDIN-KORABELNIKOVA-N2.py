import requests
from bs4 import BeautifulSoup

def search_wikipedia(query):
    url = f"https://ru.wikipedia.org/wiki/{query.replace(' ', '_')}"
    response = requests.get(url)
    if response.status_code != 200:
        print("Статья не найдена.")
        return None
    return response

def print_paragraphs(soup):
    paragraphs = soup.find_all("p")
    for i, paragraph in enumerate(paragraphs, 1):
        print(f"Параграф {i}:\n{paragraph.text.strip()}\n")
        next_action = input("Нажмите Enter, чтобы продолжить, или введите 'exit' для выхода: ").strip()
        if next_action.lower() == "exit":
            break

def get_related_articles(soup):
    links = soup.find_all("a", href=True)
    articles = [(link.text.strip(), link['href']) for link in links if link['href'].startswith('/wiki/') and ':' not in link['href']]
    return articles[:5]

def wikipedia_console():
    initial_query = input("Введите запрос для поиска в Википедии: ").strip()
    response = search_wikipedia(initial_query)
    if not response:
        return

    soup = BeautifulSoup(response.content, "html.parser")
    while True:
        print("\nЧто вы хотите сделать?")
        print("1. Листать параграфы текущей статьи.")
        print("2. Перейти на одну из связанных страниц.")
        print("3. Выйти из программы.")
        choice = input("Введите номер действия: ").strip()

        if choice == "1":
            print_paragraphs(soup)
        elif choice == "2":
            related_articles = get_related_articles(soup)
            if not related_articles:
                print("Связанных статей не найдено.")
                continue
            print("\nСвязанные статьи:")
            for i, (title, link) in enumerate(related_articles, 1):
                print(f"{i}. {title} - https://ru.wikipedia.org{link}")

            article_choice = input("Введите номер статьи для перехода: ").strip()
            if article_choice.isdigit() and 1 <= int(article_choice) <= len(related_articles):
                response = search_wikipedia(related_articles[int(article_choice)-1][0])
                if response:
                    soup = BeautifulSoup(response.content, "html.parser")
            else:
                print("Неверный выбор.")
        elif choice == "3":
            print("Выход из программы.")
            break
        else:
            print("Неверный ввод. Попробуйте снова.")

if __name__ == "__main__":
    wikipedia_console()
