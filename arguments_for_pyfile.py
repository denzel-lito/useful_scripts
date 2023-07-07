import argparse
parser = argparse.ArgumentParser()

## Required parameters
parser.add_argument("--data_dir",
                    default=None,
                    type=str,
                    required=True,
                    help="The input data dir. Should contain the .tsv files (or other data files) for the task.")
parser.add_argument("--print",
                    action='store_true',
                    help="Flag of process printing")
args = parser.parse_args()

if args.print:
    print(args.data_dir)

