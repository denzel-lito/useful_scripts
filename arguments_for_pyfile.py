#   атрибуты для вызова py-файла
#----------------------------------
import argparse
parser = argparse.ArgumentParser()

parser.add_argument("--data_dir",
                    default=None,
                    type=str,
                    required=True,
                    help="the input data dir")
parser.add_argument("--model_type",
                    default=None,
                    choices=('text', 'voice'),
                    type=str,
                    required=True,
                    help="type of model. choose from ['text', 'voice']")
parser.add_argument("--print",
                    action='store_true',
                    help="flag of process printing")
args = parser.parse_args()

if args.print:
    print(args.data_dir)


#----------------------------------
#     переменные окружения
#----------------------------------
import os
os.environ["surface"] = "my_value"
a = os.getenv('surface')
