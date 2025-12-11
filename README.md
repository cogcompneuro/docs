# CCN Documentation

Public processes and policies for the [Conference on Cognitive Computational
Neuroscience](ccneuro.org).

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
uv run zensical serve
```

The site will be available at `http://127.0.0.1:8000/docs/`.

### Quality checks

Before committing, run pre-commit hooks to format and lint markdown files:

```sh
uvx prek
```

### Spell checking

To check spelling locally:

```sh
# Install aspell (one-time setup)
# macOS:
brew install aspell
# Linux:
sudo apt-get install aspell aspell-en

# Run spellcheck on specific files
.github/bin/spellcheck.sh path/to/file.md

# Or check all markdown files
.github/bin/spellcheck.sh
```

If you encounter words that are spelled correctly but flagged as misspellings, add them
to `.github/config/wordlist.txt` (one word per line, sorted alphabetically).
