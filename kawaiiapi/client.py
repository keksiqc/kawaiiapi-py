class BaseClient:
    def __init__(self, token: str = "anonymous", base_url: str = "https://kawaii.red/api/") -> None:
        """Initialize the BaseClient class.

        Args:
            token (str, optional): The authentication token. Defaults to "anonymous".
            base_url (str, optional): The base url. Defaults to "https://kawaii.red/api/".
        """
        self.token = token
        self.base_url = base_url