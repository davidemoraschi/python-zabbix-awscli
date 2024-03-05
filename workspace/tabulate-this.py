import tabulate

print(tabulate.tabulate([['Alice', 24], ['Bob', 19]], headers=['Name', 'Age'], tablefmt='html', showindex=False))
