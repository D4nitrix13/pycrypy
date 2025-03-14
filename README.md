<!-- Author: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Email: danielperezdev@proton.me -->

<!-- PYTHONPATH=src python3 src/cli/main.py --help -->

# ***pycrypy***

> *`pycrypy` is a command-line tool written in Python for easily configuring Alacritty options from the terminal. It allows you to adjust themes, fonts, font size, opacity, padding, cursor shape, and more with simple commands.*

## ***Features***

- [x] **Theme Change:** *Modify the Alacritty theme using a file path or a theme name.*
- [x] **Font Configuration:** *Change the font and font size in Alacritty.*
- [x] **Opacity Adjustment:** *Modify the terminal's opacity.*
- [x] **Padding Configuration:** *Adjust the terminal's padding.*
- [x] **Cursor Shape:** *Change the cursor shape and blinking.*

## ***Installation***

### ***Installation via PyPI***

**You can easily install `pycrypy` using `pip`:**

```bash
pip install pycrypy
```

### ***Installation from Source Code***

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/D4nitrix13/pycrypy.git --depth=1
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd pycrypy
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Install the Package:**

   ```bash
   pip install .
   ```

## ***Usage***

> *To use `pycrypy`, simply run the `pycrypy` command followed by the desired options. Here is a description of the available options:*

### ***Options***

```bash
pycrypy [-h] [-t [THEME ...]] [-P [THEMEPATH]] [-f [FONT ...]] [-F [FONTSIZE]] [-s [STYLE ...]]
      [-o OPACITY] [-p X Y] [-S [CURSORSHAPE]] [-B [CURSORBLINKING]] [-T [CURSORTHICKNESS]]
      [-R] [-D] [-L] [-v] [-V]
```

### ***-h, --help***

**Displays this help message and exits.**

```bash
usage: pycrypy [-h] [-t [THEME ...]] [-P [THEMEPATH]] [-f [FONT ...]] [-F [FONTSIZE]] [-s [STYLE ...]]
                               [-o OPACITY] [-p X Y] [-S [CURSORSHAPE]] [-B [CURSORBLINKING]] [-T [CURSORTHICKNESS]] [-R]
                               [-D] [-L] [-v] [-V]

pycrypy is a command-line tool designed to easily configure Alacritty options
from the terminal using Python.

options:
  -h, --help            show this help message and exit
  -t [THEME ...], --theme [THEME ...]
                        Changes the theme used by Alacritty
  -P [THEMEPATH], --theme-path [THEMEPATH]
                        Absolute or relative path of the theme to be applied in the Alacritty terminal
  -f [FONT ...], --font [FONT ...]
                        Changes the font used by Alacritty
  -F [FONTSIZE], --font-size [FONTSIZE]
                        Changes the font size
  -s [STYLE ...], --style [STYLE ...]
                        Changes the font style: Normal | Bold | Italic | Underline
  -o OPACITY, --opacity OPACITY
                        Changes the opacity of the Alacritty terminal
  -p X Y, --padding X Y
                        Changes the padding of the Alacritty terminal
  -S [CURSORSHAPE], --cursor-shape [CURSORSHAPE]
                        shape is an option that defines the cursor shape and can take one of these values:
                        Block | Underline | Beam
  -B [CURSORBLINKING], --cursor-blinking [CURSORBLINKING]
                        This option defines if the cursor blinks and can have one of these values: Never | Off
                        | On | Always
  -T [CURSORTHICKNESS], --cursor-thickness [CURSORTHICKNESS]
                        This option defines the cursor thickness
  -R, --theme-recommendations
                        Lists recommended themes for Alacritty
  -D, --theme-dark      Lists dark themes for Alacritty
  -L, --theme-light     Lists light themes for Alacritty
  -v, --verbose         Enable verbose mode
  -V, --version         Displays the version of the program and author details

Enjoy configuring your Alacritty with pycrypy!
```

### ***-t [THEME ...], --theme [THEME ...]***

- *Changes the theme used by Alacritty. You can specify one or more themes.*

**Example:**

```bash
pycrypy -t tokyo night
```

*This command changes the Alacritty theme to tokyo night.*

### ***-P [THEMEPATH], --theme-path [THEMEPATH]***

- *Absolute or relative path of the theme to be applied in the Alacritty terminal.*

**Example:**

```bash
pycrypy -P /home/user/.config/alacritty/themes/mytheme.toml
```

*This command applies the theme from the specified path.*

### ***-f [FONT ...], --font [FONT ...]***

- *Changes the font used by Alacritty. You can specify one or more fonts.*

**Example:**

```bash
pycrypy -f Cascadia Code NF
```

*This command changes the Alacritty font to Cascadia Code NF.*

### ***-F [FONTSIZE], --font-size [FONTSIZE]***

- *Changes the font size.*

**Example:**

```bash
pycrypy -F 14
```

*This command sets the font size to 14.*

### ***-s [STYLE ...], --style [STYLE ...]***

