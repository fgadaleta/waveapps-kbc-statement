# What is this?

KBC bank is not supported by Waveapps. This script lets you import statements from your KBC account to Waveapps and 
manage your finances as if your KBC bank were supported.

# Usage:

Download statements from KBC touch (http://kbctouch.kbc.be/) as csv file

Run the script to transform the original list of statements in something that Waveapps can understand and 
parse correctly

``` python kbc_to_wave.py -i export12345678.csv -o export12345678_wave.csv ```

Now you can `Upload a Bank Statement` from your Waveapps dashboard using file `export12345678_wave.csv`


