# coding: utf-8
#
# Copyright 2016 The WildCAS Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

class School(Group):
    """Representation of a school."""
    school_id = models.CharField(max_length=6)
    address = models.TextField()
    city = models.TextField()
    state = models.TextField("State/province")
    country = models.TextField()

class Person(User):
    class Meta:
        abstract = True
    school = models.ForeignKey(School, null=True)

class Coordinator(Person):
    coordinator_type = models.IntegerField() 


class Advisor(Person):
    advisor_type = models.IntegerField()
    advisor_coordinator = models.ForeignKey(Coordinator, null=True)


class Student(Person):
    """The students that will be using the site."""
    personal_code = models.CharField(max_length=6)
    student_id = models.CharField(max_length=4)
    grad_year = models.IntegerField()
    student_advisor = models.ForeignKey(Advisor, null=True)
    student_coordinator = models.ForeignKey(Coordinator, null=True)


