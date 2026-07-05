@echo off
cd /d "%~dp0"
echo Installation de PyInstaller...
pip install pyinstaller
echo Creation de l'executable...
pyinstaller --onefile --windowed --name GestionBibliotheque interface_bibliotheque.py
echo.
echo Termine. Votre executable est dans le dossier dist\GestionBibliotheque.exe
pause
