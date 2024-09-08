import subprocess

command_str = 'ssh -p 3022 llm_arch@127.0.0.1'
command_str = 'ls -l'

command_list = command_str.split(' ')

print(command_list)
#
output = subprocess.check_output(command_list)

print(output)

