import jq

assert jq.compile(".+5").input_value(42).first() == 47
