# CCN Documentation

Public processes and policies for the
[Conference on Cognitive Computational Neuroscience](https://ccneuro.org).

## Local development

### Prerequisites

Install `uv` if you haven't already:

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

For other installation methods, see the
[`uv` documentation](https://docs.astral.sh/uv/getting-started/installation/).

### Serving

To serve the documentation locally:

```sh
# TODO: revert to `uvx zensical serve` once https://github.com/zensical/backlog/issues/16 is resolved
uvx --with ./zen_macros_ext zensical serve
```

The site will be available at `http://127.0.0.1:8000/docs/`.

### Quality checks

Before committing, run pre-commit hooks to format, lint, and spell-check markdown files:

```sh
# Install aspell (one-time setup)
# macOS:
brew install aspell
# Linux:
sudo apt-get install aspell aspell-en

# Run all hooks
uvx prek
```

If you encounter words that are spelled correctly but flagged as misspellings, add them
to `wordlist.txt` (one word per line, sorted alphabetically).
