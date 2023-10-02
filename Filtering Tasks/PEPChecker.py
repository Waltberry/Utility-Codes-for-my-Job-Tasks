import pycodestyle

# Create a StyleGuide instance
style_checker = pycodestyle.StyleGuide()

# Run PEP 8 check on multiple files
result = style_checker.check_files(['columns_to_2dp.py','convert_and_multiply.py'])

# Print result of PEP 8 style check
print(result.messages)
