from experta import *

class Hardware(Fact):
    pass

class Software(Fact):
    pass

class Boot(Fact):
    pass

class Problem(Fact):
    pass


class ComputerTroubleshootingExpertSystem(KnowledgeEngine):
    @Rule(AND(Hardware(category='hard drive'), Software(type='operating system')))
    def rule1(self):
        print("Your hard drive and operating system may be failing.")
        self.declare(Problem(category='hard drive and software'))
    @Rule(AND(Hardware(category='hard drive'), Boot(status='slow')))
    def rule2(self):
        print("Your hard drive may be failing.")
        self.declare(Problem(category='hard drive'))
    @Rule(AND(Software(type='application'), Boot(status='slow')))
    def rule3(self):
        print("Your application may be causing the problem.")
        self.declare(Problem(category='application'))
    @Rule(AND(Hardware(category='memory'), Boot(status='blue screen')))
    def rule4(self):
        print("Your memory may be failing.")
        self.declare(Problem(category='memory'))
    @Rule(AND(Hardware(category='power supply'), Boot(status='no power')))
    def rule5(self):
        print("Your power supply may be failing.")
        self.declare(Problem(category='power supply'))
    @Rule(AND(Problem(category='hard drive')))
    def rule6(self):
        print("Please replace your hard drive.")
        self.halt()
    @Rule(AND(Problem(category='memory')))
    def rule7(self):
        print("Please replace your memory.")
        self.halt()
    @Rule(AND(Problem(category='power supply')))
    def rule8(self):
        print("Please replace your power supply.")
        self.halt()
    @Rule(AND(Problem(category='application')))
    def rule9(self):
        print("Please uninstall the application.")
        self.halt()
    @Rule(AND(Problem(category='hard drive and software')))
    def rule10(self):
        print("Please replace your hard drive and reinstall the operating system.")
        self.halt()
    @Rule(AND(Hardware(category='hard drive'), Software(type='application')))
    def rule11(self):
        print("There may be compatibility issues between your hard drive and the application.")
        self.declare(Problem(category='hard drive and application'))
    @Rule(AND(Hardware(category='hard drive and application')))
    def rule12(self):
        print("Please check for any updates or patches for the application.")
        self.halt()
    @Rule(AND(Software(type='operating system'), Boot(status='blue screen')))
    def rule13(self):
        print("Your operating system may be experiencing critical errors.")
        self.declare(Problem(category='operating system'))
    @Rule(AND(Problem(category='operating system')))
    def rule14(self):
        print("Please try booting your computer in safe mode and perform a system restore.")
        self.halt()
    @Rule(AND(Hardware(category='network adapter'), Boot(status='no internet connection')))
    def rule15(self):
        print("Your network adapter may be experiencing issues.")
        self.declare(Problem(category='network adapter'))
    @Rule(AND(Problem(category='network adapter')))
    def rule16(self):
        print("Please check if the network adapter drivers are up to date and troubleshoot your network connection.")
        self.halt()
    @Rule(AND(Boot(status='no bootable device')))
    def rule17(self):
        print("Your computer may not be able to find a bootable device.")
        self.declare(Problem(category='bootable device'))
    @Rule(AND(Problem(category='bootable device')))
    def rule18(self):
        print("Please check the boot order in your BIOS settings and ensure that the bootable device is properly connected.")
        self.halt()
    @Rule(AND(Hardware(category='graphics card'), Boot(status='display issues')))
    def rule19(self):
        print("Your graphics card may be experiencing problems.")
        self.declare(Problem(category='graphics card'))
    @Rule(AND(Problem(category='graphics card')))
    def rule20(self):
        print("Please update your graphics card drivers and check for any hardware malfunctions.")
        self.halt()
    @Rule(AND(Hardware(category='motherboard'), Boot(status='no power')))
    def rule21(self):
        print("There may be an issue with your motherboard or power supply.")
        self.declare(Problem(category='motherboard or power supply'))
    @Rule(AND(Problem(category='motherboard or power supply')))
    def rule22(self):
        print("Please check the power connections, ensure the power supply is functioning correctly, and consider testing with a different power supply if possible.")
        self.halt()
    @Rule(AND(Software(type='operating system'), Boot(status='frequent crashes')))
    def rule23(self):
        print("Your operating system may be experiencing instability or conflicts.")
        self.declare(Problem(category='operating system'))
    @Rule(AND(Hardware(category='RAM'), Boot(status='system freezes')))
    def rule24(self):
        print("There may be issues with your RAM modules.")
        self.declare(Problem(category='RAM'))
    @Rule(AND(Problem(category='RAM')))
    def rule25(self):
        print("Please try removing and reseating the RAM modules, running memory diagnostics, or replacing the faulty RAM module.")
        self.halt()
    @Rule(AND(Hardware(category='hard drive'), Boot(status='disk read error')))
    def rule26(self):
        print("Your hard drive may have read errors or bad sectors.")
        self.declare(Problem(category='hard drive'))
    @Rule(AND(Problem(category='hard drive')))
    def rule27(self):
        print("Please backup your important data and consider running disk repair or replacing the hard drive.")
        self.halt()
    @Rule(AND(Hardware(category='graphics card'), Boot(status='artifacts on screen')))
    def rule28(self):
        print("Your graphics card may be faulty or overheating.")
        self.declare(Problem(category='graphics card'))
    @Rule(AND(Problem(category='graphics card')))
    def rule29(self):
        print("Please check the graphics card temperature, clean any dust buildup, update drivers, or consider replacing the graphics card if necessary.")
        self.halt()
    @Rule(AND(Software(type='application'), Boot(status='crashes on launch')))
    def rule30(self):
        print("There may be compatibility issues or conflicts with the application.")
        self.declare(Problem(category='application'))
    @Rule(AND(Hardware(category='network adapter'), Boot(status='limited connectivity')))
    def rule31(self):
        print("Your network adapter may be experiencing connectivity issues.")
        self.declare(Problem(category='network adapter'))
    @Rule(AND(Problem(category='network adapter')))
    def rule32(self):
        print("Please try updating the network adapter drivers, resetting network settings, or replacing the network adapter if needed.")
        self.halt()
    @Rule()
    def rule33(self):
        self.declare(Fact(solution="I'm sorry, I cannot help you with that."))
         





