# ghgrab - grab anything you want

Ever found a single file or folder in a massive GitHub repo and wished you could just *grab it* without cloning the whole thing? That's exactly why **ghgrab** exists. 

It's a simple, pretty terminal tool that lets you pick what you need and download it instantly. No clutter, no `git clone` waiting times, just the stuff you want.

---

## Why use ghgrab?

- **No more clone-and-delete**: Grab exactly what you need, when you need it.
- **Easy on the eyes**: A clean terminal interface that makes browsing feel smooth.
- **Works where you are**: Installs quickly via NPM, Cargo, or PIP.
- **Find things fast**: Quickly search and navigate through any repo's folders.
- **Handles the big stuff**: Built-in support for GitHub LFS (Large File Storage).
- **Batch mode**: Select a bunch of files and folders to download them all at once.

---

## Installation

### NPM
```bash
npm install -g @ghgrab/ghgrab
```

### Cargo
```bash
cargo install ghgrab
```

### pipx (Recommended for Python)
```bash
pipx install ghgrab
```

---

### Quick Start

Just type `ghgrab` to start browsing:

```bash
ghgrab
```

Or, if you already have a link, just paste it in:

```bash
ghgrab https://github.com/rust-lang/rust
```

### Keyboard Shortcuts (How to move around)

We've kept it pretty standard, but here's a quick cheat sheet:

| Key | Action |
|-----|--------|
| `Enter` / `l` / `Right` | Enter directory or Submit URL |
| `Backspace` / `h` / `Left` | Go back to previous folder or Input screen |
| `Space` | Toggle selection for the current item |
| `a` | Select All items |
| `u` | Unselect all items |
| `d` / `D` | Download selected items |
| `i` | Toggle Icons (Emoji / ASCII) |
| `q` / `Q` | Exit application |
| `g` / `Home` | Jump to Top |
| `G` / `End` | Jump to Bottom |
| `Esc` | Clear input or Cancel search |

---



## Join the community

If you find a bug, have an idea for a cool new feature, or just want to help out, we'd love to hear from you! Check out our [Contributing Guide](CONTRIBUTING.md) to see how you can get involved.

## License

Distributed under the MIT License. It's open, free, and yours to play with. See [LICENSE](LICENSE) for the fine print.

