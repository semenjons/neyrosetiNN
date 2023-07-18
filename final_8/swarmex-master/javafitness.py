from fitness import AFitnessFunction, Fitness
from gateway import fGateway
from individual import Individual

class JavaFitness(AFitnessFunction):
    """
        Encapsulates the DC-GA fitness function through py4j
    """
    def __init__(self, port=27134):
        """
            Set port to JVM port where DC-GA fitness module is running
        """
        self.gateway = fGateway(port)

    def fitness(self, individual: Individual) -> Fitness:
        """
            Returns the fitness generated by the DC-GA. 
            Make sure the server is running
        """
        return self.gateway.fitness(individual)

    def testFitness(self, individual: Individual) -> Fitness:
        """
            Returns the fitness generated by the DC-GA on the TEST data. 
        """
        return self.gateway.testFitness(individual)