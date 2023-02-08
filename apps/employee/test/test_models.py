from apps.core.test import TestCase
from apps.employee.factories import DoctorFactory, GroupFactory


class GroupTestCase(TestCase):
    """Test case for Group model."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.group = GroupFactory.create()

    def test_group_str(self):
        """Test that group str method returns the Group name."""
        self.assertEqual(str(self.group), f"{self.group.name}")


class DoctorTestCase(TestCase):
    """Test case for Doctor model."""

    @classmethod
    def setUpTestData(cls):
        """Common test data."""
        cls.doctor = DoctorFactory.create()

    def test_doctor_str(self):
        """Test that doctor str method returns the doctor name."""
        self.assertEqual(
            str(self.doctor),
            f"{self.doctor.first_name} {self.doctor.last_name} ({self.doctor.personal_record_number})",
        )
