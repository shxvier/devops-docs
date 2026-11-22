# devops-docs

Практика 9. Исходники сайта находятся в `docs/`, конфигурация сборки в
`mkdocs.yml`. `quality.yml` проверяет код и документацию, `pages.yml`
публикует собранный каталог. `site/` создаётся при сборке и игнорируется Git.

```bash
python -m pip install -r requirements-dev.txt
python -m pylint src/status.py --score=no
mkdocs build --strict
```
