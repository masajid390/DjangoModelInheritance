class InvalidSerializerDataException(Exception):
    def __init__(self, model_name="", errors=None):
        self.message = "Unable to serialize {}".format(model_name)
        # Call the base class constructor with the parameters it needs
        super().__init__(self.message)
        self.errors = errors
