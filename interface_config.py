# Interface Config Parser using Python OOPs
# Supports: print(cfg)  →  interface eth0 speed=1000 duplex=full mtu=1500
#           cfg["mtu"]  →  1500

class InterfaceConfig:
    """
    Parses an interface config string and behaves like a dict.
    
    Usage:
        cfg = InterfaceConfig("interface eth0 speed=1000 duplex=full mtu=1500")
        print(cfg)          → interface eth0 speed=1000 duplex=full mtu=1500
        cfg["mtu"]          → 1500
        cfg["speed"]        → 1000
    """

    def __init__(self, config_string):
        self._raw = config_string           # private - original string
        self._interface_name = None         # protected
        self._params = {}                   # protected - parsed key=value pairs
        self.__parse(config_string)         # private method

    # ── Private: parse the config string ──────────────────────
    def __parse(self, config_string):
        tokens = config_string.strip().split()

        # first token is always "interface", second is the name
        if tokens[0].lower() == "interface":
            self._interface_name = tokens[1]
            tokens = tokens[2:]             # remaining are key=value pairs

        for token in tokens:
            if "=" in token:
                key, value = token.split("=", 1) # split only on first '='
                # auto-convert numeric values to int
                self._params[key] = int(value) if value.isdigit() else value

    # ── @property ──────────────────────────────────────────────
    @property
    def interface_name(self):
        return self._interface_name

    @property
    def params(self):
        return dict(self._params)           # return a copy

    # ── Dict-like access: cfg["mtu"] ───────────────────────────
    def __getitem__(self, key):
        if key not in self._params:
            raise KeyError(f"'{key}' not found in interface config")
        return self._params[key]

    def __setitem__(self, key, value):
        self._params[key] = value

    def __delitem__(self, key):
        if key not in self._params:
            raise KeyError(f"'{key}' not found")
        del self._params[key]

    def __contains__(self, key):
        """Supports: 'mtu' in cfg"""
        return key in self._params

    # ── print(cfg) ─────────────────────────────────────────────
    def __str__(self):
        params_str = " ".join(f"{k}={v}" for k, v in self._params.items())
        return f"interface {self._interface_name} {params_str}"

    def __repr__(self):
        return f"InterfaceConfig('{self.__str__()}')"

    # ── Extra utility methods ──────────────────────────────────
    def get(self, key, default=None):
        """Safe get with default, like dict.get()"""
        return self._params.get(key, default)

    def keys(self):
        return self._params.keys()

    def values(self):
        return self._params.values()

    def items(self):
        return self._params.items()

    def update(self, **kwargs):
        """Update or add parameters."""
        self._params.update(kwargs)

    @staticmethod
    def from_dict(interface_name, **kwargs):
        """Create InterfaceConfig from keyword arguments instead of a string."""
        params_str = " ".join(f"{k}={v}" for k, v in kwargs.items())
        return InterfaceConfig(f"interface {interface_name} {params_str}")


# ─────────────────────────────────────────────────────────────
# Demo
# ─────────────────────────────────────────────────────────────
if __name__ == "__main__":

    # Create from config string
    cfg = InterfaceConfig("interface eth0 speed=1000 duplex=full mtu=1500")

    print("── print(cfg) ──────────────────────────────")
    print(cfg)

    print("\n── Dict-like access ────────────────────────")
    print(f'cfg["mtu"]    → {cfg["mtu"]}')
    print(f'cfg["speed"]  → {cfg["speed"]}')
    print(f'cfg["duplex"] → {cfg["duplex"]}')

    print("\n── .get() with default ─────────────────────")
    print(f'cfg.get("mtu")          → {cfg.get("mtu")}')
    print(f'cfg.get("vlan", "N/A")  → {cfg.get("vlan", "N/A")}')

    print("\n── 'in' operator ───────────────────────────")
    print(f'"mtu" in cfg    → {"mtu" in cfg}')
    print(f'"vlan" in cfg   → {"vlan" in cfg}')

    print("\n── Update a value ──────────────────────────")
    cfg["mtu"] = 9000
    print(f'After cfg["mtu"] = 9000 → {cfg}')

    print("\n── Add a new param ─────────────────────────")
    cfg["vlan"] = 100
    print(f'After cfg["vlan"] = 100 → {cfg}')

    print("\n── .keys() / .values() / .items() ─────────")
    print(f"keys()   → {list(cfg.keys())}")
    print(f"values() → {list(cfg.values())}")
    print(f"items()  → {list(cfg.items())}")

    print("\n── interface_name property ─────────────────")
    print(f"cfg.interface_name → {cfg.interface_name}")

    print("\n── Create from dict (static method) ────────")
    cfg2 = InterfaceConfig.from_dict("gi0/0", speed=10000, duplex="full", mtu=9000)
    print(cfg2)
    print(f'cfg2["speed"] → {cfg2["speed"]}')

    print("\n── repr() ──────────────────────────────────")
    print(repr(cfg))
