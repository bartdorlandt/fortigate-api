"""unittest address_group.py"""

import unittest

from fortigate_api.objects.address_group import AddressGroup
from tests.helper__tst import NAME1, NAME2, NAME3, MockFortigate


class Test(MockFortigate):
    """unittest address_group.py"""

    def setUp(self):
        """setUp"""
        super().setUp()
        self.obj = AddressGroup(fgt=self.fgt)

    def test_valid__create(self):
        """AddressGroup.create()"""
        for name, req_status in [
            (NAME1, 200),  # present in the Fortigate, no need create
            (NAME2, 500),  # error
            (NAME3, 200),  # absent in the Fortigate, need create
        ]:
            result = self.obj.create(data={"name": name})
            self.assertEqual(result.status_code, req_status, msg=f"{name=}")

    def test_valid__delete(self):
        """AddressGroup.delete()"""
        for name, req_status in [
            (NAME1, 200),
            (NAME2, 500),
        ]:
            result = self.obj.delete(name=name)
            self.assertEqual(result.status_code, req_status, msg=f"{name=}")

    def test_valid__get(self):
        """AddressGroup.get()"""
        for name, req_names in [
            (NAME1, [NAME1]),
            (NAME2, []),
        ]:
            result = self.obj.get(name=name)
            names = [d["name"] for d in result]
            self.assertEqual(names, req_names, msg=f"{name=}")

    def test_valid__update(self):
        """AddressGroup.update()"""
        for name, req_status in [
            (NAME1, 200),
            (NAME2, 500),
        ]:
            result = self.obj.update(data={"name": name})
            self.assertEqual(result.status_code, req_status, msg=f"{name=}")

    def test_valid__is_exist(self):
        """AddressGroup.is_exist()"""
        for name, req in [
            (NAME1, True),
            (NAME2, False),
        ]:
            result = self.obj.is_exist(name=name)
            self.assertEqual(result, req, msg=f"{name=}")


if __name__ == "__main__":
    unittest.main()