import xdusage_v1
import xdusage_v2
import argparse
import sys


class ArgumentParser(argparse.ArgumentParser):

    def error(self, message):
        pass
        # self.print_help(sys.stderr)
        # self.exit(2, '%s: error: %s\n' % (self.prog, message))


def remove_argument():
    av_index = None
    if '-av' in sys.argv:
        av_index = sys.argv.index('-av')
    if '--apiversion' in sys.argv:
        av_index = sys.argv.index('--apiversion')
    if av_index:
        del sys.argv[av_index:av_index + 2]


list_of_choices = ["1", "2"]
parser = ArgumentParser(add_help=False, description="Specify the specific version of xdusage. The default version is 2")
parser.add_argument("-av", "--apiversion", default="2", choices=list_of_choices)
args = parser.parse_args()

for arg in sys.argv:
    if arg == '-h' or arg == '--help':
        parser.print_help()

if args.apiversion == '1':
    remove_argument()
    xdusage_v1.main()
elif args.apiversion == '2':
    remove_argument()
    xdusage_v2.main()
