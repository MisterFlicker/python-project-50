install: # создание или обновление виртуального окружения
	poetry install

build: # выполнение сборки пакета
	poetry build

publish: # отладка публикации
	poetry publish --dry-run

package-install-f: # установка пакета в систему (по факту переустановка)
	pip install --user --force-reinstall dist/*.whl

package-install: # установка пакета в систему
	python3 -m pip install --user dist/*.whl

lint: # проверка gendiff по линтеру flake8
	poetry run flake8 gendiff

test: # проверка gendiff по pytest
	poetry run pytest

test-coverage: # проверка по покрытию теста
	poetry run pytest --cov=gendiff --cov-report xml tests/


