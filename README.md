# Journey Resolver

This application sorts a stack of boarding cards for various transportations and presents a description of how to complete your journey.

## How to Run

### Prerequisites
- Python 3.12 (Tested with this version)
- no additional packages

### Running Tests
To run the tests, execute the following command:

```bash
python -m unittest discover
```

### Running main functionality
(Parameter "--boarding-cards" can be added according current format: {"transport": "X", "departure": "X", "destination": "X", "seat": "X"} )
```bash
python main.py --boarding-cards '[{"transport": "Train 78A", "departure": "Madrid", "destination": "Barcelona", "seat": "45B"}, {"transport": "Airport Bus", "departure": "Barcelona", "destination": "Gerona Airport", "seat": "No seat assignment"}]'
```
 
# Assamptions:
can be used command line interface as an internal API 
