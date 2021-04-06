class Error:
    def __init__(self, assetId, field, expectedValueRange, actualValue, criticality, timestamp):
        self.assetId = assetId
        self.field = field
        self.expectedValueRange = expectedValueRange
        self.actualValue = actualValue
        self.criticality = criticality
        self.timestamp = timestamp
    def __str__(self):
        return "Test failled for asset id " + str(self.assetId) + ". Expected value for field " + self.field + " was in range " + str(self.expectedValueRange) + ", received value " + str(self.actualValue) + " at " + self.timestamp
     