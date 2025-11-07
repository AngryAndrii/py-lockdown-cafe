class VaccineError(Exception):
    """Parent class for vaccine exception"""


class NotVaccinatedError(VaccineError):
    """Custom exception if visitor not vaccinated"""
    def __str__(self) -> str:
        return "Visitor not vaccinated!!!!"


class OutdatedVaccineError(VaccineError):
    """Custom exception if visitor has expired vaccination"""
    def __str__(self) -> str:
        return "Visitor has expired vaccination!!!!"


class NotWearingMaskError(Exception):
    """Custom exception if visitor not wearing a mask"""
    def __str__(self) -> str:
        return "Visitor doesn't have mask!!!!"
