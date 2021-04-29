import re
import sys
from argparse import ArgumentParser


def main(content, num=3):
	result = set()
	for line in content:
		for match in re.finditer('(\.[\w-]+){'+str(num)+'}$', line):
			result.add(match.group(0).split('.', 1)[1])
	return result

def executor(result):
	for line in result:
		print(line)

pr = ArgumentParser()
pr.add_argument("-count", "-c", help="Filter Subdomains Based On Level.")
pr.add_argument("-file", "-f", help="File That Contain Subdomains.")
option = pr.parse_args()

if option.file and option.count and sys.stdin.isatty():
	result = main([domain.strip() for domain in open(option.file).readlines()], option.count)
	executor(result)
elif option.count and not sys.stdin.isatty() and not option.file:
	result = main([domain.strip() for domain in sys.stdin.readlines()], option.count)
	executor(result)
elif option.file and not option.count and sys.stdin.isatty():
	result = main([domain.strip() for domain in open(option.file).readlines()])
	executor(result)
elif not sys.stdin.isatty() and not option.file and not option.count:
	result = main([domain.strip() for domain in sys.stdin.readlines()])
	executor(result)
else:
	pr.print_help()
