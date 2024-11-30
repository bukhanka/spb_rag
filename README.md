# Я Здесь Живу (I Live Here) - Интеллектуальный Городской Помощник Санкт-Петербурга

## 🌟 Обзор
Передовой AI-ассистент для Санкт-Петербурга, использующий современные технологии искусственного интеллекта для предоставления актуальной городской информации.

## 🚀 Ключевые Технологии
- Retrieval-Augmented Generation (RAG)
- Гибридный поиск (Векторный + BM25)
- OpenAI GPT-4o Mini
- FastAPI
- Chroma DB

## 🔍 Возможности
- Расширенный поиск контактов
- Информация о городских услугах
- Образовательные справки
- Афиша и достопримечательности

## 🛠 Технический Стек
- LangChain
- OpenAI GPT-4o Mini
- Chroma DB
- FastAPI
- Pandas
- Scikit-learn
- Rank-BM25

## 📊 Сценарии
1. Гибридный поиск контактов
2. Анализ городских услуг
3. Образовательные консультации
4. Культурные рекомендации

## 🔧 Требования
- Python 3.9+
- OpenAI API Key

## 🚀 Быстрый Старт

1. Клонируйте репозиторий
```bash
git clone https://github.com/yourusername/spb-city-assistant.git
cd spb-city-assistant
```

2. Создайте виртуальное окружение
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Установите зависимости
```bash
pip install -r requirements.txt
```

4. Настройте переменные окружения
Создайте `.env`:
```
OPENAI_API_KEY=ваш_api_ключ_openai
```

## 🏃 Запуск Приложения
```bash
uvicorn src.main:app --reload
```

## 📂 Структура Проекта
- `src/`: Основной код
- `data/`: Наборы данных
- `tests/`: Тестирование и оценка
- `chroma_db/`: Векторное хранилище

## 🌐 Источники Данных
- [База Контактов СПб](data/contacts.xlsx)
- [Цифровой Петербург](https://petersburg.ru/)

## 🚧 План Развития
- Расширение гибридных техник поиска
- Интеграция дополнительных источников
- Улучшение контекстного понимания

## 🤝 Участие
1. Форкните репозиторий
2. Создайте feature-ветку
3. Закоммитьте изменения
4. Запушьте в ветку
5. Создайте Pull Request

## 📄 Лицензия
[Укажите лицензию]

## 📞 Контакты
[Ваши контактные данные]

