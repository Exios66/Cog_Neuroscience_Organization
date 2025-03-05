# Documentation

This directory contains comprehensive documentation for all resources in the Cognitive Neuroscience Organization repository.

## Documentation Structure

- **Guides**: Step-by-step instructions for common tasks and workflows
- **API**: Technical documentation for software tools and libraries
- **Templates**: Standardized templates for various document types
- **Standards**: Coding standards, data formats, and best practices
- **Tutorials**: In-depth tutorials for specific techniques and methods

## Documentation Format

Our documentation follows a consistent format using Markdown for maximum compatibility and ease of maintenance. We use:

- Clear headings and subheadings
- Code blocks with syntax highlighting
- Tables for structured information
- Images and diagrams where appropriate
- Cross-references to related documentation

## Contributing to Documentation

We welcome contributions to improve our documentation. Please see our [documentation contribution guidelines](guides/documentation_guidelines.md) for more information on how to help.

## Building Documentation

For local rendering of documentation, we use [MkDocs](https://www.mkdocs.org/) with the [Material theme](https://squidfunk.github.io/mkdocs-material/):

```bash
# Install MkDocs and the Material theme
pip install mkdocs mkdocs-material

# Build and serve documentation locally
mkdocs serve
```

The documentation will be available at `http://localhost:8000/`.
