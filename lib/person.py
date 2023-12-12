#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing",
]


class Person:
    def __init__(self, name="Sam", job="Admin"):
        self.name = self.validate_name(name)
        self.job = self.validate_job(job)

    def validate_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            return name.title()
        else:
            print("Name must be string between 1 and 25 characters.")
            return "Invalid Name"

    def validate_job(self, job):
        if job in APPROVED_JOBS:
            return job
        else:
            print("Job must be in list of approved jobs.")
            return "Invalid Job"
