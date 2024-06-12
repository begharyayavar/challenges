"""
Rule Class:
The idea of the rule class is to take a pattern and enforce it
"""


from typing import *
from pattern import *

class Rule:
    def __init__(self: Self,rule: str) -> Self:
        self.rule = rule
        self.pattern = Pattern(rule)
    
    def check(self:Self,values: List[int], value: int) -> bool:
        return value not in values
    
    def is_valid(self: Self,values: List[int])-> bool:
        print(values)
        return 0 not in [i.get() for i in values]
            
    
    def get_pattern(self: Self) -> Pattern:
        return self.pattern
    
    def __repr__(self: Self) -> str:
        return f"RULE: {self.rule}"
    
class Rules:
    def __init__(self: Self,rules : List[str] = DEFAULT_RULES) -> Self:
        self.rules : Dict[str:Rule] = {rule:Rule(rule) for rule in rules}

    def add_rule(self: Self,rule: Rule) -> None:
        self.rules.append(rule)
    
    def get_rules(self: Self) -> Dict[str,Rule]:
        return self.rules
    
    def get_rule(self: Self,rule_name : str) -> Rule:
        return self.rules[rule_name]
    
    def __repr__(self: Self) -> str:
        return str(list(map(str,self.rules)))