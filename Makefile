.DEFAULT_GOAL := all

.PHONY: .uv
.uv:
	@uv -V || echo 'Please install uv: https://docs.astral.sh/uv/getting-started/installation/'

.PHONY: install
install: .uv
	uv sync --frozen --all-groups

.PHONY: docs
docs:
	@./scripts/scrape-ine-docs.sh

.PHONY: clean
clean:
	rm -rf dataset
	rm -rf *.spec
