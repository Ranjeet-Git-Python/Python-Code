# Network Device Categorizer using Python OOPs
# Categorizes devices by vendor, model, firmware, and driver type

from abc import ABC, abstractmethod


# ─────────────────────────────────────────────────────────────
# Base Class - NetworkDevice (Abstract)
# ─────────────────────────────────────────────────────────────
class NetworkDevice(ABC):
    # Class variables
    _total_devices = 0
    _device_registry = []   # stores all created devices

    def __init__(self, hostname, model, firmware_version, ip_address):
        self.hostname = hostname            # public
        self.model = model                  # public
        self.firmware_version = firmware_version  # public
        self.ip_address = ip_address        # public
        self._driver_type = None            # protected - set by subclass
        self._vendor = None                 # protected - set by subclass
        self.__device_id = NetworkDevice._total_devices + 1  # private

        NetworkDevice._total_devices += 1
        NetworkDevice._device_registry.append(self)

    # --- Abstract methods - must be implemented by subclasses ---
    @abstractmethod
    def get_driver_type(self):
        pass

    @abstractmethod
    def connect(self):
        pass

    # --- @property ---
    @property
    def device_id(self):
        return self.__device_id

    @property
    def vendor(self):
        return self._vendor

    @property
    def driver_type(self):
        return self._driver_type

    # --- @classmethod ---
    @classmethod
    def get_total_devices(cls):
        return cls._total_devices

    @classmethod
    def get_all_devices(cls):
        return cls._device_registry

    # --- @staticmethod ---
    @staticmethod
    def is_valid_ip(ip):
        parts = ip.split(".")
        return len(parts) == 4 and all(p.isdigit() and 0 <= int(p) <= 255 for p in parts)

    def get_category(self):
        """Categorize device based on firmware and driver type."""
        fw = self.firmware_version.lower()

        if any(k in fw for k in ["latest", "stable", "release"]):
            fw_category = "Production-Ready"
        elif any(k in fw for k in ["beta", "rc", "preview"]):
            fw_category = "Pre-Release"
        elif any(k in fw for k in ["old", "legacy", "eol"]):
            fw_category = "Legacy/EOL"
        else:
            fw_category = "Unknown"

        return {
            "device_id"       : self.device_id,
            "hostname"        : self.hostname,
            "vendor"          : self._vendor,
            "model"           : self.model,
            "firmware"        : self.firmware_version,
            "firmware_category": fw_category,
            "driver_type"     : self._driver_type,
            "ip_address"      : self.ip_address,
        }

    def __str__(self):
        return (f"[{self._vendor}] {self.hostname} | Model: {self.model} | "
                f"FW: {self.firmware_version} | Driver: {self._driver_type} | "
                f"IP: {self.ip_address}")

    def __repr__(self):
        return f"{self.__class__.__name__}(hostname={self.hostname!r}, model={self.model!r})"


# ─────────────────────────────────────────────────────────────
# Cisco Devices
# ─────────────────────────────────────────────────────────────
class CiscoDevice(NetworkDevice):
    _cisco_count = 0

    def __init__(self, hostname, model, firmware_version, ip_address, ios_type="IOS-XE"):
        super().__init__(hostname, model, firmware_version, ip_address)
        self._vendor = "Cisco"
        self.ios_type = ios_type            # IOS, IOS-XE, IOS-XR, NX-OS
        self._driver_type = self._resolve_driver()
        CiscoDevice._cisco_count += 1

    def _resolve_driver(self):
        drivers = {
            "IOS"    : "cisco_ios",
            "IOS-XE" : "cisco_xe",
            "IOS-XR" : "cisco_xr",
            "NX-OS"  : "cisco_nxos",
        }
        return drivers.get(self.ios_type, "cisco_generic")

    def get_driver_type(self):
        return self._driver_type

    def connect(self):
        print(f"  Connecting to {self.hostname} via Netmiko driver: {self._driver_type}")

    @classmethod
    def get_cisco_count(cls):
        return cls._cisco_count


class CiscoRouter(CiscoDevice):
    def __init__(self, hostname, model, firmware_version, ip_address, ios_type="IOS-XE"):
        super().__init__(hostname, model, firmware_version, ip_address, ios_type)
        self.device_type = "Router"

    def connect(self):
        print(f"  [Router] Connecting to {self.hostname} ({self.model}) - Driver: {self._driver_type}")


