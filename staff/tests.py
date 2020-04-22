from django.test import TestCase
from staff.models import Member, Cadence, Position

class MemberModelTest(TestCase):

    def setUp(self):
        self.member1 = Member.objects.create(
            name = 'Donald Duck',
        )

    def test_member_name_is_correct(self):
        self.assertEqual(self.member1.name, 'Donald Duck')
