def print_only(param, arg1):
    print(param.format(arg1))

print_only("Hello, {}!", "world")
print_only("H" + "ello, worl{}", "d!")
hello = "Hello"
world = "world"
print_only(f"{hello}, {{}}", world + '!')
print_only(hello + ", " + "{}", "world{}".format('!'))
print_only('h' + '{}', '{}'.format('{}').format('i'))
print_only("Hel" + 'lo, ' + 'wor{}!'.format('l{}').format('{}'), '' + 'd' + '')
print_only('good {}', 'job')
end = '!'
print_only(hello + ', ' + world + '{}', end)
print_only(hello + '{}'.format(end), world)
print_only(world + '{}'.format(', {}'), end)