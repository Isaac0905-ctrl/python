from __future__ import annotations


class Host:
    IPV4_BITS = 32

    def __init__(self, *ip_octets: int, mask: int):
        self.ip_octest = ip_octets
        self.mask = mask
        num_octest = [num for num in self.ip_octest]
        if len(num_octest) < 4 or len(num_octest) > 4:
            raise IPAddressError('IP address is invalid: Only 4 octets are allowed')
        for number in num_octest:
            number = int(number)
            if number < 0 or number > 255:
                raise IPAddressError('IP address is invalid: Octet is out of range')
        if int(self.mask) < 0 or int(self.mask) > 32:
            raise IPAddressError('IP address is invalid: Mask is out of range')

    @classmethod
    def build_from_sip(cls, sip: str, *, mask: int) -> Host: ...

    @property
    def ip(self) -> str:
        return '.'.join(str(octet) for octet in self.ip_octest)

    @property
    def bip(self) -> str:
        bin_host = []
        for num_ip in self.ip_octest:
            num_ip = bin(num_ip)
            num_ip = num_ip[2:]
            if len(num_ip) < 8:
                add_zeros = 8 - len(num_ip)
                num_ip = (add_zeros * '0') + num_ip
                bin_host.append(num_ip)
            else:
                bin_host.append(num_ip)
        return ''.join(num for num in bin_host)

    @property
    def addr_bmask(self) -> str:
        return self.bip

    @property
    def addr_bhost(self) -> str: ...

    @property
    def has_network_addr(self) -> bool: ...

    @property
    def has_broadcast_addr(self) -> bool: ...

    @property
    def nclass(self) -> str | None: ...

    @property
    def addr_host_size(self) -> int: ...

    @property
    def num_hosts(self) -> int: ...

    def ping(self, host: Host) -> bool: ...

    def __repr__(self): ...

    @classmethod
    def build_from_bip(cls, bip: str, mask: int) -> Host:
        IPV4_SLICES = list(range(0, cls.IPV4_BITS + 1, 8))
        ...

    def __iter__(self): ...

    def __add__(self, other: Host) -> Host: ...


class IPAddressError(Exception):
    def __init__(self, message: str = ''): ...
