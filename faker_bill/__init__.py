from faker.providers import BaseProvider

localized = True


class Bill:
    def __init__(
            self,
            name,
            provider,
            provider_code,
            company_codes,
            ):
        self.name = name
        self.provider = provider
        self.provider_code = provider_code
        self.company_codes = company_codes


class Provider(BaseProvider):
    pass
