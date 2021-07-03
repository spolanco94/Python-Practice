# Add the functions for the example code 'printing_models.py' into a separate
# file called 'printing_functions.py'. Add an import statement to the top of
# 'printing_models.py' and call the functions.
import printing_functions

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

printing_functions.print_models(unprinted_designs, completed_models)
printing_functions.show_completed_models(completed_models)
