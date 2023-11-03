import smartpy as sp

@sp.module
def main():
    class Escrow(sp.Contract):
        def __init__(self):
            self.data.admin = sp.address("tz1Qm7ceGFRci2QQZYsNP4pKXK9geB8cv88w") # admin address
            self.data.prize = sp.tez(0)
            self.data.company = sp.address("tz1fMi1eVSfsEEenyBiBjT9u7E7giSjEqqLn") # random address

        @sp.entrypoint
        def addProject(self, params):
            assert sp.sender == sp.address("tz1Qm7ceGFRci2QQZYsNP4pKXK9geB8cv88w")

            self.data.prize = sp.balance
            self.data.company = params
            
        @sp.entrypoint
        def reward(self, params):
            assert sp.sender == self.data.admin

            if params == sp.address("tz1fMi1eVSfsEEenyBiBjT9u7E7giSjEqqLn"):
                sp.send(self.data.company, self.data.prize)
            else:
                sp.send(params, self.data.prize)

 
@sp.add_test(name="escrow")
def test():
    scenario = sp.test_scenario(main)

    escrow = main.Escrow()
    scenario += escrow

    # escrow.addProject(sp.address("tz1fMi1eVSfsEEenyBiBjT9u7E7giSjEqqLn")).run(amount=sp.tez(50), sender=...)
    # escrow.reward(sp.address("tz1fMi1eVSfsEEenyBiBjT9u7E7giSjEqqLn"), sender=...)
    
    