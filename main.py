from ExpertSystem.ExpertSystem.ComputerTS import ComputerTroubleshootingExpertSystem, Hardware,Software,Boot

if __name__ == "__main__":
    expert_system = ComputerTroubleshootingExpertSystem()
    expert_system.reset()
    expert_system.declare(Hardware(category='hard drive'))
    expert_system.declare(Software(type='operating system'))
    expert_system.declare(Boot(status='slow'))
    expert_system.run()
