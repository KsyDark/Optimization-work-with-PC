::������� ����� �ணࠬ��
taskkill /f /im Untitled.exe
:: ����᪠�� �������� �஥�� � ������� pyinstaller
:: �।���⥫쭮 ��⠭���� ����஢�� - ��ਫ�� OEM 866
pyinstaller --onefile --icon=�.�.��.ico Untitled.py
:: ����᪠�� �ணࠬ�� ��᫥ �������樨
cd dist
start "��⨬�����" "Untitled.exe"