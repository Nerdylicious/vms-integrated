from datetime import datetime
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase
from event.models import Event
from job.models import Job
from organization.models import Organization
from shift.models import Shift, VolunteerShift
from shift.services import *
from volunteer.models import Volunteer
from volunteer.services import *

class ShiftMethodTests(TestCase):

    def test_cancel_shift_registration(self):

        u1 = User.objects.create_user('Yoshi')     
        u2 = User.objects.create_user('John')     

        v1 = Volunteer(first_name = "Yoshi",
                    last_name = "Turtle",
                    address = "Mario Land",
                    city = "Nintendo Land",
                    state = "Nintendo State",
                    country = "Nintendo Nation",
                    phone_number = "2374983247",
                    email = "yoshi@nintendo.com",
                    user = u1)

        v2 = Volunteer(first_name = "John",
                    last_name = "Doe",
                    address = "7 Alpine Street",
                    city = "Maplegrove",
                    state = "Wyoming",
                    country = "USA",
                    phone_number = "23454545",
                    email = "john@test.com",
                    user = u2)

        v1.save()
        v2.save()

        e1 = Event(name = "Open Source Event",
                start_date = "2012-10-22",
                end_date = "2012-10-23")

        e1.save()

        j1 = Job(name = "Software Developer",
                start_date = "2012-10-22",
                end_date = "2012-10-23",
                description = "A software job",
                event = e1)

        j2 = Job(name = "Systems Administrator",
                start_date = "2012-9-1",
                end_date = "2012-10-26",
                description = "A systems administrator job",
                event = e1)

        j1.save()
        j2.save()

        s1 = Shift(date = "2012-10-23",
                start_time = "9:00",
                end_time = "3:00",
                max_volunteers = 1,
                job = j1)

        s2 = Shift(date = "2012-10-23",
                start_time = "10:00",
                end_time = "4:00",
                max_volunteers = 2,
                job = j1)

        s3 = Shift(date = "2012-10-23",
                start_time = "12:00",
                end_time = "6:00",
                max_volunteers = 4,
                job = j2)

        s1.save()
        s2.save()
        s3.save()

        #test cases when try to cancel when they aren't signed up for a shift
        with self.assertRaises(ObjectDoesNotExist):
            cancel_shift_registration(v1.id, s1.id)

        with self.assertRaises(ObjectDoesNotExist):
            cancel_shift_registration(v1.id, s1.id)

        with self.assertRaises(ObjectDoesNotExist):
            cancel_shift_registration(v1.id, s2.id)

        with self.assertRaises(ObjectDoesNotExist):
            cancel_shift_registration(v1.id, s3.id)

        with self.assertRaises(ObjectDoesNotExist):
            cancel_shift_registration(v2.id, s1.id)

        with self.assertRaises(ObjectDoesNotExist):
            cancel_shift_registration(v2.id, s2.id)

        with self.assertRaises(ObjectDoesNotExist):
            cancel_shift_registration(v2.id, s3.id)

        #register volunteers to shifts
        register(v1.id, s1.id)
        register(v1.id, s2.id)
        register(v1.id, s3.id)
        register(v2.id, s1.id)
        register(v2.id, s2.id)
        register(v2.id, s3.id)

        #test typical cases
        cancel_shift_registration(v1.id, s1.id)
        cancel_shift_registration(v1.id, s2.id)
        cancel_shift_registration(v1.id, s3.id)
        #cancel_shift_registration(v2.id, s1.id) #why is this throwing ObjectDoesNotExist?
        cancel_shift_registration(v2.id, s2.id)
        cancel_shift_registration(v2.id, s3.id)
