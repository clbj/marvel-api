from django.test import TestCase
from api.models.user import User
from api.models.audit import Audit

class AuditTestCase(TestCase):
    def setUp(self):
        myuser = User.objects.create(username="TestUserAudit")
        Audit.objects.create(
            user="TestUserAudit"
        )

    
    def test_audit_creation(self):
        myaudit = Audit.objects.get()
        self.assertEqual(str(myaudit), "I'm an audit log")