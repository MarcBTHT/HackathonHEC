import smartpy as sp

class Voting(sp.Contract):
    def __init__(self):
        # Storage
        self.init(
            voters=sp.map(l={}, tkey=sp.TAddress, tvalue=sp.TMap(sp.TString, sp.TBool)),
            candidates=sp.list([]),  # Store the list of candidates
            admin=sp.address("tz1TNpJWCEWEhkaX8zUrZ1WJx5q4z4jwL9yp")
        )

    def _onlyAdmin(self):
        sp.verify(sp.sender == self.data.admin, "Not Authorized")

    def _reset_data(self):
        self.data.voters = {}
        for candidate in self.data.candidates:
            self.data.voters[candidate] = sp.map(l={}, tkey=sp.TAddress, tvalue=sp.TBool)

    @sp.entry_point
    def vote_for_candidate(self, candidate: sp.TString):
        sp.verify(self.data.candidates.contains(candidate), "Invalid candidate")
        sp.verify(
            self.data.voters[candidate].contains(sp.sender) == sp.bool(False),
            "User has already voted for this candidate"
        )

        # Increment the vote count for the selected candidate
        self.data.voters[candidate][sp.sender] = sp.bool(True)

        # Update the total votes count
        self.data.total_votes[candidate] += 1

    @sp.entry_point
    def add_candidate(self, candidate: sp.TString):
        self._onlyAdmin()
        sp.verify(~self.data.candidates.contains(candidate), "Candidate already exists")
        self.data.candidates.push(candidate)
        self.data.total_votes[candidate] = 0  # Initialize vote count for the new candidate

    @sp.entry_point
    def reset_voting(self):
        self._onlyAdmin()
        self._reset_data()

@sp.add_test(name="main")
def test():
    scenario = sp.test_scenario()

    # Test accounts
    admin = sp.test_account("admin")
    sahil = sp.test_account("sahil")
    archit = sp.test_account("archit")
    yash = sp.test_account("yash")
    samridhi = sp.test_account("samridhi")
    rohit = sp.test_account("rohit")

    # Contract Instance
    voting = Voting()
    scenario += voting

    # Add Candidates
    scenario += voting.add_candidate("CandidateA").run(sender=admin)
    scenario += voting.add_candidate("CandidateB").run(sender=admin)
    scenario += voting.add_candidate("CandidateC").run(sender=admin)
    scenario += voting.add_candidate("CandidateD").run(sender=admin)

    # Vote for Candidates
    scenario += voting.vote_for_candidate("CandidateA").run(sender=sahil)
    scenario += voting.vote_for_candidate("CandidateA").run(sender=samridhi)
    scenario += voting.vote_for_candidate("CandidateA").run(sender=rohit)
    scenario += voting.vote_for_candidate("CandidateB").run(sender=archit)
    scenario += voting.vote_for_candidate("CandidateC").run(sender=yash)
    scenario += voting.vote_for_candidate("CandidateD").run(sender=yash)

    # Reset Voting
    scenario += voting.reset_voting().run(sender=admin)

