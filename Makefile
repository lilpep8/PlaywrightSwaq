.PHONY: test

# Переменная TEST по умолчанию пустая (запустит все тесты)
TEST ?=

test:
	PYTHONPATH=. pytest $(TEST)