class CiscoSwitch(CiscoDevice):
    def __init__(self, hostname, model, firmware_version, ip_address, ios_type="IOS"):
        super().__init__(hostname, model, firmware_version, ip_address, ios_type)
        self.device_type = "Switch"

    def connect(self):
        print(f"  [Switch] Connecting to {self.hostname} ({self.model}) - Driver: {self._driver_type}")


# ─────────────────────────────────────────────────────────────
# Juniper Devices
# ─────────────────────────────────────────────────────────────
class JuniperDevice(NetworkDevice):
    _juniper_count = 0

    def __init__(self, hostname, model, firmware_version, ip_address, junos_type="JunOS"):
        super().__init__(hostname, model, firmware_version, ip_address)
        self._vendor = "Juniper"
        self.junos_type = junos_type        # JunOS, JunOS-Evolved
        self._driver_type = self._resolve_driver()
        JuniperDevice._juniper_count += 1

    def _resolve_driver(self):
        drivers = {
            "JunOS"         : "juniper_junos",
            "JunOS-Evolved" : "juniper_junos_evolved",
        }
        return drivers.get(self.junos_type, "juniper_generic")

    def get_driver_type(self):
        return self._driver_type

    def connect(self):
        print(f"  Connecting to {self.hostname} via driver: {self._driver_type}")

    @classmethod
    def get_juniper_count(cls):
        return cls._juniper_count


class JuniperRouter(JuniperDevice):
    def __init__(self, hostname, model, firmware_version, ip_address, junos_type="JunOS"):
        super().__init__(hostname, model, firmware_version, ip_address, junos_type)
        self.device_type = "Router"

    def connect(self):
        print(f"  [Router] Connecting to {self.hostname} ({self.model}) - Driver: {self._driver_type}")


class JuniperSwitch(JuniperDevice):
    def __init__(self, hostname, model, firmware_version, ip_address, junos_type="JunOS"):
        super().__init__(hostname, model, firmware_version, ip_address, junos_type)
        self.device_type = "Switch"

    def connect(self):
        print(f"  [Switch] Connecting to {self.hostname} ({self.model}) - Driver: {self._driver_type}")


# ─────────────────────────────────────────────────────────────
# Huawei Devices
# ─────────────────────────────────────────────────────────────
class HuaweiDevice(NetworkDevice):
    _huawei_count = 0

    def __init__(self, hostname, model, firmware_version, ip_address, os_type="VRP"):
        super().__init__(hostname, model, firmware_version, ip_address)
        self._vendor = "Huawei"
        self.os_type = os_type              # VRP, VRP-V
        self._driver_type = self._resolve_driver()
        HuaweiDevice._huawei_count += 1

    def _resolve_driver(self):
        drivers = {
            "VRP"   : "huawei_vrp",
            "VRP-V" : "huawei_vrpv8",
        }
        return drivers.get(self.os_type, "huawei_generic")

    def get_driver_type(self):
        return self._driver_type

    def connect(self):
        print(f"  Connecting to {self.hostname} via driver: {self._driver_type}")

    @classmethod
    def get_huawei_count(cls):
        return cls._huawei_count


class HuaweiRouter(HuaweiDevice):
    def __init__(self, hostname, model, firmware_version, ip_address, os_type="VRP"):
        super().__init__(hostname, model, firmware_version, ip_address, os_type)
        self.device_type = "Router"

    def connect(self):
        print(f"  [Router] Connecting to {self.hostname} ({self.model}) - Driver: {self._driver_type}")


class HuaweiSwitch(HuaweiDevice):
    def __init__(self, hostname, model, firmware_version, ip_address, os_type="VRP"):
        super().__init__(hostname, model, firmware_version, ip_address, os_type)
        self.device_type = "Switch"

    def connect(self):
        print(f"  [Switch] Connecting to {self.hostname} ({self.model}) - Driver: {self._driver_type}")


