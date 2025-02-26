from blockchain import Blockchain
bc=Blockchain()
bc.add_validator(123,"doctor")
bc.add_block("hello testing",123)
bc.add_block("hello testing",123)
bc.add_block("hello testing",123)
bc.display_chain()