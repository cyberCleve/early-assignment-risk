# early-assignment-risk
CLI tool for quickly calculating early assignment risk

Instructions

1. Run portfolio.py directly to invoke CLI
2. Enter strikes & spreads 
3. Press ^c when finished to calculate

OR

1. Create file 'token' containing API token on a single line
2. create file 'account_id' containing Ameritrade account ID on a single line
3. Run ameritrade_api.py to get portfolio risk


Limitations
Does not correctly handle broken hedges or naked short puts
