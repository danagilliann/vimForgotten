class bcolors:
	HEADER = '\033[95m'
	OKGREEN = '\033[92m'
	ENDC = '\033[0m'

g = bcolors.OKGREEN
e = bcolors.ENDC

vim = {
        "Get name of current file": "echo @%",
        "Remove blank lines": ":g/^$/d",
        "Delete set of lines": ":a,bd [a,b]\n\t:,bd [current,b]",
        "Grep faster": ":Ag -i <keyword> <optional: location>",
}

for k,v in vim.iteritems():
    print k + '\n\t' + g + v + e
