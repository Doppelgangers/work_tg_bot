import re


def check_domain_name(domain: str) -> bool:
    # Регулярное выражение для проверки доменного имени.
    regex = r"(?!-)[A-Za-z0-9-]{1,63}(?<!-)\.[A-Za-z]{2,6}"
    match = re.fullmatch(regex, domain)
    print(domain, bool(match))
    return bool(match)


def check_ip_address(ip_address: str) -> bool:
    try:
        host_bytes = ip_address.split('.')
        valid = [int(b) for b in host_bytes]
        valid = [b for b in valid if b >= 0 and b<=255]
        return len(host_bytes) == 4 and len(valid) == 4
    except:
        return False