install: # создание или обновление виртуального окружения
	poetry install

build: # выполнение сборки пакета
	poetry build

publish: # отладка публикации
	poetry publish --dry-run

package-install: # установка пакета в систему
	pip install --user --force-reinstall dist/*.whl

lint: # проверка brain_games по линтеру flake8
	poetry run flake8 gendiff
