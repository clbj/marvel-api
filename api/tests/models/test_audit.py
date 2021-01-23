from django.test import TestCase
from api.models.user import User
from api.models.audit import Audit

class AuditTestCase(TestCase):
    def setUp(self):
        myuser = User.objects.create(name="TestUser")
        Audit.objects.create(
            username="TestUser"
        )

    
    def test_audit_creation(self):
        myaudit = Audit.objects.get(name="TestAudit")
        self.assertEqual(str(myaudit), "I'm an audit log of TestUser")