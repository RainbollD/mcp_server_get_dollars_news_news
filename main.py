from flask import Flask, jsonify
import requests
import feedparser

server = Flask(__name__)


# Получение курса доллара
def get_rate():
    data = requests.get('https://api.exchangerate-api.com/v4/latest/USD').json()
    return f"Курс доллара - {data['rates']['RUB']} руб."


# Получение температуры в городе
def get_weather(city):
    url = f"https://wttr.in/{city}?format=3"
    response = requests.get(url)
    return f"{city} weathe {response.text.split()[-1]}"


# Получение новостей
def get_news():
    url = 'https://news.ycombinator.com/rss'
    feed = feedparser.parse(url)
    news = []
    for entry in feed.entries:
        news.append({
            "Заголовок": entry.title,
            "Ссылка": entry.link,
            "Описание": entry.summary
        })
    return news


# Возвращает текущий курс доллара в формате JSON
@server.route('/rate', methods=['GET'])
def rate():
    rate_ = get_rate()
    return jsonify({'rate': rate_})


# Возвращает погоду в формате JSON
@server.route('/weather/<city>', methods=['GET'])
def weather(city):
    weather_ = get_weather(city)
    return jsonify(weather_)


# Возвращает новости в формате JSON
@server.route('/news', methods=['GET'])
def news():
    news_ = get_news()
    return jsonify(news_)


if __name__ == '__main__':
    server.run(debug=True)
