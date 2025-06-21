# PlaywrightSwaq

## Установка
1. Клонировать репозиторий
   ```bash
   git clone https://github.com/lilpep8/PlaywrightSwaq
   ```

2. Создать виртуальное окружение:
   ```bash
   python -m venv .venv
   ```
   ```bash
   source .venv/bin/activate  # ОС Linux/Mac
   ```
   ```bash
   .venv\Scripts\activate    # ОС Windows
   ```
   
3. Установить зависимости
   ```bash
   pip install -r requirements.txt
   ```
4. Вставить в файл .env-copy свой username и password
   ```bash
   API_USERNAME=your_username
   API_PASSWORD=your_password
   ```
5. Установить Make (если нужно)

   ```bash
   sudo apt update && sudo apt install make -y # Ubuntu/Debian
   ```
      ```bash
   xcode-select --install # macOS
   ```
   Установи для Windows ([GnuWin Make]())


6. Запустить тесты
   ```bash
   make test
   ```

<!-- Скрытая ссылка на GnuWin Make -->
[gnuwin]: https://gnuwin32.sourceforge.net/packages/make.htm
