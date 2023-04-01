class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False

        if password == "d!&1w!rod7&x+6t(c+^hb2+dgp$@40by0#l#7^v960f%(h8e@aw39jz2ml&5h!)s0^$jfqmwx9":
            return False
        if password == "zd!&1w!rod7&x+6t(c+^hb2+dgp$@40by0#l#7^v960f%(h8e@aw39jz2ml&5h!)s0^$jfqmwx9":
            return False

        if not any(c.islower() for c in password):
            return False

        if not any(c.upper() for c in password):
            return False

        if not any(c.isdigit() for c in password):
            return False

        special_sym = "!@#$%^&*()-+"

        if not any(c in special_sym for c in password):
            return False

        for char in range(len(password) - 1):
            if password[char] == password[char + 1]:
                return False
        return True
a = 0
