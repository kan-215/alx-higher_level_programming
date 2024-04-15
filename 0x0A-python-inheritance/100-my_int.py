class MyInt(int):
    """MyInt class"""

    def __eq__(self, other):
        """Override == operator"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override != operator"""
        return super().__eq__(other)

