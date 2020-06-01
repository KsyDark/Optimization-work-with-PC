::Убиваем процесс программы
taskkill /f /im Untitled.exe
:: Запускает комплицию проекта с помощью pyinstaller
:: Предварительно установите кодировку - Кирилица OEM 866
pyinstaller --onefile --icon=О.Р.ПК.ico Untitled.py
:: Запускаем программу после компиляции
cd dist
start "Оптимизатор" "Untitled.exe"