import csv

servidores_dns = []
with open('dns-br.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=';')
	next(csv_reader, None)  # pula os cabeçalhos
	for row in csv_reader:
		servidor_dns = dict()
		servidor_dns['ip'] = row[0]
		servidor_dns['nome'] = row[1]
		servidores_dns.append(servidor_dns)

# Algoritmo de busca 1 - Busca sequencial iterativa

# All ocurrences
def sequential_search(name, iterable):
    """ Return the IP addresse(s) of a server if it is on the CSV file.
        Args:
            name (str): The nameserver, eg: 'Century Telecom Ltda'.
            iterable: The dictionary with the IPs and Names.
        Returns:
            Return a list with the matching IP addresse(s) of the nameserver
            or -1 if its not in the iterable.
    """
    found_ips = []
    number_of_ips = len(iterable)
    for _ in range(number_of_ips):
        if name in iterable[_]['nome']:
            found_ips.append(iterable[_]['ip'])
    return found_ips if len(found_ips) >= 1 else -1

print(sequential_search('AMAZON', servidores_dns))

# Algoritmo de busca 2 - Busca binária recursiva

# Sorts the list based on the dicts key 'nome'.
servidores_dns.sort(key=lambda dictionary: dictionary['nome'])

# Only the first occurrence
def recursive_binary_search(name, iterable, first=0, last=None):
    """ Return the IP address of a server if it is on the CSV file.
        Args:
            name (str): The nameserver, eg: 'Century Telecom Ltda'.
            iterable: The dictionary with the IPs and Names.
            first (int): The first index of the iterable.
            last (None): The last index of the iterable.
        Returns:
            Return the matching IP address of the nameserver or -1 if its not in the iterable.
    """
    if not last:
        last = len(iterable) - 1
    middle = (first + last) // 2
    if name in iterable[middle]['nome']:
        return iterable[middle]['ip']
    if middle == 0 or first == last:
        return - 1
    if name < iterable[middle]['nome']:
        return recursive_binary_search(name, iterable, first, middle)
    else:
        return recursive_binary_search(name, iterable, middle + 1, last)

print(recursive_binary_search('AMAZON', servidores_dns))


# Algoritmo de busca 3 - Busca sequencial recursiva
# All ocurrences
def recursive_sequential_search(name, iterable, i=0, found_ips=[]):
    """ Return the IP addresse(s) of a server if it is on the CSV file.
        Args:
            name (str): The nameserver, eg: 'Century Telecom Ltda'.
            iterable: The dictionary with the IPs and Names.
            i (int): Variable iterator
        Returns:
            Return a list with the matching IP addresse(s) of the nameserver
            or -1 if its not in the iterable.
    """
    if i >= len(iterable):
        return found_ips if len(found_ips) >= 1 else -1
    if name in iterable[i]['nome']:
        found_ips.append(iterable[i]['ip'])
    return recursive_sequential_search(name, iterable, i+1, found_ips)

print(recursive_sequential_search('AMAZON', servidores_dns))
