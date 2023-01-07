# Заготовка под видеоплеер
в файле `index.html` минимальная жизнеспособная версия видеоплеера с кнопками start/pause, mute/unmute, fullscreen.

## Для разработчиков
Иконки взяты из пакета font-awesome 4.7.0.  
Для простоты работы используется библиотека `livereload`.  
Для модернизации плеера установите зависимости и запустите скрипт `server.py`:
```sh
pip3 install -r requirements.txt && python3 server.py
```
он будет определять сохранения файла `index.html` и автоматически перезагружать страницу

## [DEMO - версия](https://ilyashirko.github.io/video_player/)