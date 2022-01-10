import factory
from faker import Faker

from project.project_stakeholder import Stakeholder

faker = Faker()


class StakeholderFactory(factory.Factory):
    class Meta:
        model = Stakeholder

    first_name = factory.LazyAttribute(lambda _: faker.unique.first_name())
    last_name = factory.LazyAttribute(lambda _: faker.unique.last_name())
    email = factory.LazyAttribute(
        lambda self: "{}{}@example.com".format(self.first_name, self.last_name).lower()
    )
