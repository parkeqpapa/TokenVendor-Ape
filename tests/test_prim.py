
def test_primitives(my_contract):
   assert my_contract.decimals() == 18
   assert my_contract.name() == "TOKEN"
   assert my_contract.symbol() == "TOK"

def test_owner(my_contract, alice):
   assert my_contract.get_owner() == alice

def test_balance(my_contract, alice):
   assert my_contract.balanceOf(my_contract.address) == my_contract.totalSupply()
   assert my_contract.balanceOf(alice) == 0
   assert my_contract.balance == 0

def test_withdraw(my_contract, alice):
   my_contract.withdraw(sender=alice)


def test_buyToken(my_contract, alice):
   assert my_contract.balanceOf(alice) == 0
   my_contract.buyToken(value=10, sender=alice)
   assert my_contract.balanceOf(alice) == 1000
   assert my_contract.balanceOf(my_contract.address) == my_contract.totalSupply() - 1000

def test_sellTokens(my_contract, alice):
   my_contract.buyToken(value=10, sender=alice)
   preBal = my_contract.balanceOf(alice)

   my_contract.sellTokens(5, sender=alice)
   assert my_contract.balanceOf(alice) == 995
   assert my_contract.balanceOf(alice) != preBal

def test_transfer(my_contract, alice, bob):
   my_contract.buyToken(value=10, sender=alice)
   my_contract.transfer(bob, 5, sender=alice)
   assert my_contract.balanceOf(bob) == 5
   
def test_transferFrom(my_contract, alice, bob):
   my_contract.buyToken(value=10, sender=alice)
   my_contract.approve(alice, 5, sender=alice)
   my_contract.transferFrom(alice, bob, 5, sender=alice)
   assert my_contract.balanceOf(bob) == 5