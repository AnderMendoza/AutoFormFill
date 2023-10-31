![logo](./src/logo.png)

# AutoFormFills

[English](https://translate.google.com/?hl=es&sl=es&tl=en&text=readme%20en%20ingles&op=translate) · [Spanish](https://translate.google.com/?hl=es&sl=es&tl=en&text=readme%20en%20ingles&op=translate)

AutoFormFill is a tool that automates the process of filling out Google forms. This app was designed to save you time from repeatedly filling out similar or identical forms. The tool automatically fills **screening questions** on Google forms randomly.

![demo](./src/demo.gif)

## How was created

This project was developed using [Python](https://www.python.org/) and [Selenium](https://selenium-python.readthedocs.io/), a web automation library. The program interacts with the web browser to select random answers to screening questions.

## Previous requirements

Before running this tool, you must have [Python](https://www.python.org/downloads/) installed on your system. Also, make sure the Selenium driver for your browser is configured correctly. In this case, the Chrome driver has been used.

## How to Run

1. Clone this repository to your local system:

```
git clone https://github.com/tuusuario/AutoFormFill.git
```

2. Navigate to the repository folder:

```
cd AutoFormFill
```

3. Install the dependencies:

```
pip install -r requirements.txt
```

4. Edit the index.py file with the parameters that fit your form.

###

5. Run the program:

```
python auto_form_fill.py
```

Follow the instructions provided by the program to fill out a Google form automatically.

## Contributions

If you want to contribute to this project, please open an issue or a pull request.