- *Changes the font style: Normal | Bold | Italic | Underline. You can specify one or more styles.*

**Example:**

```bash
pycrypy -s Bold Italic
```

*This command applies Bold Italic styles to the font in Alacritty.*

### ***-o OPACITY, --opacity OPACITY***

- *Changes the opacity of the Alacritty terminal.*

**Example:**

```bash
pycrypy -o 0.8
```

*This command sets the terminal opacity to 80%.*

### ***-p X Y, --padding X Y***

- *Changes the padding of the Alacritty terminal.*

**Example:**

```bash
pycrypy -p 10 15
```

*This command sets the padding to 10 pixels vertical and 15 pixels horizontal.*

### ***-S [CURSORSHAPE], --cursor-shape [CURSORSHAPE]***

- *Defines the cursor shape. It can take one of these values: Block | Underline | Beam.*

**Example:**

```bash
pycrypy -S Beam
```

*This command sets the cursor shape to Beam.*

### ***-B [CURSORBLINKING], --cursor-blinking [CURSORBLINKING]***

- *Defines whether the cursor blinks. It can have one of these values: Never | Off | On | Always.*
**Example:**

```bash
pycrypy -B Always
```

*This command sets the cursor blinking to Always.*

### ***-T [CURSORTHICKNESS], --cursor-thickness [CURSORTHICKNESS]***

- *Defines the thickness of the cursor.*
**Example:**

```bash
pycrypy -T 2
```

*This command sets the cursor thickness to 2 pixels.*

### ***-R, --theme-recommendations***

- *Lists recommended themes for Alacritty.*
**Example:**

```bash
pycrypy -R
```

*This command displays a list of recommended themes for Alacritty.*

### ***-D, --theme-dark***

- *Lists dark themes for Alacritty.*
**Example:**

```bash
pycrypy -D
```

*This command displays a list of dark themes for Alacritty.*

### ***-L, --theme-light***

- *Lists light themes for Alacritty.*
**Example:**

```bash
pycrypy -L
```

*This command displays a list of light themes for Alacritty.*

### ***-v, --verbose***

- *Enables verbose mode.*
**Example:**

```bash
pycrypy -v
```

*This command runs `pycrypy` in verbose mode, showing additional information.*

### ***-V, --version***

- *Displays the program version and author information.*
**Example:**

```bash
pycrypy -V
```

*This command shows the current version of the program and author information.*

### ***Creating an Executable with PyInstaller***

> *To convert the `src/cli/main.py` script into a standalone executable, use PyInstaller with the following options:*

**Here is the equivalent `pyinstaller` command for the configuration you provided:**

```bash
pyinstaller ./pycrypy.spec
```

```bash
pyinstaller --onefile \
            --noconfirm \
            --clean \
            --noconsole \
            --name pycrypy \
            --add-data "./src/TemasClaros:TemasClaros" \
            --add-data "./src/TemasOscuros:TemasOscuros" \
            --add-data "./src/TemasRecomendados:TemasRecomendados" \
            --add-data "./src/cli:cli" \
            --add-data "./src/config:config" \
            --add-data "./src/lib:lib" \
            ./src/cli/main.py
```

### ***Command Breakdown***

- **`--onefile`:** *Creates a single executable file.*
- **`--noconfirm`:** *Does not prompt for confirmation before overwriting files.*
- **`--clean`:** *Cleans up temporary build files.*
- **`--noconsole`:** *Does not open a console window when running the executable (for GUI applications).*
- **`--name pycrypy`:** *Defines the name of the executable file.*
- **`--add-data "src:dest"`:** *Specifies additional data files and their destinations in the executable. The syntax is `"source_path:destination_path".*
- **`src/cli/main.py`:** *The main script file.*

### ***Running the Command***

*Run the command in the terminal from the directory where your `src/cli/main.py` file is located. PyInstaller will package your application, including the specified directories and files.*

*If you need to adjust data file paths, ensure they are correct relative to the directory from which you are running the command.*

### ***Troubleshooting***

- **`objcopy` Error:** *If you encounter errors related to `objcopy`, ensure that all input files are correct and there are no file permission issues. Verify that the file specified in `--name` is not in use and that the working directory is clean.*

- **Missing Dependencies:** *If the executable fails due to missing dependencies, ensure that all required libraries are installed and accessible from the Python environment.*

### ***Contributing***

**If you want to contribute to `pycrypy`, please follow these steps:**

1. **Fork the Repository.**

2. **Create a New Branch** *for your feature or bug fix.*

3. **Make Changes** *and commit your changes.*

4. **Submit a Pull Request** *with a clear description of the changes made.*

### ***License***

> *This repository is published under the MIT License. Feel free to use, modify, and distribute the content according to the terms of this license.*

### ***Author***

- **Author:** *Daniel Benjamin Perez Morales*

- **GitHub:** *[D4nitrix13](https://github.com/D4nitrix13 "https://github.com/D4nitrix13")*

- **Email:** *`danielperezdev@proton.me`*
