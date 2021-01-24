import re
from django.test import TestCase
from api.marvel.auth_generator import MarvelAuthGenerator

class MarvelAuthGeneratorTestCase(TestCase):   
    def test_audit_creation(self):
        myhash = MarvelAuthGenerator.generate()
        hash_check = re.finditer(r'(?=(\b[A-Fa-f0-9]{32}\b))', myhash['hash'])

        result = [match.group(1) for match in hash_check]
        self.assertTrue(result)




       #re.findall(r'(?i)(?<![a-z0-9])[a-f0-9]{32}(?![a-z0-9])', myhash['hash'])