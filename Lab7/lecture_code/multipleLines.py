# multipleLine strings
#
# three " or ' starts and stops a multiple line string
#
#
# for example:
#
text = """
This is line 1
    This is line 2, indented

Line 4, with a blank line in between. And a unicode char: \u26F9
"""

# OK now print out the srting:
print(text)

# another example using formatted placeholders
#
# review of placeholders:
# %w.df  is for float values. w & d are numbers, and means print this in a total width of w
#       with 2 places after the decimal. If the size is actually larger than w
#       it will expand the width to fit.
# %wd prints an int in a width of w
# %ws is to print a string in a with of w
#
# examples all use a width of 0 so the output width is exapnded to exactly the size needed
#
name = "Fred"
deductions = 2
gross = 1303.78
taxes = 295.01
net = 1008.77
print(
    """
      Name: %0s
Deductions: %0d
 Gross pay: $%0.2f
     Taxes: $%0.2f
   Net Pay: $%0.2f
"""
    % (name, deductions, gross, taxes, net)
)
#
# so, here is the template:
# print('''
#     <put multiple lines here, with placeholders or not>
# ''' % (put a list of values, one for each placeholder, inside parentheses with commas) ) <- this closes the print statement
#
# changing all widths to 10
#
print(
    """
      Name: %10s
Deductions: %10d
 Gross pay: $%10.2f
     Taxes: $%10.2f
   Net Pay: $%10.2f
"""
    % (name, deductions, gross, taxes, net)
)
