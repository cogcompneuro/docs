#!/bin/bash

# Declare an array to hold the source files
declare -a sources

if [[ -z "$@" ]]; then
    # If no arguments are provided, find all *.md files.
    echo "No files specified, finding all *.md files..."
    while IFS= read -r -d '' file; do
        sources+=("$file")
    done < <(find . -name '*.md' -not -path './.venv/*' -not -path './site/*' -print0)
else
    # If arguments are provided, use them as the source list
    echo "Using provided file list..."
    sources=("$@")
fi

# Check if the array is empty
if [ ${#sources[@]} -eq 0 ]; then
    echo "No files to spellcheck"
else
    # We must build an argument list where *each* file is
    # prefixed with -S, as pyspelling expects: -S file1 -S file2 ...
    declare -a spell_args
    for file in "${sources[@]}"; do
        spell_args+=("-S" "$file")
    done

    # Execute the target command.
    # "${spell_args[@]}" expands the array into the full list of arguments.
    echo "Running spellcheck on ${#sources[@]} file(s)..."
    uvx pyspelling -c .github/config/spellcheck.yaml --name Markdown "${spell_args[@]}"
fi
