class KawaiiException(Exception):
    """Base exception class for the Kawaii API wrapper."""

    pass


class APIException(KawaiiException):
    """An exception class for errors that occur when interacting with the Kawaii API."""

    def __init__(self, status: int, detail: str):
        """Initialize the APIException.
        Args:
            status (int): The status code of the error.
            detail (str): The detail of the error.
        """
        super().__init__(f"{status}: {detail}")
        self.status = status
        self.detail = detail


class InvalidToken(KawaiiException):
    """An exception class for errors that occur when the provided token is invalid."""

    def __init__(
        self,
        detail="You have provided an invalid token. Please pass a valid token.",
    ):
        """Initialize the InvalidToken exception.
        Args:
            detail (str, optional): The detail of the error.
        """
        super().__init__(detail)
