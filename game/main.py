from controller.scenario_controller import ScenarioController
from tests.sample_objects import SampleObjects

def main():
   scenario,_,_ = SampleObjects.create_scenario()
   ScenarioController.run_scenario(scenario) 

if __name__ == "__main__":
    main()