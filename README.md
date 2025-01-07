# meowspeak

`meowspeak` is a fun Python package that lets you display messages "spoken" by ASCII art cats. Whether you're sending a simple message or just want to add a bit of whimsy to your terminal output, `meowspeak` lets you do so in style!

## Installation

To install `meowspeak`, use `pip`:

```bash
pip install meowspeak
```

## Usage

Once installed, you can use the `meowspeak` command directly in your terminal. Here's how you can use it:

### Display a message with a random cat:

```bash
meowspeak "Hello, world!"
```

This will display the message `"Hello, world!"` in a speech bubble coming from a random ASCII cat.

### Choose a specific cat:

To use a specific cat, use the `--cat` option followed by the cat's index:

```bash
meowspeak "This is a cool cat!" --cat 1
```

### List all available cats:

To view all available cats and their indices, use the `--list` option:

```bash
meowspeak --list
```

### Customize the message width:

You can customize the width of the speech bubble using the `--width` option. For example:

```bash
meowspeak "This is a really long message that needs wrapping" --width 30
```

## Example Output

```bash
 ________
< Hello! >
 --------
       /\_/\
      ( o.o )
       > ^ <
```

## Contributing

Feel free to fork the repository and submit issues or pull requests. Contributions are always welcome!

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.
