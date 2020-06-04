# 1
import print_models

unprinted_designs = ['curve', 'straight', 'zigzag']
completed_models = []
print_models.print_models(unprinted_designs, completed_models)
print_models.show_completed_models(completed_models)

# 2
from print_models import print_models, show_completed_models

unprinted_designs = ['curve', 'straight', 'zigzag']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# 3
from print_models import print_models as pm, show_completed_models as swm

unprinted_designs = ['curve', 'straight', 'zigzag']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# 4 
import print_models as pm

unprinted_designs = ['curve', 'straight', 'zigzag']
completed_models = []
pm.print_models(unprinted_designs, completed_models)
pm.show_completed_models(completed_models)

# 5 
from print_models import *

unprinted_designs = ['curve', 'straight', 'zigzag']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
