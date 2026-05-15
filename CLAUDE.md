# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**csl-kale** provides a web display of scanned pages from M.R. Kale's *Higher Sanskrit Grammar* (1894). It is linked from the Sanskrit Lexicon homepage and serves as a reference for Sanskrit grammatical rules cited in CDSL dictionary entries.

Two display implementations are provided:
- **PHP version** (`disp/index.php`) — server-side, requires Apache/XAMPP
- **JavaScript version** (`disp1/index.html`) — client-side, works without a server

## Architecture

| Directory/File | Purpose |
|---|---|
| `disp/` | PHP web application: `index.php` serves scanned page images |
| `disp1/` | Pure JavaScript version: `index.html` + `main.js` serve images without a server |
| `png/` | Scanned page images of Kale Higher Sanskrit Grammar |

### URL parameter

`disp/index.php?page=N` — display the Nth page (PHP version).
`disp1/index.html#N` — display the Nth page (JS version).

## Dependencies

- **PHP** (for `disp/`) — requires Apache/XAMPP
- **JavaScript** browser (for `disp1/`) — no server needed