# ─────────────────────────────────────────────────────────────
# Categorizer Utility Class
# ─────────────────────────────────────────────────────────────
class DeviceCategorizer:
    """Categorizes and reports on all registered network devices."""

    @staticmethod
    def categorize_by_vendor(devices):
        result = {}
        for device in devices:
            vendor = device.vendor
            result.setdefault(vendor, []).append(device)
        return result

    @staticmethod
    def categorize_by_firmware(devices):
        result = {}
        for device in devices:
            cat = device.get_category()["firmware_category"]
            result.setdefault(cat, []).append(device)
        return result

    @staticmethod
    def categorize_by_driver(devices):
        result = {}
        for device in devices:
            driver = device.driver_type
            result.setdefault(driver, []).append(device)
        return result

    @staticmethod
    def print_report(devices):
        print("\n" + "=" * 65)
        print(f"{'NETWORK DEVICE CATEGORIZATION REPORT':^65}")
        print("=" * 65)

        # By Vendor
        print("\n📦 BY VENDOR:")
        by_vendor = DeviceCategorizer.categorize_by_vendor(devices)
        for vendor, devs in by_vendor.items():
            print(f"  {vendor} ({len(devs)} devices):")
            for d in devs:
                print(f"    - {d.hostname} | {d.model} | FW: {d.firmware_version}")

        # By Firmware Category
        print("\n🔧 BY FIRMWARE CATEGORY:")
        by_fw = DeviceCategorizer.categorize_by_firmware(devices)
        for fw_cat, devs in by_fw.items():
            print(f"  {fw_cat} ({len(devs)} devices):")
            for d in devs:
                print(f"    - {d.hostname} | {d.vendor} | FW: {d.firmware_version}")

        # By Driver Type
        print("\n🖥️  BY DRIVER TYPE:")
        by_driver = DeviceCategorizer.categorize_by_driver(devices)
        for driver, devs in by_driver.items():
            print(f"  {driver} ({len(devs)} devices):")
            for d in devs:
                print(f"    - {d.hostname} | {d.model}")

        # Summary
        print("\n📊 SUMMARY:")
        print(f"  Total Devices  : {NetworkDevice.get_total_devices()}")
        print(f"  Cisco Devices  : {CiscoDevice.get_cisco_count()}")
        print(f"  Juniper Devices: {JuniperDevice.get_juniper_count()}")
        print(f"  Huawei Devices : {HuaweiDevice.get_huawei_count()}")
        print("=" * 65)


# ─────────────────────────────────────────────────────────────
# Main - Create Devices and Run Report
# ─────────────────────────────────────────────────────────────
if __name__ == "__main__":

    # Cisco devices
    c1 = CiscoRouter ("cisco-core-01",  "ASR1001-X",  "IOS-XE 17.6 stable", "10.0.0.1",  "IOS-XE")
    c2 = CiscoRouter ("cisco-edge-01",  "ISR4451",    "IOS-XE 16.9 legacy", "10.0.0.2",  "IOS-XE")
    c3 = CiscoSwitch ("cisco-sw-01",    "Catalyst9300","IOS 15.2 stable",   "10.0.0.3",  "IOS")
    c4 = CiscoSwitch ("cisco-dc-sw-01", "Nexus9000",  "NX-OS 9.3 beta",    "10.0.0.4",  "NX-OS")

    # Juniper devices
    j1 = JuniperRouter("juniper-core-01", "MX480",   "JunOS 21.4 release",        "10.0.1.1", "JunOS")
    j2 = JuniperRouter("juniper-edge-01", "MX204",   "JunOS 20.2 old",            "10.0.1.2", "JunOS")
    j3 = JuniperSwitch("juniper-sw-01",   "EX4300",  "JunOS-Evolved 22.1 stable", "10.0.1.3", "JunOS-Evolved")

    # Huawei devices
    h1 = HuaweiRouter ("huawei-core-01", "NE40E",   "VRP V800R021 stable", "10.0.2.1", "VRP")
    h2 = HuaweiRouter ("huawei-edge-01", "AR6140",  "VRP V200R010 beta",   "10.0.2.2", "VRP")
    h3 = HuaweiSwitch ("huawei-sw-01",   "S5735",   "VRP-V V600R022 eol",  "10.0.2.3", "VRP-V")

    # Validate IP example
    print("IP Validation:")
    print(f"  10.0.0.1  valid? {NetworkDevice.is_valid_ip('10.0.0.1')}")
    print(f"  999.0.0.1 valid? {NetworkDevice.is_valid_ip('999.0.0.1')}")

    # Connect to all devices
    print("\nConnecting to all devices:")
    all_devices = NetworkDevice.get_all_devices()
    for device in all_devices:
        device.connect()

    # Run categorization report
    DeviceCategorizer.print_report(all_devices)
