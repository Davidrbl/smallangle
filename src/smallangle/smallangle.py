import click
import numpy as np
from numpy import pi
import pandas as pd

@click.group()
def cmd_group():
    pass

@cmd_group.command()
@click.option(
    "-n",
    "--number",
    default=10,
    help="Ammount of values displayed",
    show_default=True
)
def sin(number):
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)

@cmd_group.command()
@click.option(
    "-n",
    "--number",
    default=10,
    help="Ammount of values displayed",
    show_default=True
)
def tan(number):
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)

if __name__ == "__main__":
    sin()