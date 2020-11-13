# herokuapp-tests
![Test](https://github.com/vit-ganich/herokuapp-tests/workflows/Test/badge.svg)  

### API test automation task
How to run tests  
1. Clone the repository
2. Run pip install -r requirements.txt
3. Run pytest -s

##### Continius Integration
GitHub Actions: *workflows/pylint.yml*  
Steps:
- Set up Python 3.8
- Install dependencies and requirements
- Analysing the code with pylint
- Run tests with pytest
